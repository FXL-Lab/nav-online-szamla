#!/usr/bin/env python3
"""
Single Invoice Fetch Test Script

Test script to fetch a specific invoice using get_invoice_data method.
Uses Diego's production credentials to fetch invoice: 1001002131002/25
"""
import datetime as dt
import logging
from pathlib import Path
import json

# NAV imports
from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.config import NavEnvironment
from nav_online_szamla.models import InvoiceDirectionType
from nav_online_szamla.exceptions import NavApiException, NavValidationException, NavInvoiceNotFoundException

# Import credentials
from creds import DIEGO_PROD

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_single_invoice_fetch(
    credentials, 
    invoice_number: str,
    invoice_direction: InvoiceDirectionType = InvoiceDirectionType.OUTBOUND,
    environment: NavEnvironment = NavEnvironment.PRODUCTION
):
    """
    Test fetching a single invoice using get_invoice_data method.
    
    Args:
        credentials: NAV credentials to use
        invoice_number: Specific invoice number to fetch
        invoice_direction: Invoice direction (OUTBOUND or INBOUND)
        environment: NAV environment (TEST or PRODUCTION)
    
    Returns:
        dict: Test results with invoice data details
    """
    logger.info("=" * 80)
    logger.info("SINGLE INVOICE FETCH TEST")
    logger.info("=" * 80)
    logger.info(f"Credentials: {credentials.tax_number}")
    logger.info(f"Environment: {environment.value}")
    logger.info(f"Invoice Number: {invoice_number}")
    logger.info(f"Direction: {invoice_direction.value}")
    logger.info("=" * 80)
    
    test_result = {
        'invoice_number': invoice_number,
        'direction': invoice_direction.value,
        'environment': environment.value,
        'tax_number': credentials.tax_number,
        'timestamp': dt.datetime.now().isoformat(),
        'status': 'unknown',
        'error': None,
        'invoice_data': None,
        'summary': {}
    }
    
    try:
        logger.info("🔌 Connecting to NAV API...")
        
        with NavOnlineInvoiceClient(credentials, environment=environment) as client:
            logger.info("✅ Connection established")
            
            # Test basic connection first
            logger.info("🔑 Testing authentication...")
            token_response = client.get_token()
            logger.info("✅ Authentication successful")
            
            # Fetch the specific invoice
            logger.info(f"📄 Fetching invoice: {invoice_number}")
            
            invoice_data = client.get_invoice_data(
                invoice_number=invoice_number,
                invoice_direction=invoice_direction
            )
            
            logger.info("✅ Invoice fetched successfully!")
            
            # Extract key information from the invoice
            summary = extract_invoice_summary(invoice_data)
            test_result['summary'] = summary
            test_result['status'] = 'success'
            
            # Log the summary
            logger.info("\n📋 INVOICE SUMMARY:")
            logger.info("-" * 40)
            for key, value in summary.items():
                logger.info(f"{key}: {value}")
            
            # Save detailed invoice data to file (optional)
            save_invoice_details(invoice_data, invoice_number, credentials.tax_number)
            
            return test_result
            
    except NavInvoiceNotFoundException as e:
        logger.error(f"❌ Invoice not found: {e}")
        test_result['status'] = 'not_found'
        test_result['error'] = str(e)
        return test_result
        
    except NavApiException as e:
        logger.error(f"❌ NAV API error: {e}")
        test_result['status'] = 'api_error'
        test_result['error'] = str(e)
        return test_result
        
    except NavValidationException as e:
        logger.error(f"❌ Validation error: {e}")
        test_result['status'] = 'validation_error'
        test_result['error'] = str(e)
        return test_result
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        test_result['status'] = 'unexpected_error'
        test_result['error'] = str(e)
        return test_result


