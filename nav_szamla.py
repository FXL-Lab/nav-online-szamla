import os
import requests
import xml.dom.minidom
from datetime import datetime, timedelta
import pandas as pd
import hashlib
import string
import random
import logging
import base64
import gzip
import json
import concurrent.futures
import threading
from typing import Tuple, Optional
import io
from flask import send_file
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from .nav_constans import mapping, line_mapping

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


ONLINE_SZAMLA_URL = "https://api.onlineszamla.nav.gov.hu/invoiceService/v3/"

HEADERS = {
    'Content-Type': 'application/xml',
    'Content-Type': 'application/xml'
}

# Retry decorator for NAV API calls
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type((
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException
    )),
    reraise=True
)
def make_nav_api_request(method: str, url: str, headers: dict, data: str, timeout: int = 30) -> requests.Response:
    """
    Make a retryable HTTP request to NAV API with exponential backoff.
    
    Args:
        method: HTTP method (GET, POST, etc.)
        url: Full URL to make request to
        headers: Request headers
        data: Request data/body
        timeout: Request timeout in seconds
        
    Returns:
        requests.Response: HTTP response object
        
    Raises:
        Exception: If all retry attempts fail
    """
    try:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data, timeout=timeout)
        else:
            response = requests.request(method, url, headers=headers, data=data, timeout=timeout)
        
        return response
        
    except (requests.exceptions.ConnectionError, 
            requests.exceptions.Timeout, 
            requests.exceptions.HTTPError,
            requests.exceptions.RequestException) as e:
        logger.warning(f"NAV API request failed (will retry if attempts remaining): {e}")
        raise  # Let tenacity handle the retry

def create_error_excel(error_message):
        """Helper function to create an Excel file with error message."""
        error_df = pd.DataFrame({
            'Hiba': ['Validációs hiba'],
            'Részletek': [error_message],
            'Dátum': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        })
        
        # Create Excel file in memory
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            error_df.to_excel(writer, sheet_name='Hiba', index=False)
            
            # Auto-adjust column widths
            worksheet = writer.sheets['Hiba']
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)
                worksheet.column_dimensions[column_letter].width = adjusted_width
        
        output.seek(0)
        
        # Generate error filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"nav_hiba_{timestamp}.xlsx"
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )

def validate_request_params(date_from: str, date_to: str, login: str, password: str, signer_key: str, invoice_direction: str, tax_number: str):
    # Validate required fields
    if not all([login, password, signer_key, date_from, date_to, invoice_direction]):
        return create_error_excel('Minden mező kitöltése kötelező!')
    
    # Validate invoice direction
    if invoice_direction not in ['OUTBOUND', 'INBOUND', 'BOTH']:
        return create_error_excel('Érvénytelen számla irány!')
    
    # Validate tax number format (should be 8 digits for Hungarian tax number)
    if tax_number and not (tax_number.isdigit() and len(tax_number) == 8):
        return create_error_excel('A magyar adószám 8 számjegyből áll a -x-xx rész nélkül!')
    
    # Validate date format and order
    try:
        start_date = datetime.strptime(date_from, '%Y-%m-%d')
        end_date = datetime.strptime(date_to, '%Y-%m-%d')
        if start_date > end_date:
            return create_error_excel('A kezdő dátum nem lehet későbbi a befejező dátumnál!')
        
        # Check if date range is too far in the future
        today = datetime.now().date()
        if start_date.date() > today:
            return create_error_excel('A kezdő dátum nem lehet jövőbeli!')
            
    except ValueError:
        return create_error_excel('Érvénytelen dátum formátum!')
    
    return None  
    

def create_df_from_xml(xml):
    invoices = xml.getElementsByTagName('invoiceDigest')
    if not invoices:
        invoices = xml.getElementsByTagName('ns2:invoiceDigest')

    if len(invoices) == 0:
        logger.info("No invoices found in XML response")
        return pd.DataFrame(columns=['invoiceId', 'invoiceOperation', 'issueDate', 'customerName', 'customerTaxNumber', 'dueDate', 'invoiceCurrency', 'netAmount', 'netAmountHuf', 'vatAmount', 'vatAmountHuf', 'originalInvoiceNumber', 'supplierName', 'supplierTaxNumber', 'invoiceCategory', 'invoiceAppearance', 'paymentMethod', 'invoiceDeliveryDate', 'transactionId', 'index', 'modificationIndex', 'insDate', 'completenessIndicator'])
    invoice_data = []

    logger.info(f"Processing {len(invoices)} invoices from XML response")
    for invoice in invoices:
        try:
            # Helper function to safely get XML field value
            def get_xml_field(element, tag_name, default_value=""):
                elements = element.getElementsByTagName(tag_name)
                if not elements:
                    elements = element.getElementsByTagName(f'ns2:{tag_name}')
                if elements and elements[0].firstChild:
                    return elements[0].firstChild.data
                return default_value
            
            def get_xml_field_float(element, tag_name, default_value=0.0):
                elements = element.getElementsByTagName(tag_name)
                if not elements:
                    elements = element.getElementsByTagName(f'ns2:{tag_name}')
                if elements and elements[0].firstChild:
                    try:
                        return float(elements[0].firstChild.data)
                    except (ValueError, TypeError):
                        return default_value
                return default_value
            
            def get_xml_field_int(element, tag_name, default_value=0):
                elements = element.getElementsByTagName(tag_name)
                if not elements:
                    elements = element.getElementsByTagName(f'ns2:{tag_name}')
                if elements and elements[0].firstChild:
                    try:
                        return int(elements[0].firstChild.data)
                    except (ValueError, TypeError):
                        return default_value
                return default_value
            
            def get_xml_field_bool(element, tag_name, default_value=False):
                elements = element.getElementsByTagName(tag_name)
                if not elements:
                    elements = element.getElementsByTagName(f'ns2:{tag_name}')
                if elements and elements[0].firstChild:
                    try:
                        return elements[0].firstChild.data.lower() == 'true'
                    except (ValueError, TypeError):
                        return default_value
                return default_value
            
            original_invoice_number = get_xml_field(invoice, 'originalInvoiceNumber')
            invoice_id = get_xml_field(invoice, 'invoiceNumber')

            invoice_data.append({
                'invoiceId': invoice_id,
                'invoiceOperation': get_xml_field(invoice, 'invoiceOperation', 'UNKNOWN'),
                'issueDate': get_xml_field(invoice, 'issueDate'),
                'customerName': get_xml_field(invoice, 'customerName') or get_xml_field(invoice, 'supplierName'),  # Use supplier name for inbound
                'customerTaxNumber': get_xml_field(invoice, 'customerTaxNumber'),
                'dueDate': get_xml_field(invoice, 'paymentDate') or get_xml_field(invoice, 'invoiceDeliveryDate', 'N/A'),  # Fallback to delivery date
                'invoiceCurrency': get_xml_field(invoice, 'currency', 'HUF'),
                'netAmount': get_xml_field_float(invoice, 'netAmount'),
                'netAmountHuf': get_xml_field_float(invoice, 'netAmountHuf'),
                'vatAmount': get_xml_field_float(invoice, 'vatAmount'),
                'vatAmountHuf': get_xml_field_float(invoice, 'vatAmountHuf'),
                'originalInvoiceNumber': original_invoice_number,
                'supplierName': get_xml_field(invoice, 'supplierName'),  # Add supplier info for inbound invoices
                'supplierTaxNumber': get_xml_field(invoice, 'supplierTaxNumber'),
                'invoiceCategory': get_xml_field(invoice, 'invoiceCategory'),
                'invoiceAppearance': get_xml_field(invoice, 'invoiceAppearance'),
                # Additional fields from pagination documentation
                'paymentMethod': get_xml_field(invoice, 'paymentMethod'),
                'invoiceDeliveryDate': get_xml_field(invoice, 'invoiceDeliveryDate'),
                'transactionId': get_xml_field(invoice, 'transactionId'),
                'index': get_xml_field_int(invoice, 'index'),
                'modificationIndex': get_xml_field_int(invoice, 'modificationIndex'),
                'insDate': get_xml_field(invoice, 'insDate'),
                'completenessIndicator': get_xml_field_bool(invoice, 'completenessIndicator')
            })
            
        except Exception as e:
            logger.exception(f"Error processing invoice: {e} Invoice XML: {invoice.toxml()}")
            continue

    df = pd.DataFrame(invoice_data)
    
    # Sort by issue date (newest first)
    return sort_invoices_by_date(df)

