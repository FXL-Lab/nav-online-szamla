"""
Main NAV Online Számla API client.

This module provides the main client class for interacting with the NAV Online Számla API.
"""
import logging
from datetime import datetime
from typing import List, Optional, Dict, Any
import pandas as pd
import xml.dom.minidom

from .config import ONLINE_SZAMLA_URL, MAX_DATE_RANGE_DAYS
from .models import (
    NavCredentials, InvoiceDirection, InvoiceDigest, InvoiceDetail,
    ApiResponse, ErrorInfo,
    QueryInvoiceDigestRequest, QueryInvoiceCheckRequest, QueryInvoiceDataRequest,
    QueryInvoiceChainDigestRequest, MandatoryQueryParams, AdditionalQueryParams,
    RelationalQueryParams, TransactionQueryParams, InvoiceQueryParams,
    DateRange, DateTimeRange, OriginalInvoiceNumber, RelationalQueryParam,
    # API-compliant response types
    QueryInvoiceDigestResponseType, QueryInvoiceCheckResponseType,
    QueryInvoiceDataResponseType, QueryInvoiceChainDigestResponseType,
    InvoiceDigestType, InvoiceCheckResultType, InvoiceDataType,
    BasicOnlineInvoiceResponseType, BasicResultType, BasicHeaderType
)
from .exceptions import (
    NavApiException, NavValidationException, NavXmlParsingException,
    NavInvoiceNotFoundException
)
from .utils import (
    generate_password_hash, generate_custom_id, calculate_request_signature,
    validate_date_range, validate_tax_number, split_date_range,
    parse_xml_safely, get_xml_element_value, format_timestamp_for_nav,
    is_network_error
)
from .http_client import NavHttpClient

logger = logging.getLogger(__name__)