def extract_invoice_summary(invoice_data):
    """
    Extract key information from invoice data for summary display.
    
    Args:
        invoice_data: InvoiceData object from NAV API
    
    Returns:
        dict: Summary of key invoice information
    """
    summary = {}
    
    try:
        # Basic invoice information
        summary['Invoice Number'] = getattr(invoice_data, 'invoice_number', 'N/A')
        summary['Issue Date'] = getattr(invoice_data, 'invoice_issue_date', 'N/A')
        summary['Completeness Indicator'] = getattr(invoice_data, 'completeness_indicator', 'N/A')
        
        # Access the main invoice structure
        if hasattr(invoice_data, 'invoice_main') and invoice_data.invoice_main:
            invoice_main = invoice_data.invoice_main
            
            if hasattr(invoice_main, 'invoice') and invoice_main.invoice:
                invoice = invoice_main.invoice
                
                # Invoice head information
                if hasattr(invoice, 'invoice_head') and invoice.invoice_head:
                    head = invoice.invoice_head
                    
                    # Supplier info
                    if hasattr(head, 'supplier_info') and head.supplier_info:
                        supplier = head.supplier_info
                        summary['Supplier Name'] = getattr(supplier, 'supplier_name', 'N/A')
                        if hasattr(supplier, 'supplier_tax_number') and supplier.supplier_tax_number:
                            summary['Supplier Tax Number'] = supplier.supplier_tax_number.taxpayer_id
                    
                    # Customer info
                    if hasattr(head, 'customer_info') and head.customer_info:
                        customer = head.customer_info
                        summary['Customer Name'] = getattr(customer, 'customer_name', 'N/A')
                        if hasattr(customer, 'customer_vat_data') and customer.customer_vat_data:
                            if hasattr(customer.customer_vat_data, 'customer_tax_number') and customer.customer_vat_data.customer_tax_number:
                                summary['Customer Tax Number'] = customer.customer_vat_data.customer_tax_number.taxpayer_id
                    
                    # Invoice details
                    if hasattr(head, 'invoice_detail') and head.invoice_detail:
                        detail = head.invoice_detail
                        summary['Invoice Category'] = getattr(detail, 'invoice_category', 'N/A')
                        summary['Currency'] = getattr(detail, 'currency_code', 'N/A')
                        summary['Delivery Date'] = getattr(detail, 'invoice_delivery_date', 'N/A')
                        summary['Payment Method'] = getattr(detail, 'payment_method', 'N/A')
                        summary['Self Billing'] = getattr(detail, 'self_billing_indicator', 'N/A')
                        summary['Invoice Appearance'] = getattr(detail, 'invoice_appearance', 'N/A')
                
                # Line items
                if hasattr(invoice, 'invoice_lines') and invoice.invoice_lines:
                    if hasattr(invoice.invoice_lines, 'line') and invoice.invoice_lines.line:
                        lines = invoice.invoice_lines.line
                        summary['Line Items Count'] = len(lines)
                        
                        # Sample line item info
                        if lines:
                            first_line = lines[0]
                            summary['First Line Description'] = getattr(first_line, 'line_description', 'N/A')[:100] + '...' if len(getattr(first_line, 'line_description', '')) > 100 else getattr(first_line, 'line_description', 'N/A')
                            summary['First Line Quantity'] = f"{getattr(first_line, 'quantity', 'N/A')} {getattr(first_line, 'unit_of_measure_own', '')}"
                            summary['First Line Unit Price'] = f"{getattr(first_line, 'unit_price', 'N/A')} {summary.get('Currency', '')}"
                    else:
                        summary['Line Items Count'] = 0
                else:
                    summary['Line Items Count'] = 0
                
                # Invoice summary/totals
                if hasattr(invoice, 'invoice_summary') and invoice.invoice_summary:
                    inv_summary = invoice.invoice_summary
                    if hasattr(inv_summary, 'summary_normal') and inv_summary.summary_normal:
                        normal_summary = inv_summary.summary_normal
                        currency = summary.get('Currency', '')
                        summary['Net Amount'] = f"{getattr(normal_summary, 'invoice_net_amount', 'N/A')} {currency}"
                        summary['VAT Amount'] = f"{getattr(normal_summary, 'invoice_vat_amount', 'N/A')} {currency}"
                        
                        # Calculate gross amount (net + VAT)
                        net_amount = getattr(normal_summary, 'invoice_net_amount', 0)
                        vat_amount = getattr(normal_summary, 'invoice_vat_amount', 0)
                        if net_amount and vat_amount is not None:
                            gross_amount = net_amount + vat_amount
                            summary['Gross Amount'] = f"{gross_amount} {currency}"
                        
                        # VAT breakdown
                        if hasattr(normal_summary, 'summary_by_vat_rate') and normal_summary.summary_by_vat_rate:
                            vat_rates = normal_summary.summary_by_vat_rate
                            summary['VAT Rates Count'] = len(vat_rates)
                            
                            # Check first VAT rate details
                            if vat_rates:
                                first_vat = vat_rates[0]
                                if hasattr(first_vat, 'vat_rate') and first_vat.vat_rate:
                                    vat_rate = first_vat.vat_rate
                                    if hasattr(vat_rate, 'vat_domestic_reverse_charge') and vat_rate.vat_domestic_reverse_charge:
                                        summary['Domestic Reverse Charge'] = 'Yes'
                                    if hasattr(vat_rate, 'no_vat_charge') and vat_rate.no_vat_charge:
                                        summary['No VAT Charge'] = 'Yes'
                
            
    except Exception as e:
        logger.warning(f"Error extracting invoice summary: {e}")
        summary['Error'] = f"Failed to extract summary: {e}"
    
    return summary