def generate_password_hash(password):  
    # SHA-512 hash előállítása  
    hash_object = hashlib.sha512(password.encode('utf-8'))  
    # A hash értékének nagybetűs hexadecimális formátuma  
    password_hash = hash_object.hexdigest().upper()  
    return password_hash  

def generate_custom_id(length=30):
    characters = string.ascii_letters + string.digits + '_'
    return ''.join(random.choice(characters) for _ in range(length))

def calculate_request_signature(request_id, timestamp, signer_key):  
    # Parciális hitelesítés előállítása  
    timestamp_str = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y%m%d%H%M%S')  
    partial_auth = f"{request_id}{timestamp_str}{signer_key}"  
  
    # requestSignature előállítása  
    hash_object = hashlib.sha3_512(partial_auth.encode('utf-8'))  
    request_signature = hash_object.hexdigest().upper()  
      
    return request_signature

def split_date_range(start_date: str, end_date: str, max_days: int = 35):
    """Split a date range into chunks of maximum days."""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    date_ranges = []
    current_start = start
    
    while current_start <= end:
        current_end = min(current_start + timedelta(days=max_days - 1), end)
        date_ranges.append((
            current_start.strftime('%Y-%m-%d'),
            current_end.strftime('%Y-%m-%d')
        ))
        current_start = current_end + timedelta(days=1)
    
    return date_ranges

def sort_invoices_by_date(df):
    """Sort DataFrame by issue date (newest first)."""
    if df.empty or 'issueDate' not in df.columns:
        return df
    
    try:
        # Convert issueDate to datetime for proper sorting
        df_copy = df.copy()
        df_copy['issueDate'] = pd.to_datetime(df_copy['issueDate'])
        df_sorted = df_copy.sort_values('issueDate', ascending=False)
        # Convert back to string format for display
        df_sorted['issueDate'] = df_sorted['issueDate'].dt.strftime('%Y-%m-%d')
        return df_sorted.reset_index(drop=True)
    except Exception as e:
        logger.warning(f"Could not sort by issue date: {e}")
        return df