class NavOnlineInvoiceClient:
    """
    Main client for interacting with the NAV Online Számla API.
    
    This client provides methods for querying invoice data, getting invoice details,
    and managing invoice operations through the NAV API.
    """
    
    def __init__(self, base_url: str = ONLINE_SZAMLA_URL, timeout: int = 30):
        """
        Initialize the NAV API client.
        
        Args:
            base_url: Base URL for the NAV API
            timeout: Request timeout in seconds
        """
        self.base_url = base_url
        self.http_client = NavHttpClient(base_url, timeout)
        
    def validate_credentials(self, credentials: NavCredentials) -> None:
        """
        Validate NAV API credentials.
        
        Args:
            credentials: NAV API credentials
            
        Raises:
            NavValidationException: If credentials are invalid
        """
        if not all([credentials.login, credentials.password, credentials.signer_key]):
            raise NavValidationException("Missing required credentials: login, password, or signer_key")
        
        if not validate_tax_number(credentials.tax_number):
            raise NavValidationException(f"Invalid tax number format: {credentials.tax_number}")
    
    def get_token(self, credentials: NavCredentials) -> str:
        """
        Get exchange token from NAV API.
        
        Args:
            credentials: NAV API credentials
            
        Returns:
            str: Exchange token
            
        Raises:
            NavValidationException: If credentials are invalid
            NavApiException: If API call fails
        """
        self.validate_credentials(credentials)
        
        request_id = generate_custom_id()
        timestamp = format_timestamp_for_nav(datetime.now())
        
        # Build token exchange request
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        request_data = {
            "user": {
                "login": credentials.login,
                "passwordHash": password_hash,
                "taxNumber": credentials.tax_number,
                "requestSignature": request_signature
            }
        }
        
        import json
        
        with self.http_client as client:
            headers = {"Content-Type": "application/json"}
            response = client.post("/tokenExchange", json.dumps(request_data), headers)
            
        try:
            response_data = response.json()
        except ValueError:
            raise NavApiException("Invalid JSON response from token exchange")
            
        if response_data.get("result", {}).get("funcCode") == "OK":
            return response_data["result"]["encodedExchangeToken"]
        else:
            error_code = response_data.get("result", {}).get("errorCode", "UNKNOWN_ERROR")
            message = response_data.get("result", {}).get("message", "Token exchange failed")
            raise NavApiException(f"{error_code}: {message}")

    def _build_basic_request_xml(self, credentials: NavCredentials, request_id: str, 
                                timestamp: str) -> str:
        """
        Build basic request XML structure with authentication.
        
        Args:
            credentials: NAV API credentials
            request_id: Unique request ID
            timestamp: Request timestamp
            
        Returns:
            str: Basic XML request structure
        """
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDigestRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base">
    <header>
        <requestId>{request_id}</requestId>
        <timestamp>{timestamp}</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <user>
        <login>{credentials.login}</login>
        <passwordHash>{password_hash}</passwordHash>
        <taxNumber>{credentials.tax_number}</taxNumber>
        <requestSignature>{request_signature}</requestSignature>
    </user>
    <software>
        <softwareId>NAV_PYTHON_CLIENT</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>{credentials.tax_number}</softwareDevTaxNumber>
    </software>"""
    
    def _build_query_invoice_data_xml(self, credentials: NavCredentials, invoice_number: str,
                                     invoice_direction: InvoiceDirection, 
                                     supplier_tax_number: Optional[str] = None,
                                     batch_index: Optional[int] = None) -> str:
        """
        Build XML for queryInvoiceData request.
        
        Args:
            credentials: NAV API credentials
            invoice_number: Invoice number to query
            invoice_direction: Invoice direction
            supplier_tax_number: Optional supplier tax number
            batch_index: Optional batch index
            
        Returns:
            str: Complete XML request
        """
        request_id = generate_custom_id()
        timestamp = format_timestamp_for_nav()
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        supplier_tax_filter = ""
        if supplier_tax_number:
            supplier_tax_filter = f"<supplierTaxNumber>{supplier_tax_number}</supplierTaxNumber>"
        
        batch_index_filter = ""
        if batch_index is not None:
            batch_index_filter = f"<batchIndex>{batch_index}</batchIndex>"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDataRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base">
    <header>
        <requestId>{request_id}</requestId>
        <timestamp>{timestamp}</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <user>
        <login>{credentials.login}</login>
        <passwordHash>{password_hash}</passwordHash>
        <taxNumber>{credentials.tax_number}</taxNumber>
        <requestSignature>{request_signature}</requestSignature>
    </user>
    <software>
        <softwareId>NAV_PYTHON_CLIENT</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>{credentials.tax_number}</softwareDevTaxNumber>
    </software>
    <invoiceNumber>{invoice_number}</invoiceNumber>
    <invoiceDirection>{invoice_direction.value}</invoiceDirection>
    {batch_index_filter}
    {supplier_tax_filter}
</QueryInvoiceDataRequest>"""

    def _build_query_invoice_digest_request_xml(self, credentials: NavCredentials, 
                                               request: QueryInvoiceDigestRequest) -> str:
        """Build XML for QueryInvoiceDigest request according to API specification."""
        request_id = generate_custom_id()
        timestamp = format_timestamp_for_nav()
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        # Build mandatory query params
        mandatory_params = ""
        if request.invoice_query_params.mandatory_query_params.invoice_issue_date:
            date_range = request.invoice_query_params.mandatory_query_params.invoice_issue_date
            mandatory_params += f"""
            <invoiceIssueDate>
                <dateFrom>{date_range.date_from}</dateFrom>
                <dateTo>{date_range.date_to}</dateTo>
            </invoiceIssueDate>"""
        
        if request.invoice_query_params.mandatory_query_params.ins_date:
            datetime_range = request.invoice_query_params.mandatory_query_params.ins_date
            mandatory_params += f"""
            <insDate>
                <dateTimeFrom>{datetime_range.date_time_from}</dateTimeFrom>
                <dateTimeTo>{datetime_range.date_time_to}</dateTimeTo>
            </insDate>"""
        
        if request.invoice_query_params.mandatory_query_params.original_invoice_number:
            orig_num = request.invoice_query_params.mandatory_query_params.original_invoice_number
            mandatory_params += f"""
            <originalInvoiceNumber>
                <originalInvoiceNumber>{orig_num.original_invoice_number}</originalInvoiceNumber>
            </originalInvoiceNumber>"""
        
        # Build additional query params
        additional_params = ""
        if request.invoice_query_params.additional_query_params:
            add_params = request.invoice_query_params.additional_query_params
            additional_elements = []
            
            if add_params.tax_number:
                additional_elements.append(f"<taxNumber>{add_params.tax_number}</taxNumber>")
            if add_params.group_member_tax_number:
                additional_elements.append(f"<groupMemberTaxNumber>{add_params.group_member_tax_number}</groupMemberTaxNumber>")
            if add_params.name:
                additional_elements.append(f"<name>{add_params.name}</name>")
            if add_params.invoice_category:
                additional_elements.append(f"<invoiceCategory>{add_params.invoice_category.value}</invoiceCategory>")
            if add_params.payment_method:
                additional_elements.append(f"<paymentMethod>{add_params.payment_method.value}</paymentMethod>")
            if add_params.invoice_appearance:
                additional_elements.append(f"<invoiceAppearance>{add_params.invoice_appearance.value}</invoiceAppearance>")
            if add_params.source:
                additional_elements.append(f"<source>{add_params.source.value}</source>")
            if add_params.currency:
                additional_elements.append(f"<currency>{add_params.currency}</currency>")
            
            if additional_elements:
                additional_params = f"""
        <additionalQueryParams>
            {''.join(additional_elements)}
        </additionalQueryParams>"""
        
        # Build relational query params
        relational_params = ""
        if request.invoice_query_params.relational_query_params:
            rel_params = request.invoice_query_params.relational_query_params
            relational_elements = []
            
            if rel_params.invoice_delivery:
                relational_elements.append(f"""
            <invoiceDelivery>
                <queryOperator>{rel_params.invoice_delivery.query_operator.value}</queryOperator>
                <queryValue>{rel_params.invoice_delivery.query_value}</queryValue>
            </invoiceDelivery>""")
            
            if rel_params.payment_date:
                relational_elements.append(f"""
            <paymentDate>
                <queryOperator>{rel_params.payment_date.query_operator.value}</queryOperator>
                <queryValue>{rel_params.payment_date.query_value}</queryValue>
            </paymentDate>""")
            
            if rel_params.invoice_net_amount:
                relational_elements.append(f"""
            <invoiceNetAmount>
                <queryOperator>{rel_params.invoice_net_amount.query_operator.value}</queryOperator>
                <queryValue>{rel_params.invoice_net_amount.query_value}</queryValue>
            </invoiceNetAmount>""")
            
            if rel_params.invoice_net_amount_huf:
                relational_elements.append(f"""
            <invoiceNetAmountHUF>
                <queryOperator>{rel_params.invoice_net_amount_huf.query_operator.value}</queryOperator>
                <queryValue>{rel_params.invoice_net_amount_huf.query_value}</queryValue>
            </invoiceNetAmountHUF>""")
            
            if rel_params.invoice_vat_amount:
                relational_elements.append(f"""
            <invoiceVatAmount>
                <queryOperator>{rel_params.invoice_vat_amount.query_operator.value}</queryOperator>
                <queryValue>{rel_params.invoice_vat_amount.query_value}</queryValue>
            </invoiceVatAmount>""")
            
            if rel_params.invoice_vat_amount_huf:
                relational_elements.append(f"""
            <invoiceVatAmountHUF>
                <queryOperator>{rel_params.invoice_vat_amount_huf.query_operator.value}</queryOperator>
                <queryValue>{rel_params.invoice_vat_amount_huf.query_value}</queryValue>
            </invoiceVatAmountHUF>""")
            
            if relational_elements:
                relational_params = f"""
        <relationalQueryParams>
            {''.join(relational_elements)}
        </relationalQueryParams>"""
        
        # Build transaction query params
        transaction_params = ""
        if request.invoice_query_params.transaction_query_params:
            trans_params = request.invoice_query_params.transaction_query_params
            transaction_elements = []
            
            if trans_params.transaction_id:
                transaction_elements.append(f"<transactionId>{trans_params.transaction_id}</transactionId>")
            if trans_params.index:
                transaction_elements.append(f"<index>{trans_params.index}</index>")
            if trans_params.invoice_operation:
                transaction_elements.append(f"<invoiceOperation>{trans_params.invoice_operation.value}</invoiceOperation>")
            
            if transaction_elements:
                transaction_params = f"""
        <transactionQueryParams>
            {''.join(transaction_elements)}
        </transactionQueryParams>"""
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDigestRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base">
    <header>
        <requestId>{request_id}</requestId>
        <timestamp>{timestamp}</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <user>
        <login>{credentials.login}</login>
        <passwordHash>{password_hash}</passwordHash>
        <taxNumber>{credentials.tax_number}</taxNumber>
        <requestSignature>{request_signature}</requestSignature>
    </user>
    <software>
        <softwareId>NAV_PYTHON_CLIENT</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>{credentials.tax_number}</softwareDevTaxNumber>
    </software>
    <page>{request.page}</page>
    <invoiceDirection>{request.invoice_direction.value}</invoiceDirection>
    <invoiceQueryParams>
        <mandatoryQueryParams>{mandatory_params}
        </mandatoryQueryParams>{additional_params}{relational_params}{transaction_params}
    </invoiceQueryParams>