def save_invoice_details(invoice_data, invoice_number, tax_number):
    """
    Save detailed invoice data to a JSON file for further analysis.
    
    Args:
        invoice_data: InvoiceData object from NAV API
        invoice_number: Invoice number for filename
        tax_number: Tax number for filename
    """
    try:
        # Create results directory
        results_dir = Path("test_results")
        results_dir.mkdir(exist_ok=True)
        
        # Generate filename
        safe_invoice_num = invoice_number.replace('/', '_')
        timestamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"invoice_detail_{tax_number}_{safe_invoice_num}_{timestamp}.json"
        filepath = results_dir / filename
        
        # Convert invoice data to dict (simplified representation)
        invoice_dict = {
            'type': str(type(invoice_data)),
            'attributes': []
        }
        
        # Extract all attributes from the invoice data object
        for attr_name in dir(invoice_data):
            if not attr_name.startswith('_'):
                try:
                    attr_value = getattr(invoice_data, attr_name)
                    # Convert to string representation for JSON serialization
                    invoice_dict['attributes'].append({
                        'name': attr_name,
                        'type': str(type(attr_value)),
                        'value': str(attr_value) if attr_value is not None else None
                    })
                except Exception as e:
                    invoice_dict['attributes'].append({
                        'name': attr_name,
                        'type': 'error',
                        'value': f"Error getting attribute: {e}"
                    })
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(invoice_dict, f, indent=2, ensure_ascii=False)
        
        logger.info(f"💾 Detailed invoice data saved to: {filepath}")
        
    except Exception as e:
        logger.warning(f"Failed to save invoice details: {e}")


def main():
    """Main test function."""
    # Test configuration
    INVOICE_NUMBER = "1001002131002/25"
    DIRECTION = InvoiceDirectionType.OUTBOUND
    ENVIRONMENT = NavEnvironment.PRODUCTION
    
    logger.info("Starting single invoice fetch test...")
    
    # Run the test
    result = test_single_invoice_fetch(
        credentials=DIEGO_PROD,
        invoice_number=INVOICE_NUMBER,
        invoice_direction=DIRECTION,
        environment=ENVIRONMENT
    )
    
    # Final summary
    logger.info("\n" + "=" * 80)
    logger.info("TEST RESULTS")
    logger.info("=" * 80)
    logger.info(f"Status: {result['status'].upper()}")
    
    if result['status'] == 'success':
        logger.info("🎉 Invoice fetched successfully!")
        logger.info(f"📊 Summary items: {len(result['summary'])}")
    else:
        logger.error(f"❌ Test failed: {result.get('error', 'Unknown error')}")
    
    # Save test results
    try:
        results_dir = Path("test_results")
        results_dir.mkdir(exist_ok=True)
        
        timestamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
        result_file = results_dir / f"single_invoice_test_result_{timestamp}.json"
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Test results saved to: {result_file}")
        
    except Exception as e:
        logger.warning(f"Failed to save test results: {e}")


if __name__ == "__main__":
    main()