def get_single_range_invoices(date_from: str, date_to: str, login: str, password: str, signer_key: str, tax_number: str = "32703094", invoice_direction: str = "OUTBOUND"):
    """Get invoices for a single date range (max 35 days) with pagination support."""
    
    pwd_hash = generate_password_hash(password)
    all_invoices = []
    current_page = 1
    total_pages = 1
    
    while current_page <= total_pages:
        logger.info(f"Querying NAV API for page {current_page} of {total_pages} for date range {date_from} to {date_to}")
        request_id = generate_custom_id()
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-4]+'Z'
        signature = calculate_request_signature(request_id, timestamp, signer_key)

        template = f"""<?xml version="1.0" encoding="UTF-8"?>
	<QueryInvoiceDigestRequest xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns="http://schemas.nav.gov.hu/OSA/3.0/api">
		<common:header>
			<common:requestId>{request_id}</common:requestId>
			<common:timestamp>{timestamp}</common:timestamp>
			<common:requestVersion>3.0</common:requestVersion>
			<common:headerVersion>1.0</common:headerVersion>
		</common:header>
		<common:user>
			<common:login>{login}</common:login>
			<common:passwordHash cryptoType="SHA-512">{pwd_hash}</common:passwordHash>
			<common:taxNumber>{tax_number}</common:taxNumber>
			<common:requestSignature cryptoType="SHA3-512">{signature}</common:requestSignature>
			<!--<signKey>ac-ac3a-7f661bff7d342N43CYX4U9FG</signKey>-->
		</common:user>
		<software>
			<softwareId>123456789123456789</softwareId>
			<softwareName>string</softwareName>
			<softwareOperation>LOCAL_SOFTWARE</softwareOperation>
			<softwareMainVersion>string</softwareMainVersion>
			<softwareDevName>string</softwareDevName>
			<softwareDevContact>string</softwareDevContact>
			<softwareDevCountryCode>HU</softwareDevCountryCode>
			<softwareDevTaxNumber>string</softwareDevTaxNumber>
		</software>
		<page>{current_page}</page>
		<invoiceDirection>{invoice_direction}</invoiceDirection>
		<invoiceQueryParams>
			<mandatoryQueryParams>
				<invoiceIssueDate>
					<dateFrom>{date_from}</dateFrom>
					<dateTo>{date_to}</dateTo>
				</invoiceIssueDate>
			</mandatoryQueryParams>
		</invoiceQueryParams>
	</QueryInvoiceDigestRequest>
"""

        try:
            response = make_nav_api_request("POST", ONLINE_SZAMLA_URL + 'queryInvoiceDigest', HEADERS, template)
            
            # Check if HTTP request failed
            if response.status_code != 200:
                error_msg = f"HTTP {response.status_code}: {response.reason} | {response.text}"
                logger.error(f"HTTP Error: {error_msg}")
                raise Exception(f"NAV API HTTP hiba: {error_msg}")
            
            # Check for XML errors first
            try:
                dom = xml.dom.minidom.parseString(response.text)
            except xml.parsers.expat.ExpatError as e:
                logger.error(f"XML parsing error: {e}")
                logger.error(f"Response text: {response.text}")
                raise Exception(f"Érvénytelen XML válasz a NAV API-tól: {e}")
            
            # Check if response contains an error
            error_elements = dom.getElementsByTagName('errorCode')
            if not error_elements:
                error_elements = dom.getElementsByTagName('ns2:errorCode')
            if error_elements:
                error_code = error_elements[0].firstChild.data if error_elements[0].firstChild else "UNKNOWN"
                message_elements = dom.getElementsByTagName('message')
                if not message_elements:
                    message_elements = dom.getElementsByTagName('ns2:message')
                error_message = message_elements[0].firstChild.data if message_elements and message_elements[0].firstChild else "Ismeretlen hiba"
                logger.error(f"NAV API Error: {error_code} - {error_message}")
                raise Exception(f"NAV API hiba ({error_code}): {error_message}")
            
            # Check for general error response
            func_code_elements = dom.getElementsByTagName('funcCode')
            if not func_code_elements:
                func_code_elements = dom.getElementsByTagName('ns2:funcCode')
            if func_code_elements:
                func_code = func_code_elements[0].firstChild.data if func_code_elements[0].firstChild else ""
                if func_code == "ERROR":
                    # Look for any error message
                    message_elements = dom.getElementsByTagName('message')
                    if not message_elements:
                        message_elements = dom.getElementsByTagName('ns2:message')
                    if message_elements and message_elements[0].firstChild:
                        error_message = message_elements[0].firstChild.data
                        logger.error(f"NAV API funcCode ERROR: {error_message}")
                        raise Exception(f"NAV API hiba: {error_message}")
                    else:
                        logger.error("NAV API returned ERROR funcCode but no message")
                        raise Exception("NAV API hiba: Ismeretlen hiba történt")
            
            # Extract pagination info from response
            if current_page == 1:
                # On first page, get total pages info
                available_page_elements = dom.getElementsByTagName('availablePage')
                if not available_page_elements:
                    # Try with namespace prefix in case it's wrapped differently
                    available_page_elements = dom.getElementsByTagName('ns2:availablePage')
                if available_page_elements and available_page_elements[0].firstChild:
                    total_pages = int(available_page_elements[0].firstChild.data)
                    logger.info(f"NAV API: {total_pages} elérhető oldal")
                else:
                    total_pages = 1
                    logger.info("NAV API: Nincs elérhető oldal, csak az első oldalt kérjük le")
            
            # Extract current page info for verification
            current_page_elements = dom.getElementsByTagName('currentPage')
            if not current_page_elements:
                # Try with namespace prefix in case it's wrapped differently
                current_page_elements = dom.getElementsByTagName('ns2:currentPage')
            if current_page_elements and current_page_elements[0].firstChild:
                actual_current_page = int(current_page_elements[0].firstChild.data)
            # Process invoices from current page
            page_invoices = create_df_from_xml(dom)
            if not page_invoices.empty:
                all_invoices.append(page_invoices)
            
            # Move to next page
            current_page += 1
            
        except Exception as e:
            # Check if it's a connection-related error that couldn't be retried
            if any(error_type in str(e).lower() for error_type in ['connection', 'timeout', 'network', 'resolve']):
                logger.error(f"Network error after retries: {e}")
                raise Exception(f"Hálózati hiba a NAV API-hoz: {str(e)} - Ellenőrizze az internetkapcsolatot és próbálja meg később")
            
            # Re-raise our custom exceptions
            if "NAV API hiba" in str(e) or "Érvénytelen XML" in str(e) or "HTTP" in str(e):
                raise
            
            # Handle any other unexpected errors
            logger.exception(f"Unexpected error querying NAV API: {e}")
            logger.error(f"Unexpected error querying NAV API: {e}")
            raise Exception(f"Váratlan hiba a NAV lekérdezés során: {str(e)}")
    
    # Combine all pages into a single DataFrame
    if all_invoices:
        df_invoices = pd.concat(all_invoices, ignore_index=True)
        df_invoices = sort_invoices_by_date(df_invoices)
        return df_invoices
    else:
        return pd.DataFrame(columns=['invoiceId', 'invoiceOperation', 'issueDate', 'customerName', 'customerTaxNumber', 'dueDate', 'invoiceCurrency', 'netAmount', 'netAmountHuf', 'vatAmount', 'vatAmountHuf', 'originalInvoiceNumber', 'supplierName', 'supplierTaxNumber', 'invoiceCategory', 'invoiceAppearance', 'paymentMethod', 'invoiceDeliveryDate', 'transactionId', 'index', 'modificationIndex', 'insDate', 'completenessIndicator'])

def get_invoices_from_nav(date_from: str, date_to: str, login: str, password: str, signer_key: str, tax_number: str = "32703094", invoice_direction: str = "OUTBOUND"):
    """Get invoices from NAV, automatically splitting date ranges if necessary."""
    # Calculate the date difference
    start_date = datetime.strptime(date_from, '%Y-%m-%d')
    end_date = datetime.strptime(date_to, '%Y-%m-%d')
    date_diff = (end_date - start_date).days + 1
    
    # Handle "BOTH" direction by making separate calls for OUTBOUND and INBOUND
    if invoice_direction == "BOTH":
        
        try:
            # Get OUTBOUND invoices
            df_outbound = get_invoices_from_nav(date_from, date_to, login, password, signer_key, tax_number, "OUTBOUND")
            
            # Get INBOUND invoices
            df_inbound = get_invoices_from_nav(date_from, date_to, login, password, signer_key, tax_number, "INBOUND")
            
            # Combine both results
            if not df_outbound.empty and not df_inbound.empty:
                df_invoices = pd.concat([df_outbound, df_inbound], ignore_index=True)
                df_invoices = sort_invoices_by_date(df_invoices)
            elif not df_outbound.empty:
                df_invoices = df_outbound
            elif not df_inbound.empty:
                df_invoices = df_inbound
            else:
                df_invoices = pd.DataFrame(columns=['invoiceId', 'invoiceOperation', 'issueDate', 'customerName', 'dueDate', 'invoiceCurrency', 'netAmount', 'netAmountHuf', 'vatAmount', 'vatAmountHuf', 'originalInvoiceNumber', 'supplierName', 'supplierTaxNumber', 'invoiceCategory', 'invoiceAppearance', 'paymentMethod', 'invoiceDeliveryDate', 'transactionId', 'index', 'modificationIndex', 'insDate', 'completenessIndicator'])
            
            return df_invoices
            
        except Exception as e:
            logger.error(f"Error fetching BOTH direction invoices: {e}")
            raise
    
    # Handle single direction (OUTBOUND or INBOUND)
    if date_diff <= 35:
        # Single request
        df_invoices = get_single_range_invoices(date_from, date_to, login, password, signer_key, tax_number, invoice_direction)
    else:
        # Split into multiple requests
        date_ranges = split_date_range(date_from, date_to)
        
        all_invoices = []
        for i, (range_start, range_end) in enumerate(date_ranges, 1):
            try:
                chunk_invoices = get_single_range_invoices(range_start, range_end, login, password, signer_key, tax_number, invoice_direction)
                if not chunk_invoices.empty:
                    all_invoices.append(chunk_invoices)
            except Exception as e:
                # Log the error but include chunk information
                logger.error(f"Error in chunk {i}/{len(date_ranges)} ({range_start} to {range_end}): {e}")
                raise Exception(f"Hiba a(z) {i}. részletben ({range_start} - {range_end}): {str(e)}")
        
        # Combine all DataFrames
        if all_invoices:
            df_invoices = pd.concat(all_invoices, ignore_index=True)
            df_invoices = sort_invoices_by_date(df_invoices)
        else:
            df_invoices = pd.DataFrame(columns=['invoiceId', 'invoiceOperation', 'issueDate', 'customerName', 'dueDate', 'invoiceCurrency', 'netAmount', 'netAmountHuf', 'vatAmount', 'vatAmountHuf', 'originalInvoiceNumber', 'supplierName', 'supplierTaxNumber', 'invoiceCategory', 'invoiceAppearance', 'paymentMethod', 'invoiceDeliveryDate', 'transactionId', 'index', 'modificationIndex', 'insDate', 'completenessIndicator'])
    
    # Add metadata columns
    if not df_invoices.empty:
        df_invoices['account'] = login
        df_invoices['name'] = df_invoices['customerName'] + ' | ' + df_invoices['invoiceId']
        df_invoices['direction'] = invoice_direction
    
    logger.info(f"Final result: {len(df_invoices)} invoices returned for direction {invoice_direction}")
    return df_invoices