</QueryInvoiceDigestRequest>"""

    def _build_query_invoice_check_request_xml(self, credentials: NavCredentials, 
                                              request: QueryInvoiceCheckRequest) -> str:
        """Build XML for QueryInvoiceCheck request according to API specification."""
        request_id = generate_custom_id()
        timestamp = format_timestamp_for_nav()
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        batch_index_filter = ""
        if request.batch_index is not None:
            batch_index_filter = f"<batchIndex>{request.batch_index}</batchIndex>"
        
        supplier_tax_filter = ""
        if request.supplier_tax_number:
            supplier_tax_filter = f"<supplierTaxNumber>{request.supplier_tax_number}</supplierTaxNumber>"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceCheckRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base">
    <header>
        <requestId>{request_id}</requestId>
        <timestamp>{timestamp}</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <user>
        <login>{credentials.login}</login>
        <passwordHash>{password_hash}</passwordHash>
        <taxNumber>{credentials.tax_number}</taxNumber>
        <requestSignature>{request_signature}</requestSignature>
    </user>
    <software>
        <softwareId>NAV_PYTHON_CLIENT</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>{credentials.tax_number}</softwareDevTaxNumber>
    </software>
    <invoiceNumber>{request.invoice_number}</invoiceNumber>
    <invoiceDirection>{request.invoice_direction.value}</invoiceDirection>
    {batch_index_filter}
    {supplier_tax_filter}
</QueryInvoiceCheckRequest>"""

    def _build_query_invoice_data_request_xml(self, credentials: NavCredentials, 
                                             request: QueryInvoiceDataRequest) -> str:
        """Build XML for QueryInvoiceData request according to API specification."""
        request_id = generate_custom_id()
        timestamp = format_timestamp_for_nav()
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        batch_index_filter = ""
        if request.batch_index is not None:
            batch_index_filter = f"<batchIndex>{request.batch_index}</batchIndex>"
        
        supplier_tax_filter = ""
        if request.supplier_tax_number:
            supplier_tax_filter = f"<supplierTaxNumber>{request.supplier_tax_number}</supplierTaxNumber>"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDataRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base">
    <header>
        <requestId>{request_id}</requestId>
        <timestamp>{timestamp}</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <user>
        <login>{credentials.login}</login>
        <passwordHash>{password_hash}</passwordHash>
        <taxNumber>{credentials.tax_number}</taxNumber>
        <requestSignature>{request_signature}</requestSignature>
    </user>
    <software>
        <softwareId>NAV_PYTHON_CLIENT</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>{credentials.tax_number}</softwareDevTaxNumber>
    </software>
    <invoiceNumber>{request.invoice_number}</invoiceNumber>
    <invoiceDirection>{request.invoice_direction.value}</invoiceDirection>
    {batch_index_filter}
    {supplier_tax_filter}