def get_invoice_detail(invoice_number: str, invoice_direction: str, login: str, password: str, signer_key: str, tax_number: str = "32703094", supplier_tax_number: str = None, batch_index: int = None, save_xml: bool = False, xml_storage_path: str = None):
    """Get detailed invoice data from NAV using queryInvoiceData endpoint.
    
    Args:
        invoice_number: Invoice number to retrieve
        invoice_direction: Direction of the invoice (OUTBOUND/INBOUND)
        login: NAV login
        password: NAV password
        signer_key: NAV signer key
        tax_number: Tax number
        supplier_tax_number: Optional supplier tax number
        batch_index: Optional batch index
        save_xml: Whether to save the XML file to local storage
        xml_storage_path: Path where to save XML files (defaults to ./invoice_xmls)
        
    Returns:
        xml.dom.minidom.Document: Parsed invoice XML document
    """
    # check if the file is already downloaded
    if save_xml:
        if not os.path.exists(xml_storage_path):
            os.makedirs(xml_storage_path)
        xml_file_path = os.path.join(xml_storage_path, f"{invoice_number}.xml")
        if os.path.exists(xml_file_path):
            logger.info(f"XML file for invoice {invoice_number} already exists at {xml_file_path}. Skipping download.")
            try:
                with open(xml_file_path, 'r', encoding='utf-8') as f:
                    xml_content = f.read()
                return xml.dom.minidom.parseString(xml_content)
            except Exception as e:
                logger.error(f"Error reading existing XML file: {e}")
                raise

    pwd_hash = generate_password_hash(password)
    request_id = generate_custom_id()
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-4]+'Z'
    signature = calculate_request_signature(request_id, timestamp, signer_key)
    
    # Build the request template
    template = f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDataRequest xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common" xmlns="http://schemas.nav.gov.hu/OSA/3.0/api">
    <common:header>
        <common:requestId>{request_id}</common:requestId>
        <common:timestamp>{timestamp}</common:timestamp>
        <common:requestVersion>3.0</common:requestVersion>
        <common:headerVersion>1.0</common:headerVersion>
    </common:header>
    <common:user>
        <common:login>{login}</common:login>
        <common:passwordHash cryptoType="SHA-512">{pwd_hash}</common:passwordHash>
        <common:taxNumber>{tax_number}</common:taxNumber>
        <common:requestSignature cryptoType="SHA3-512">{signature}</common:requestSignature>
    </common:user>
    <software>
        <softwareId>123456789123456789</softwareId>
        <softwareName>string</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>string</softwareMainVersion>
        <softwareDevName>string</softwareDevName>
        <softwareDevContact>string</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>string</softwareDevTaxNumber>
    </software>
    <invoiceNumberQuery>
        <invoiceNumber>{invoice_number}</invoiceNumber>
        <invoiceDirection>{invoice_direction}</invoiceDirection>"""
    
    # Add optional parameters if provided
    if supplier_tax_number:
        template += f"""
        <supplierTaxNumber>{supplier_tax_number}</supplierTaxNumber>"""
    
    if batch_index is not None:
        template += f"""
        <batchIndex>{batch_index}</batchIndex>"""
    
    template += """
    </invoiceNumberQuery>
</QueryInvoiceDataRequest>"""
    
    try:
        response = make_nav_api_request("POST", ONLINE_SZAMLA_URL + 'queryInvoiceData', HEADERS, template)
        if response.status_code != 200:
            logger.error(f"NAV API detail response error: {response.text}")
            error_msg = f"HTTP {response.status_code}: {response.reason}"
            logger.error(f"HTTP Error: {error_msg}")
            raise Exception(f"NAV API HTTP hiba: {error_msg}")
        
        # Parse XML response
        try:
            dom = xml.dom.minidom.parseString(response.text)
        except xml.parsers.expat.ExpatError as e:
            logger.error(f"XML parsing error: {e}")
            raise Exception(f"Érvénytelen XML válasz a NAV API-tól: {e}")
        
        # Check for errors
        error_elements = dom.getElementsByTagName('errorCode')
        if not error_elements:
            error_elements = dom.getElementsByTagName('ns2:errorCode')
        if error_elements:
            error_code = error_elements[0].firstChild.data if error_elements[0].firstChild else "UNKNOWN"
            message_elements = dom.getElementsByTagName('message')
            if not message_elements:
                message_elements = dom.getElementsByTagName('ns2:message')
            error_message = message_elements[0].firstChild.data if message_elements and message_elements[0].firstChild else "Ismeretlen hiba"
            logger.error(f"NAV API Error: {error_code} - {error_message}")
            raise Exception(f"NAV API hiba ({error_code}): {error_message}")
        
        # Extract invoice data
        invoice_data_elements = dom.getElementsByTagName('invoiceData')
        if not invoice_data_elements:
            # Try with namespace prefix in case it's wrapped differently
            invoice_data_elements = dom.getElementsByTagName('ns2:invoiceData')
        
        if not invoice_data_elements or not invoice_data_elements[0].firstChild:
            logger.warning(f"No invoice data found for {invoice_number}")
            return None
        
        # Decode base64 data
        encoded_data = invoice_data_elements[0].firstChild.data
        decoded_data = base64.b64decode(encoded_data)
        
        # Check if data is compressed
        compressed_elements = dom.getElementsByTagName('compressedContentIndicator')
        if not compressed_elements:
            # Try with namespace prefix
            compressed_elements = dom.getElementsByTagName('ns2:compressedContentIndicator')
        
        is_compressed = False
        if compressed_elements and compressed_elements[0].firstChild:
            is_compressed = compressed_elements[0].firstChild.data.lower() == 'true'
        
        # Decompress if necessary
        if is_compressed:
            try:
                decoded_data = gzip.decompress(decoded_data)
            except Exception as e:
                logger.error(f"Error decompressing data: {e}")
                raise Exception(f"Hiba az adatok kicsomagolásában: {e}")
        
        # Parse the invoice XML
        try:
            invoice_xml = xml.dom.minidom.parseString(decoded_data.decode('utf-8'))
            
            # Save XML to local file storage if requested
            if save_xml:
                try:
                    # Set default storage path if not provided
                    if xml_storage_path is None:
                        xml_storage_path = './invoice_xmls'
                    
                    # Create directory if it doesn't exist
                    os.makedirs(xml_storage_path, exist_ok=True)
                    
                    # Sanitize invoice number for filename (remove invalid characters)
                    safe_invoice_number = "".join(c for c in invoice_number if c.isalnum() or c in ('-', '_', '.')).rstrip()
                    
                    # Create filename with invoice number
                    xml_filename = f"{safe_invoice_number}.xml"
                    xml_filepath = os.path.join(xml_storage_path, xml_filename)
                    
                    # Save the pretty-printed XML to file
                    with open(xml_filepath, 'w', encoding='utf-8') as xml_file:
                        # Use toprettyxml for better formatting
                        pretty_xml = invoice_xml.toprettyxml(indent='  ', encoding=None)
                        xml_file.write(pretty_xml)
                    
                except Exception as save_error:
                    logger.warning(f"Failed to save XML for invoice {invoice_number}: {save_error}")
                    # Don't fail the whole operation if XML saving fails
            
            return invoice_xml
        except Exception as e:
            logger.exception(f"Error parsing invoice XML: {e}")
            raise Exception(f"Hiba a számla XML feldolgozásában: {e}")
    
    except Exception as e:
        # Check if it's a connection-related error that couldn't be retried
        if any(error_type in str(e).lower() for error_type in ['connection', 'timeout', 'network', 'resolve']):
            logger.error(f"Network error after retries: {e}")
            raise Exception(f"Hálózati hiba a NAV API-hoz: {str(e)} - Ellenőrizze az internetkapcsolatot és próbálja meg később")
        
        if "NAV API hiba" in str(e) or "Érvénytelen XML" in str(e) or "HTTP" in str(e):
            raise
        logger.exception(f"Unexpected error querying invoice detail: {e}")
        raise Exception(f"Váratlan hiba a számla részletek lekérdezésében: {str(e)}")


def extract_invoice_lines_from_xml(invoice_xml, invoice_number: str):
    """Extract invoice line items from detailed invoice XML."""
    
    try:
        lines = []
        
        # Look for invoiceLines container first
        invoice_lines_container = invoice_xml.getElementsByTagName('invoiceLines')
        if not invoice_lines_container:
            # Try with namespace prefix in case it's wrapped differently
            invoice_lines_container = invoice_xml.getElementsByTagName('ns2:invoiceLines')
        if not invoice_lines_container:
            logger.warning(f"No invoiceLines container found in invoice {invoice_number}")
            return pd.DataFrame()
        
        # Get all line elements within invoiceLines
        line_elements = invoice_lines_container[0].getElementsByTagName('line')
        if not line_elements:
            # Try with namespace prefix in case it's wrapped differently
            line_elements = invoice_lines_container[0].getElementsByTagName('ns2:line')
        
        if not line_elements:
            logger.warning(f"No line elements found in invoice {invoice_number}")
            return pd.DataFrame()
        
        logger.info(f"Found {len(line_elements)} line items in invoice {invoice_number}")
        
        for line_element in line_elements:
            try:
                # Helper function to safely extract text from XML elements
                def get_line_field(element, tag_name, default_value=""):
                    elements = element.getElementsByTagName(tag_name)
                    if not elements:
                        elements = element.getElementsByTagName(f'ns2:{tag_name}')
                    if elements and elements[0].firstChild:
                        return elements[0].firstChild.data.strip()
                    return default_value
                
                def get_line_field_float(element, tag_name, default_value=0.0):
                    try:
                        value = get_line_field(element, tag_name)
                        return float(value) if value else default_value
                    except (ValueError, TypeError):
                        return default_value
                
                def get_line_field_int(element, tag_name, default_value=0):
                    try:
                        value = get_line_field(element, tag_name)
                        return int(value) if value else default_value
                    except (ValueError, TypeError):
                        return default_value
                
                # Extract VAT rate (can be percentage or out of scope)
                vat_rate = 0.0
                vat_rate_description = ""
                
                # Try to get VAT percentage
                vat_percentage = get_line_field_float(line_element, 'vatPercentage')
                if vat_percentage > 0:
                    vat_rate = vat_percentage * 100  # Convert to percentage
                    vat_rate_description = f"{vat_rate:.1f}%"
                else:
                    # Check for VAT out of scope
                    vat_case = get_line_field(line_element, 'case')
                    vat_reason = get_line_field(line_element, 'reason')
                    if vat_case or vat_reason:
                        vat_rate_description = f"{vat_case} - {vat_reason}" if vat_case and vat_reason else (vat_case or vat_reason)
                    else:
                        # If no VAT data found, check if it's an advance payment or other special case
                        advance_indicator = get_line_field(line_element, 'advanceIndicator')
                        if advance_indicator == 'true':
                            vat_rate_description = "Előleg"
                        else:
                            vat_rate_description = "Nincs megadva"
                
                # Extract line item data based on the actual XML structure
                line_data = {
                    'invoiceNumber': invoice_number,
                    'customerTaxNumber': '',  # Will be filled later
                    'customerName': '',  # Will be filled later
                    'supplierTaxNumber': '',  # Will be filled later
                    'supplierName': '',  # Will be filled later
                    'lineNumber': get_line_field_int(line_element, 'lineNumber', len(lines) + 1),
                    'lineModificationReference': get_line_field(line_element, 'lineModificationReference'),
                    'modificationType': get_line_field(line_element, 'modificationType'),
                    'lineDescription': get_line_field(line_element, 'lineDescription'),
                    'quantity': get_line_field_float(line_element, 'quantity', 1.0),
                    'unitOfMeasure': get_line_field(line_element, 'unitOfMeasure'),
                    'unitOfMeasureOwn': get_line_field(line_element, 'unitOfMeasureOwn'),
                    'unitPrice': get_line_field_float(line_element, 'unitPrice'),
                    'unitPriceHUF': get_line_field_float(line_element, 'unitPriceHUF'),
                    'lineNetAmount': get_line_field_float(line_element, 'lineNetAmount'),
                    'lineNetAmountHUF': get_line_field_float(line_element, 'lineNetAmountHUF'),
                    'lineVatRate': vat_rate,
                    'lineVatRateDescription': vat_rate_description,
                    'vatExemptionIndicator': get_line_field(line_element, 'vatExemptionIndicator'),
                    'vatExemptionCase': get_line_field(line_element, 'vatExemptionCase'),
                    'vatExemptionDescription': get_line_field(line_element, 'vatExemptionDescription'),
                    'vatOutOfScopeIndicator': get_line_field(line_element, 'vatOutOfScopeIndicator'),
                    'vatOutOfScopeCase': get_line_field(line_element, 'vatOutOfScopeCase'),
                    'vatOutOfScopeDescription': get_line_field(line_element, 'vatOutOfScopeDescription'),
                    'taxBaseAndTaxDifferenceCase': get_line_field(line_element, 'taxBaseAndTaxDifferenceCase'),
                    'differentTaxBaseAndTaxContent': get_line_field(line_element, 'differentTaxBaseAndTaxContent'),
                    'domesticReverseChargeIndicator': get_line_field(line_element, 'domesticReverseChargeIndicator'),
                    'transferredTaxMarginSchemeIndicator': get_line_field(line_element, 'transferredTaxMarginSchemeIndicator'),
                    'nonTransferredTaxMarginSchemeIndicator': get_line_field(line_element, 'nonTransferredTaxMarginSchemeIndicator'),
                    'marginSchemeIndicator': get_line_field(line_element, 'marginSchemeIndicator'),
                    'lineVatAmount': get_line_field_float(line_element, 'lineVatAmount'),
                    'lineVatAmountHUF': get_line_field_float(line_element, 'lineVatAmountHUF'),
                    'lineGrossAmountNormal': get_line_field_float(line_element, 'lineGrossAmountNormal'),
                    'lineGrossAmountNormalHUF': get_line_field_float(line_element, 'lineGrossAmountNormalHUF'),
                    'vatContent': get_line_field(line_element, 'vatContent'),
                    'advanceIndicator': get_line_field(line_element, 'advanceIndicator'),
                    'lineExchangeRate': get_line_field_float(line_element, 'lineExchangeRate', 1.0),
                    'lineDeliveryDate': get_line_field(line_element, 'lineDeliveryDate'),
                    'noVatCharged17': get_line_field(line_element, 'noVatCharged17'),
                    
                    # Additional fields that might be present
                    'lineExpressionIndicator': get_line_field(line_element, 'lineExpressionIndicator'),
                    'productCode': get_line_field(line_element, 'productCode') or get_line_field(line_element, 'productCodeValue'),
                    'aggregateInvoiceLineFlag': get_line_field(line_element, 'aggregateInvoiceLineFlag'),
                    'productCodeCategory': get_line_field(line_element, 'productCodeCategory'),
                    'productCodeValue': get_line_field(line_element, 'productCodeValue'),
                    'productCodeOwnValue': get_line_field(line_element, 'productCodeOwnValue'),
                    'advancePaymentData': get_line_field(line_element, 'advancePaymentData'),
                    'referencesToOtherLines': get_line_field(line_element, 'referencesToOtherLines'),
                    'intermediatedService': get_line_field(line_element, 'intermediatedService'),
                    'depositIndicator': get_line_field(line_element, 'depositIndicator'),
                    'obligatedForProductFee': get_line_field(line_element, 'obligatedForProductFee'),
                    'GPCExcise': get_line_field(line_element, 'GPCExcise'),
                    'dieselOilPurchase': get_line_field(line_element, 'dieselOilPurchase'),
                    'netaDeclaration': get_line_field(line_element, 'netaDeclaration'),
                    'productFeeClause': get_line_field(line_element, 'productFeeClause'),
                    'lineDiscountData': get_line_field(line_element, 'lineDiscountData'),
                    'conventionalLineInfo': get_line_field(line_element, 'conventionalLineInfo'),
                    'additionalLineData': get_line_field(line_element, 'additionalLineData')
                }
                
                lines.append(line_data)
                
            except Exception as e:
                logger.error(f"Error processing line item {len(lines) + 1} in invoice {invoice_number}: {e}")
                continue
        
        if lines:
            df_lines = pd.DataFrame(lines)
            return df_lines
        else:
            return pd.DataFrame()
    
    except Exception as e:
        logger.error(f"Error extracting line items from invoice {invoice_number}: {e}")
        return pd.DataFrame()


def get_invoice_field(xml_doc, tag_name, default_value=""):
    """
    Get invoice field value with namespace handling.
    Tries multiple namespace prefixes to find the element.
    """
    for prefix in ['', 'ns2:']:
        full_tag_name = f'{prefix}{tag_name}' if prefix else tag_name
        elements = xml_doc.getElementsByTagName(full_tag_name)
        if elements and elements[0].firstChild:
            return elements[0].firstChild.data.strip()
    return default_value

def get_invoice_field_float(xml_doc, tag_name, default_value=0.0):
    try:
        value = get_invoice_field(xml_doc, tag_name)
        return float(value) if value else default_value
    except (ValueError, TypeError):
        return default_value


def get_nested_element_value(xml_doc, xml_path):
    """
    Extract value from XML using a dot-separated path (e.g., 'invoiceMain.invoice.invoiceHead.supplierInfo.supplierName')
    Handles namespace variations by trying multiple prefixes for each element.
    """
    return _extract_with_path_variants(xml_doc, xml_path)




def _extract_with_path_variants(xml_doc, xml_path):
    """Helper function to extract value trying different namespace variants."""
    elements = [xml_doc]
    
    # Split the path and traverse through XML structure
    path_parts = xml_path.split('.')
    
    for part in path_parts:
        new_elements = []
        for element in elements:
            # Try multiple namespace variations for each element
            for prefix in ['', 'ns2:']:
                tag_name = f'{prefix}{part}' if prefix else part
                found = element.getElementsByTagName(tag_name)
                if found:
                    new_elements.extend(found)
                    break  # Found with this prefix, no need to try others
        
        if not new_elements:
            return None
        elements = new_elements
    
    # Get the first element's text content
    if elements and elements[0].firstChild:
        return elements[0].firstChild.data.strip()
    return None


def create_detailed_invoice_from_mapping(invoice_xml, invoice_number):
    """
    Create a detailed invoice dictionary and extract line items using mapping constants from nav_constans.
    
    This function processes the main invoice-level mapping for header data and the line_mapping 
    for individual line items. Each invoice line is processed separately and returned as a list.
    
    Args:
        invoice_xml: Parsed XML document
        invoice_number: Invoice number for identification
        
    Returns:
        tuple: (detailed_invoice_dict, lines_list) where:
            - detailed_invoice_dict: Dictionary with invoice header data from main mapping
            - lines_list: List of dictionaries, each representing one invoice line from line_mapping
    """
    detailed_invoice = {}
    
    # Start with basic invoice identification
    detailed_invoice['invoiceId'] = invoice_number
    
    def process_field_mapping(field_mapping, xml_context=None):
        """Helper function to process a single field mapping with multiple XML path support."""
        field_name = field_mapping['field_name']
        field_type = field_mapping['type']
        default_value = field_mapping['default']
        
        # Special case: invoiceNumber should use the function parameter
        if field_name == 'invoiceNumber':
            return field_name, invoice_number
        
        # Determine which XML to search in
        search_xml = xml_context if xml_context is not None else invoice_xml
        
        value = None
        
        # Handle multiple XML paths (new structure)
        if 'xml_paths' in field_mapping:
            xml_paths = field_mapping['xml_paths']
            for xml_path in xml_paths:
                # Adjust path if we're in line context
                if xml_context is not None and 'invoiceLines.line.' in xml_path:
                    line_path = xml_path.split('invoiceLines.line.')[-1]
                    xml_path = line_path
                elif xml_context is not None and xml_path.startswith('invoiceMain.invoice.invoiceHead'):
                    # This is invoice-level data, search in main invoice XML
                    search_xml = invoice_xml
                
                # Try to extract value from this path
                if '.' in xml_path:
                    value = get_nested_element_value(search_xml, xml_path)
                else:
                    value = get_invoice_field(search_xml, xml_path)
                
                # If we found a value, break out of the loop
                if value is not None and value != '':
                    break
        
        # If no value found in xml_paths, try xml_path_combiner
        if (value is None or value == '') and 'xml_path_combiner' in field_mapping:
            xml_paths = field_mapping['xml_path_combiner']
            parts = []
            for xml_path in xml_paths:
                # Adjust path if we're in line context
                if xml_context is not None and 'invoiceLines.line.' in xml_path:
                    line_path = xml_path.split('invoiceLines.line.')[-1]
                    xml_path = line_path
                elif xml_context is not None and xml_path.startswith('invoiceMain.invoice.invoiceHead'):
                    # This is invoice-level data, search in main invoice XML
                    search_xml = invoice_xml
                
                # Extract value from this path
                if '.' in xml_path:
                    part_value = get_nested_element_value(search_xml, xml_path)
                else:
                    part_value = get_invoice_field(search_xml, xml_path)
                
                if part_value:
                    parts.append(part_value)
            
            value = ' '.join(parts) if parts else None
        
        # Handle legacy single XML path (backward compatibility)
        elif 'xml_path' in field_mapping:
            xml_path = field_mapping['xml_path']
            # Adjust path if we're in line context
            if xml_context is not None and 'invoiceLines.line.' in xml_path:
                line_path = xml_path.split('invoiceLines.line.')[-1]
                xml_path = line_path
            elif xml_context is not None and xml_path.startswith('invoiceMain.invoice.invoiceHead'):
                # This is invoice-level data, search in main invoice XML
                search_xml = invoice_xml
            
            # Extract value from XML using the path
            if '.' in xml_path:
                value = get_nested_element_value(search_xml, xml_path)
            else:
                value = get_invoice_field(search_xml, xml_path)
        
        # Convert value to appropriate type
        if value is None or value == '':
            # Use default value only
            final_value = default_value
        else:
            if field_type == 'float':
                try:
                    final_value = float(value)
                except (ValueError, TypeError):
                    final_value = default_value
            elif field_type == 'int':
                try:
                    final_value = int(value)
                except (ValueError, TypeError):
                    final_value = default_value
            elif field_type == 'boolean':
                final_value = value.lower() in ('true', '1', 'yes', 'on') if isinstance(value, str) else bool(value)
            else:  # text type
                final_value = str(value)
        
        # Apply value replacement mapping if configured
        if 'replace_values' in field_mapping and field_mapping['replace_values']:
            replace_map = field_mapping['replace_values']
            # Check if the final_value exists in the replacement mapping
            if final_value in replace_map:
                final_value = replace_map[final_value]
        
        return field_name, final_value
    
    # Process main mapping fields (invoice-level data)
    for field_mapping in mapping:
        field_name, final_value = process_field_mapping(field_mapping)
        detailed_invoice[field_name] = final_value
    
    # Process line items using line_mapping
    line_items = []
    
    # Find invoice lines in XML
    invoice_lines_container = invoice_xml.getElementsByTagName('invoiceLines')
    if not invoice_lines_container:
        invoice_lines_container = invoice_xml.getElementsByTagName('ns2:invoiceLines')
    
    if invoice_lines_container:
        line_elements = invoice_lines_container[0].getElementsByTagName('line')
        if not line_elements:
            line_elements = invoice_lines_container[0].getElementsByTagName('ns2:line')
        
        # Process each line element
        for line_index, line_element in enumerate(line_elements, 1):
            line_item = {}
            
            # Process each field in line_mapping for this line
            for field_mapping in line_mapping:
                field_name, final_value = process_field_mapping(field_mapping, line_element)
                line_item[field_name] = final_value
            
            line_items.append(line_item)
    
    # Add additional computed fields that are not in the mapping
    detailed_invoice['supplierAddress'] = f"{detailed_invoice.get('supplierPostalCode', '')} {detailed_invoice.get('supplierCity', '')} {detailed_invoice.get('supplierAdditionalAddressDetail', '')}".strip()
    
    # Calculate line count
    detailed_invoice['lineCount'] = len(line_items)
    
    # Create name field for identification
    customer_name = detailed_invoice.get('customerName', '')
    detailed_invoice['name'] = f"{customer_name} | {invoice_number}"
    detailed_invoice = mapping_post_process(detailed_invoice)
    
    return detailed_invoice, line_items

def mapping_post_process(detailed_invoice: dict) -> dict:
    if detailed_invoice['originalInvoiceNumber'] == 'n/a':
        detailed_invoice['modificationDate'] = 'n/a'

    return detailed_invoice

def get_comprehensive_invoice_details(df_invoices, login: str, password: str, signer_key: str, tax_number: str = "32703094", save_xml: bool = False, xml_storage_path: str = None):
    """
    Get comprehensive invoice details with a single API call per invoice (sequential processing).
    
    This function uses the same processing logic as the threaded version but processes invoices sequentially.
    
    Args:
        df_invoices: DataFrame with basic invoice information
        login: NAV login
        password: NAV password
        signer_key: NAV signer key
        tax_number: Tax number
        save_xml: Whether to save XML files to local storage
        xml_storage_path: Path where to save XML files (defaults to ./invoice_xmls)
        
    Returns:
        tuple: (detailed_summary_df, lines_df)
    """
    
    detailed_invoices = []
    all_lines = []
    len_df = len(df_invoices)
    
    for index, invoice in df_invoices.iterrows():
        try:
            # Use the same processing logic as the threaded version
            args = (invoice.to_dict(), login, password, signer_key, tax_number, 
                    save_xml, xml_storage_path, index, len_df)
            detailed_invoice, df_lines = _process_single_invoice(args)
            
            if detailed_invoice:
                detailed_invoices.append(detailed_invoice)
            
            if df_lines is not None and not df_lines.empty:
                all_lines.append(df_lines)
                        
        except Exception as e:
            logger.exception(f"Error processing invoice {invoice['invoiceId']}: {e}")
            # Create fallback data on error
            basic_invoice = invoice.to_dict()
            basic_invoice.update({
                'customerVatStatus': '', 'customerVatCode': '', 'customerCountyCode': '',
                'customerCountryCode': '', 'customerPostalCode': '', 'customerCity': '',
                'customerAddressDetail': '', 'customerCommunityVatNumber': '', 'customerThirdStateTaxId': '',
                'supplierVatCode': '', 'supplierCountyCode': '', 'supplierCountryCode': '',
                'supplierPostalCode': '', 'supplierCity': '', 'supplierAddress': '',
                'exchangeRate': 1.0, 'grossAmount': 0.0, 'grossAmountHuf': 0.0,
                'paymentDate': basic_invoice.get('dueDate', ''), 'paymentDeadline': basic_invoice.get('dueDate', ''),
                'modificationDate': '', 'smallBusinessIndicator': '', 'cashAccountingIndicator': '',
                'lineCount': 0, 'name': f"{basic_invoice.get('customerName', '')} | {basic_invoice.get('invoiceId', '')}"
            })
            detailed_invoices.append(basic_invoice)
            continue
    
    # Return requested data
    df_detailed_summary = pd.DataFrame(detailed_invoices) if detailed_invoices else pd.DataFrame()
    df_all_lines = pd.concat(all_lines, ignore_index=True) if all_lines else pd.DataFrame()
    
    return df_detailed_summary, df_all_lines


def _process_single_invoice(args: Tuple) -> Tuple[Optional[dict], Optional[pd.DataFrame]]:
    """
    Process a single invoice for multithreaded execution using the mapping-based approach.
    
    Args:
        args: Tuple containing (invoice_row, login, password, signer_key, tax_number, 
                                save_xml, xml_storage_path, index, total)
    
    Returns:
        Tuple of (detailed_invoice_dict, lines_df)
    """
    (invoice, login, password, signer_key, tax_number, save_xml, xml_storage_path, index, total) = args

    try:
        logger.info(f"Processing invoice {index + 1}/{total}: {invoice['invoiceId']}")
        invoice_number = invoice['invoiceId']
        invoice_direction = invoice.get('direction', 'OUTBOUND')
        
        # Get detailed invoice data - SINGLE API CALL
        invoice_xml = get_invoice_detail(
            invoice_number=invoice_number,
            invoice_direction=invoice_direction,
            login=login,
            password=password,
            signer_key=signer_key,
            tax_number=tax_number,
            save_xml=save_xml,
            xml_storage_path=xml_storage_path
        )
        
        detailed_invoice = None
        df_lines = None
        if invoice_number in ['DBKP-313102']:
            logger.info(f"Invoice {invoice_number}: Xml content: {invoice_xml.toxml()}")
        if invoice_xml:
            # Use the refactored mapping-based approach
            detailed_invoice, line_items = create_detailed_invoice_from_mapping(invoice_xml, invoice_number)
            df_lines = pd.DataFrame(line_items)

        return detailed_invoice, df_lines
        
    except Exception as e:
        logger.exception(f"Error processing invoice {invoice['invoiceId']}: {e}")
        # Create fallback data on error
        detailed_invoice = None
        basic_invoice = invoice.copy() if isinstance(invoice, dict) else invoice.to_dict()
        basic_invoice.update({
            'customerVatStatus': '', 'customerVatCode': '', 'customerCountyCode': '',
            'customerCountryCode': '', 'customerPostalCode': '', 'customerCity': '',
            'customerAddressDetail': '', 'customerCommunityVatNumber': '', 'customerThirdStateTaxId': '',
            'supplierVatCode': '', 'supplierCountyCode': '', 'supplierCountryCode': '',
            'supplierPostalCode': '', 'supplierCity': '', 'supplierAddress': '',
            'exchangeRate': 1.0, 'grossAmount': 0.0, 'grossAmountHuf': 0.0,
            'paymentDate': basic_invoice.get('dueDate', ''), 'paymentDeadline': basic_invoice.get('dueDate', ''),
            'modificationDate': '', 'smallBusinessIndicator': '', 'cashAccountingIndicator': '',
            'lineCount': 0, 'name': f"{basic_invoice.get('customerName', '')} | {basic_invoice.get('invoiceId', '')}"
        })
        detailed_invoice = basic_invoice
        
        return detailed_invoice, None


def get_comprehensive_invoice_details_threaded(df_invoices, login: str, password: str, signer_key: str, tax_number: str = "32703094", save_xml: bool = False, xml_storage_path: str = None, max_workers: int = 8):
    """
    Get comprehensive invoice details with multithreading for improved performance.
    
    Args:
        df_invoices: DataFrame with basic invoice information
        login: NAV login
        password: NAV password
        signer_key: NAV signer key
        tax_number: Tax number
        extract_lines: Whether to extract line items
        extract_summary: Whether to extract detailed summary
        save_xml: Whether to save XML files to local storage
        xml_storage_path: Path where to save XML files (defaults to ./invoice_xmls)
        max_workers: Maximum number of threads (default: 5, recommended 3-8 for NAV API)
        
    Returns:
        tuple: (detailed_summary_df, lines_df) or individual DataFrames based on parameters
    """
    
    if df_invoices.empty:
        logger.info("No invoices to process")
        return pd.DataFrame(), pd.DataFrame()
    
    len_df = len(df_invoices)
    logger.info(f"Starting multithreaded processing of {len_df} invoices with {max_workers} threads")
    
    # Prepare arguments for each invoice
    invoice_args = []
    for index, invoice in df_invoices.iterrows():
        args = (invoice.to_dict(), login, password, signer_key, tax_number, 
                save_xml, xml_storage_path, index, len_df)
        invoice_args.append(args)
    
    detailed_invoices = []
    all_lines = []
    
    # Process invoices in parallel using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_invoice = {executor.submit(_process_single_invoice, args): args for args in invoice_args}
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(future_to_invoice):
            try:
                detailed_invoice, df_lines = future.result()

                detailed_invoices.append(detailed_invoice)

                if df_lines is not None and not df_lines.empty:
                    all_lines.append(df_lines)
                    
            except Exception as e:
                args = future_to_invoice[future]
                invoice_id = args[0].get('invoiceId', 'Unknown')
                logger.error(f"Failed to process invoice {invoice_id}: {e}")
                continue
    
    logger.info(f"Completed processing {len_df} invoices")
    
    # Return requested data
    df_detailed_summary = pd.DataFrame(detailed_invoices) if detailed_invoices else pd.DataFrame()
    df_all_lines = pd.concat(all_lines, ignore_index=True) if all_lines else pd.DataFrame()
    
    return df_detailed_summary, df_all_lines


def get_all_invoice_data_optimized(df_invoices, login: str, password: str, signer_key: str, tax_number: str = "32703094", save_xml: bool = False, xml_storage_path: str = None, use_threading: bool = True, max_workers: int = 4):
    """
    Get both detailed invoice summaries and line items with a single API call per invoice.
    This is the most efficient way to get comprehensive invoice data.
    
    Args:
        df_invoices: DataFrame with basic invoice information
        login: NAV login
        password: NAV password
        signer_key: NAV signer key
        tax_number: Tax number
        save_xml: Whether to save XML files to local storage
        xml_storage_path: Path where to save XML files (defaults to ./invoice_xmls)
        use_threading: Whether to use multithreading (default: True)
        max_workers: Maximum number of threads when using threading (default: 5)
    
    Returns:
        tuple: (detailed_summary_df, lines_df)
    """
    if use_threading:
        return get_comprehensive_invoice_details_threaded(
            df_invoices, login, password, signer_key, tax_number, 
            save_xml=save_xml, xml_storage_path=xml_storage_path, 
            max_workers=max_workers
        )
    else:
        return get_comprehensive_invoice_details(
            df_invoices, login, password, signer_key, tax_number, 
            save_xml=save_xml, xml_storage_path=xml_storage_path
        ) 