</QueryInvoiceDataRequest>"""

    def _build_query_invoice_chain_digest_request_xml(self, credentials: NavCredentials, 
                                                     request: QueryInvoiceChainDigestRequest) -> str:
        """Build XML for QueryInvoiceChainDigest request according to API specification."""
        request_id = generate_custom_id()
        timestamp = format_timestamp_for_nav()
        password_hash = generate_password_hash(credentials.password)
        request_signature = calculate_request_signature(request_id, timestamp, credentials.signer_key)
        
        tax_number_filter = ""
        if request.tax_number:
            tax_number_filter = f"<taxNumber>{request.tax_number}</taxNumber>"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceChainDigestRequest xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" xmlns:base="http://schemas.nav.gov.hu/OSA/3.0/base">
    <header>
        <requestId>{request_id}</requestId>
        <timestamp>{timestamp}</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <user>
        <login>{credentials.login}</login>
        <passwordHash>{password_hash}</passwordHash>
        <taxNumber>{credentials.tax_number}</taxNumber>
        <requestSignature>{request_signature}</requestSignature>
    </user>
    <software>
        <softwareId>NAV_PYTHON_CLIENT</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>{credentials.tax_number}</softwareDevTaxNumber>
    </software>
    <page>{request.page}</page>
    <invoiceNumber>{request.invoice_number}</invoiceNumber>
    <invoiceDirection>{request.invoice_direction.value}</invoiceDirection>
    {tax_number_filter}
</QueryInvoiceChainDigestRequest>"""
    
    def _parse_error_response(self, xml_response: str) -> ErrorInfo:
        """
        Parse error response from NAV API.
        
        Args:
            xml_response: XML response string
            
        Returns:
            ErrorInfo: Parsed error information
        """
        try:
            dom = parse_xml_safely(xml_response)
            
            error_code = get_xml_element_value(dom, 'errorCode', 'UNKNOWN')
            if not error_code:
                error_code = get_xml_element_value(dom, 'ns2:errorCode', 'UNKNOWN')
            
            message = get_xml_element_value(dom, 'message', 'Unknown error')
            if not message:
                message = get_xml_element_value(dom, 'ns2:message', 'Unknown error')
            
            return ErrorInfo(
                error_code=error_code,
                message=message,
                timestamp=datetime.now()
            )
        except Exception as e:
            logger.error(f"Failed to parse error response: {e}")
            return ErrorInfo(
                error_code='XML_PARSE_ERROR',
                message=f"Failed to parse error response: {str(e)}",
                timestamp=datetime.now()
            )
    
    def _parse_invoice_digest_response(self, xml_response: str) -> List[InvoiceDigest]:
        """
        Parse invoice digest response from XML.
        
        Args:
            xml_response: XML response string
            
        Returns:
            List[InvoiceDigest]: List of invoice digests
        """
        try:
            dom = parse_xml_safely(xml_response)
            
            # Check for errors first
            error_elements = dom.getElementsByTagName('errorCode')
            if error_elements:
                error_info = self._parse_error_response(xml_response)
                raise NavApiException(f"NAV API Error: {error_info.error_code} - {error_info.message}")
            
            invoices = []
            invoice_elements = dom.getElementsByTagName('invoiceDigest')
            
            for invoice_elem in invoice_elements:
                try:
                    # Extract basic invoice information
                    invoice_number = get_xml_element_value(invoice_elem, 'invoiceNumber', '')
                    
                    # Parse dates
                    issue_date_str = get_xml_element_value(invoice_elem, 'issueDate', '')
                    issue_date = datetime.strptime(issue_date_str, '%Y-%m-%d') if issue_date_str else datetime.now()
                    
                    completion_date_str = get_xml_element_value(invoice_elem, 'completionDate', '')
                    completion_date = None
                    if completion_date_str:
                        try:
                            completion_date = datetime.strptime(completion_date_str, '%Y-%m-%d')
                        except ValueError:
                            pass
                    
                    # Parse amounts
                    net_amount = float(get_xml_element_value(invoice_elem, 'invoiceNetAmount', '0') or '0')
                    vat_amount = float(get_xml_element_value(invoice_elem, 'invoiceVatAmount', '0') or '0')
                    gross_amount = float(get_xml_element_value(invoice_elem, 'invoiceGrossAmount', '0') or '0')
                    
                    # Parse other fields
                    operation = get_xml_element_value(invoice_elem, 'invoiceOperation', 'CREATE')
                    supplier_name = get_xml_element_value(invoice_elem, 'supplierName', '')
                    supplier_tax_number = get_xml_element_value(invoice_elem, 'supplierTaxNumber', '')
                    customer_name = get_xml_element_value(invoice_elem, 'customerName', '')
                    customer_tax_number = get_xml_element_value(invoice_elem, 'customerTaxNumber', '')
                    currency_code = get_xml_element_value(invoice_elem, 'currencyCode', 'HUF')
                    source = get_xml_element_value(invoice_elem, 'source', 'UNKNOWN')
                    
                    # Parse batch index if present
                    batch_index_str = get_xml_element_value(invoice_elem, 'batchIndex', '')
                    batch_index = int(batch_index_str) if batch_index_str else None
                    
                    from .models import InvoiceOperation
                    
                    digest = InvoiceDigest(
                        invoice_number=invoice_number,
                        batch_index=batch_index,
                        invoice_operation=InvoiceOperation(operation),
                        supplier_name=supplier_name,
                        supplier_tax_number=supplier_tax_number,
                        customer_name=customer_name,
                        customer_tax_number=customer_tax_number,
                        issue_date=issue_date,
                        completion_date=completion_date,
                        invoice_net_amount=net_amount,
                        invoice_vat_amount=vat_amount,
                        invoice_gross_amount=gross_amount,
                        currency_code=currency_code,
                        source=source
                    )
                    
                    invoices.append(digest)
                    
                except Exception as e:
                    logger.warning(f"Failed to parse invoice element: {e}")
                    continue
            
            return invoices
            
        except NavApiException:
            raise
        except Exception as e:
            raise NavXmlParsingException(f"Failed to parse invoice digest response: {str(e)}")
    
    def _parse_api_compliant_invoice_digest_response(self, xml_response: str) -> QueryInvoiceDigestResponseType:
        """
        Parse invoice digest response from XML to API-compliant response type.
        
        Args:
            xml_response: XML response string
            
        Returns:
            QueryInvoiceDigestResponseType: API-compliant response with invoice digests
        """
        try:
            dom = parse_xml_safely(xml_response)
            
            # Check for errors first
            error_elements = dom.getElementsByTagName('errorCode')
            if error_elements:
                error_info = self._parse_error_response(xml_response)
                raise NavApiException(f"NAV API Error: {error_info.error_code} - {error_info.message}")
            
            # Parse header
            header_elem = dom.getElementsByTagName('header')[0] if dom.getElementsByTagName('header') else None
            header = None
            if header_elem:
                header = BasicHeaderType(
                    request_id=get_xml_element_value(header_elem, 'requestId', ''),
                    timestamp=get_xml_element_value(header_elem, 'timestamp', ''),
                    request_version=get_xml_element_value(header_elem, 'requestVersion', '3.0'),
                    header_version=get_xml_element_value(header_elem, 'headerVersion', '1.0')
                )
            
            # Parse result
            result_elem = dom.getElementsByTagName('r')[0] if dom.getElementsByTagName('r') else None
            result = None
            if result_elem:
                result = BasicResultType(
                    func_code=get_xml_element_value(result_elem, 'funcCode', 'ERROR'),
                    error_code=get_xml_element_value(result_elem, 'errorCode', None),
                    message=get_xml_element_value(result_elem, 'message', None)
                )
            
            # Parse invoice digests
            invoice_digests = []
            invoice_elements = dom.getElementsByTagName('invoiceDigest')
            
            for invoice_elem in invoice_elements:
                try:
                    # Extract basic invoice information
                    invoice_number = get_xml_element_value(invoice_elem, 'invoiceNumber', '')
                    
                    # Parse direction
                    direction_str = get_xml_element_value(invoice_elem, 'invoiceDirection', 'OUTBOUND')
                    invoice_direction = InvoiceDirection(direction_str)
                    
                    # Parse dates
                    ins_date_str = get_xml_element_value(invoice_elem, 'insDate', '')
                    ins_date = datetime.fromisoformat(ins_date_str.replace('Z', '+00:00')) if ins_date_str else None
                    
                    # Parse other fields
                    batch_index_str = get_xml_element_value(invoice_elem, 'batchIndex', '')
                    batch_index = int(batch_index_str) if batch_index_str else None
                    
                    invoice_operation = get_xml_element_value(invoice_elem, 'invoiceOperation', 'CREATE')
                    supplier_tax_number = get_xml_element_value(invoice_elem, 'supplierTaxNumber', '')
                    customer_tax_number = get_xml_element_value(invoice_elem, 'customerTaxNumber', '')
                    completeness_indicator = get_xml_element_value(invoice_elem, 'completenessIndicator', 'false') == 'true'
                    original_request_version = get_xml_element_value(invoice_elem, 'originalRequestVersion', '3.0')
                    
                    digest = InvoiceDigestType(
                        invoice_number=invoice_number,
                        invoice_direction=invoice_direction,
                        batch_index=batch_index,
                        invoice_operation=invoice_operation,
                        supplier_tax_number=supplier_tax_number,
                        customer_tax_number=customer_tax_number,
                        ins_date=ins_date,
                        completeness_indicator=completeness_indicator,
                        original_request_version=original_request_version
                    )
                    
                    invoice_digests.append(digest)
                    
                except Exception as e:
                    logger.warning(f"Failed to parse invoice element: {e}")
                    continue
            
            # Parse pagination info
            current_page = None
            available_page = None
            available_count = None
            
            digest_result = dom.getElementsByTagName('invoiceDigestResult')
            if digest_result:
                current_page_str = get_xml_element_value(digest_result[0], 'currentPage', '')
                available_page_str = get_xml_element_value(digest_result[0], 'availablePage', '')
                available_count_str = get_xml_element_value(digest_result[0], 'availableCount', '')
                
                current_page = int(current_page_str) if current_page_str else None
                available_page = int(available_page_str) if available_page_str else None
                available_count = int(available_count_str) if available_count_str else None
            
            return QueryInvoiceDigestResponseType(
                header=header,
                result=result,
                software=None,  # Software info not typically in digest response
                current_page=current_page,
                available_page=available_page,
                available_count=available_count,
                invoice_digests=invoice_digests
            )
            
        except NavApiException:
            raise
        except Exception as e:
            raise NavXmlParsingException(f"Failed to parse invoice digest response: {str(e)}")

    def get_invoice_detail(self, credentials: NavCredentials, invoice_number: str, 
                          invoice_direction: InvoiceDirection,
                          supplier_tax_number: Optional[str] = None,
                          batch_index: Optional[int] = None) -> QueryInvoiceDataResponseType:
        """
        Get detailed information for a specific invoice.
        
        Args:
            credentials: NAV API credentials
            invoice_number: Invoice number to query
            invoice_direction: Invoice direction (OUTBOUND/INBOUND)
            supplier_tax_number: Optional supplier tax number
            batch_index: Optional batch index for batched invoices
            
        Returns:
            QueryInvoiceDataResponseType: API-compliant response with detailed invoice data
            
        Raises:
            NavValidationException: If parameters are invalid
            NavInvoiceNotFoundException: If invoice not found
            NavApiException: If API request fails
        """
        self.validate_credentials(credentials)
        
        if not invoice_number:
            raise NavValidationException("Invoice number is required")
        
        try:
            xml_request = self._build_query_invoice_data_xml(
                credentials, invoice_number, invoice_direction, 
                supplier_tax_number, batch_index
            )
            response = self.http_client.post('queryInvoiceData', xml_request)
            
            return self._parse_invoice_detail_response(response.text)
            
        except Exception as e:
            if is_network_error(str(e)):
                logger.error(f"Network error after retries: {e}")
                raise NavApiException(f"Network error: {str(e)}")
            raise
    
    def _parse_invoice_detail_response(self, xml_response: str) -> InvoiceDetail:
        """
        Parse invoice detail response from XML.
        
        Args:
            xml_response: XML response string
            
        Returns:
            InvoiceDetail: Parsed invoice detail
        """
        try:
            dom = parse_xml_safely(xml_response)
            
            # Check for errors first
            error_elements = dom.getElementsByTagName('errorCode')
            if error_elements:
                error_info = self._parse_error_response(xml_response)
                if error_info.error_code in ['INVOICE_NOT_FOUND', 'NO_INVOICE_FOUND']:
                    raise NavInvoiceNotFoundException(f"Invoice not found: {error_info.message}")
                raise NavApiException(f"NAV API Error: {error_info.error_code} - {error_info.message}")
            
            # TODO: Implement detailed invoice parsing based on the mapping in nav_constans.py
            # For now, return a basic structure
            invoice_number = get_xml_element_value(dom, 'invoiceNumber', '')
            
            # This is a simplified implementation - should be expanded based on requirements
            detail = InvoiceDetail(
                invoice_number=invoice_number,
                issue_date=datetime.now(),  # TODO: Parse from XML
                completion_date=None,  # TODO: Parse from XML
                currency_code='HUF',  # TODO: Parse from XML
                exchange_rate=None,  # TODO: Parse from XML
                supplier_info=None,  # TODO: Parse from XML
                customer_info=None,  # TODO: Parse from XML
                invoice_net_amount=0.0,  # TODO: Parse from XML
                invoice_vat_amount=0.0,  # TODO: Parse from XML
                invoice_gross_amount=0.0,  # TODO: Parse from XML
                source='UNKNOWN',  # TODO: Parse from XML
                additional_data={}  # TODO: Parse additional fields
            )
            
            return detail
            
        except (NavInvoiceNotFoundException, NavApiException):
            raise
        except Exception as e:
            raise NavXmlParsingException(f"Failed to parse invoice detail response: {str(e)}")

    # New methods using API-compliant request types
    
    def query_invoice_digest(self, credentials: NavCredentials, 
                           request: QueryInvoiceDigestRequest) -> QueryInvoiceDigestResponseType:
        """
        Query invoice digests using the official API request structure.
        
        Args:
            credentials: NAV API credentials
            request: QueryInvoiceDigestRequest with proper API structure
            
        Returns:
            QueryInvoiceDigestResponseType: API-compliant response with invoice digests
            
        Raises:
            NavValidationException: If request validation fails
            NavApiException: If API call fails
        """
        try:
            # Validate credentials
            self.validate_credentials(credentials)
            
            # Build XML request
            xml_request = self._build_query_invoice_digest_request_xml(credentials, request)
            
            # Make API call
            with self.http_client as client:
                response = client.post("/queryInvoiceDigest", xml_request)
                xml_response = response.text
            
            # Parse response
            return self._parse_api_compliant_invoice_digest_response(xml_response)
            
        except (NavValidationException, NavApiException):
            raise
        except Exception as e:
            logger.error(f"Unexpected error in query_invoice_digest: {str(e)}")
            raise NavApiException(f"Unexpected error: {str(e)}")

    def query_invoice_check(self, credentials: NavCredentials, 
                          request: QueryInvoiceCheckRequest) -> QueryInvoiceCheckResponseType:
        """
        Check if an invoice exists using the official API request structure.
        
        Args:
            credentials: NAV API credentials
            request: QueryInvoiceCheckRequest with proper API structure
            
        Returns:
            QueryInvoiceCheckResponseType: API-compliant response with check results
            
        Raises:
            NavValidationException: If request validation fails
            NavApiException: If API call fails
        """
        try:
            # Validate credentials
            self.validate_credentials(credentials)
            
            # Build XML request
            xml_request = self._build_query_invoice_check_request_xml(credentials, request)
            
            # Make API call
            with self.http_client as client:
                xml_response = client.post("/queryInvoiceCheck", xml_request)
            
            # Parse response
            try:
                dom = parse_xml_safely(xml_response)
                result_element = dom.getElementsByTagName("invoiceCheckResult")
                
                if result_element:
                    return result_element[0].firstChild.nodeValue.lower() == "true"
                else:
                    return False
                    
            except Exception as e:
                raise NavXmlParsingException(f"Failed to parse invoice check response: {str(e)}")
            
        except (NavValidationException, NavApiException):
            raise
        except Exception as e:
            logger.error(f"Unexpected error in query_invoice_check: {str(e)}")
            raise NavApiException(f"Unexpected error: {str(e)}")

    def query_invoice_data(self, credentials: NavCredentials, 
                         request: QueryInvoiceDataRequest) -> Optional[InvoiceDetail]:
        """
        Get full invoice data using the official API request structure.
        
        Args:
            credentials: NAV API credentials
            request: QueryInvoiceDataRequest with proper API structure
            
        Returns:
            Optional[InvoiceDetail]: Invoice detail if found, None otherwise
            
        Raises:
            NavValidationException: If request validation fails
            NavApiException: If API call fails
        """
        try:
            # Validate credentials
            self.validate_credentials(credentials)
            
            # Build XML request
            xml_request = self._build_query_invoice_data_request_xml(credentials, request)
            
            # Make API call
            with self.http_client as client:
                xml_response = client.post("/queryInvoiceData", xml_request)
            
            # Parse response
            return self._parse_invoice_detail_response(xml_response)
            
        except NavInvoiceNotFoundException:
            return None
        except (NavValidationException, NavApiException):
            raise
        except Exception as e:
            logger.error(f"Unexpected error in query_invoice_data: {str(e)}")
            raise NavApiException(f"Unexpected error: {str(e)}")

    def query_invoice_chain_digest(self, credentials: NavCredentials, 
                                 request: QueryInvoiceChainDigestRequest) -> List[InvoiceDigest]:
        """
        Query invoice chain digests using the official API request structure.
        
        Args:
            credentials: NAV API credentials
            request: QueryInvoiceChainDigestRequest with proper API structure
            
        Returns:
            List[InvoiceDigest]: List of invoice chain elements
            
        Raises:
            NavValidationException: If request validation fails
            NavApiException: If API call fails
        """
        try:
            # Validate credentials
            self.validate_credentials(credentials)
            
            # Build XML request
            xml_request = self._build_query_invoice_chain_digest_request_xml(credentials, request)
            
            # Make API call
            with self.http_client as client:
                xml_response = client.post("/queryInvoiceChainDigest", xml_request)
            
            # Parse response (reusing the same parser as it's similar structure)
            return self._parse_invoice_digest_response(xml_response)
            
        except (NavValidationException, NavApiException):
            raise
        except Exception as e:
            logger.error(f"Unexpected error in query_invoice_chain_digest: {str(e)}")
            raise NavApiException(f"Unexpected error: {str(e)}")

    def close(self):
        """Close the HTTP client."""
        self.http_client.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
