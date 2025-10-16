#!/usr/bin/env python3
"""
Simple NAV Invoice Query Test Script

A simplified version of the celery NAV invoice query script for testing purposes.
Uses the updated NavCredentials from creds.py.
"""
import datetime as dt
import logging
from pathlib import Path

# NAV imports
from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.config import NavEnvironment
from nav_online_szamla.models import InvoiceDirectionType
from nav_online_szamla.exceptions import NavApiException, NavValidationException

# Import credentials
from creds import CREDENTIALS, FXL_DEV, FXL_PROD, DEFAULT_CREDENTIALS

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_nav_connection(credentials, environment=NavEnvironment.TEST):
    """Test basic NAV API connection."""
    try:
        logger.info(f"Testing NAV connection with environment: {environment.value}")
        
        with NavOnlineInvoiceClient(credentials, environment=environment) as client:
            # Test token exchange to verify connection
            token_response = client.get_token()
            logger.info("✓ Token exchange successful")
            
            # Test exchange token decoding
            exchange_token = client.get_exchange_token()
            logger.info(f"✓ Exchange token obtained: {exchange_token[:20]}...")
            
            return True
            
    except NavApiException as e:
        logger.error(f"✗ NAV API error: {e}")
        return False
    except NavValidationException as e:
        logger.error(f"✗ NAV validation error: {e}")
        return False
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}")
        return False


def test_invoice_query(credentials, environment=NavEnvironment.TEST, max_results=5):
    """Test invoice query functionality."""
    try:
        logger.info(f"Testing invoice query with environment: {environment.value}")
        
        # Use a recent date range (last 30 days)
        end_date = dt.datetime(2025,10,1)
        start_date = dt.datetime(2025,10,1)
        
        logger.info(f"Querying invoices from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        
        with NavOnlineInvoiceClient(credentials, environment=environment) as client:
            # Test OUTBOUND invoice query
            logger.info("Testing OUTBOUND invoice query...")
            outbound_invoices = client.get_all_invoice_data_for_date_range(
                start_date=start_date,
                end_date=end_date,
                invoice_direction=InvoiceDirectionType.OUTBOUND,
                use_threading=False  # Disable threading for simple test
            )
            
            logger.info(f"✓ Found {len(outbound_invoices)} OUTBOUND invoices")
            
            # Show first few invoices (if any)
            for i, (invoice_data, operation) in enumerate(outbound_invoices[:max_results]):
                invoice_number = "N/A"
                if hasattr(invoice_data, 'invoice_reference') and invoice_data.invoice_reference:
                    invoice_number = invoice_data.invoice_reference.invoice_number
                elif hasattr(invoice_data, 'invoice_head') and invoice_data.invoice_head:
                    invoice_number = invoice_data.invoice_head.inv_number
                logger.info(f"  - Invoice {i+1}: {invoice_number}")
            
            # Test INBOUND invoice query
            logger.info("Testing INBOUND invoice query...")
            inbound_invoices = client.get_all_invoice_data_for_date_range(
                start_date=start_date,
                end_date=end_date,
                invoice_direction=InvoiceDirectionType.INBOUND,
                use_threading=False  # Disable threading for simple test
            )
            
            logger.info(f"✓ Found {len(inbound_invoices)} INBOUND invoices")
            
            # Show first few invoices (if any)
            for i, (invoice_data, operation) in enumerate(inbound_invoices[:max_results]):
                invoice_number = "N/A"
                if hasattr(invoice_data, 'invoice_reference') and invoice_data.invoice_reference:
                    invoice_number = invoice_data.invoice_reference.invoice_number
                elif hasattr(invoice_data, 'invoice_head') and invoice_data.invoice_head:
                    invoice_number = invoice_data.invoice_head.inv_number
                logger.info(f"  - Invoice {i+1}: {invoice_number}")
            
            return True
            
    except NavApiException as e:
        logger.error(f"✗ NAV API error: {e}")
        return False
    except NavValidationException as e:
        logger.error(f"✗ NAV validation error: {e}")
        return False
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}")
        return False


def test_excel_export(credentials, environment=NavEnvironment.TEST):
    """Test Excel export functionality."""
    try:
        logger.info("Testing Excel export functionality...")
        
        # Create output directory
        output_dir = Path("test_results")
        output_dir.mkdir(exist_ok=True)
        
        # Use a small date range for testing
        end_date = dt.datetime(2025,10,1)
        start_date = dt.datetime(2025,10,1)
        
        
        # Generate output file path
        timestamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = output_dir / f"test_nav_export_{timestamp}.xlsx"
        
        logger.info(f"Exporting to: {output_file}")
        
        with NavOnlineInvoiceClient(credentials, environment=environment) as client:
            # Test streaming Excel export
            total_exported = client.export_invoices_to_excel_streaming(
                start_date=start_date,
                end_date=end_date,
                output_file=str(output_file),
                invoice_direction=InvoiceDirectionType.OUTBOUND,
                use_threading=False,  # Disable threading for simple test
                max_workers=1
            )
            
            logger.info(f"✓ Exported {total_exported} invoices to Excel")
            
            if output_file.exists():
                file_size = output_file.stat().st_size
                logger.info(f"✓ File created successfully: {file_size} bytes")
                return True
            else:
                logger.error("✗ Output file was not created")
                return False
                
    except NavApiException as e:
        logger.error(f"✗ NAV API error: {e}")
        return False
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}")
        return False


def main():
    """Main test function."""
    logger.info("=" * 60)
    logger.info("NAV Online Számla API - Simple Test")
    logger.info("=" * 60)
    
    # Test with development credentials first
    logger.info(f"Using credentials for tax number: {CREDENTIALS['fxl_dev'].tax_number}")
    
    # Test 1: Connection test
    logger.info("\n1. Testing NAV API connection...")
    connection_ok = test_nav_connection(CREDENTIALS['fxl_dev'], NavEnvironment.TEST)
    
    if not connection_ok:
        logger.error("Connection test failed. Stopping here.")
        return
    
    # Test 2: Invoice query test
    logger.info("\n2. Testing invoice query...")
    query_ok = test_invoice_query(CREDENTIALS['fxl_dev'], NavEnvironment.TEST, max_results=3)
    
    # Test 3: Excel export test
    logger.info("\n3. Testing Excel export...")
    export_ok = test_excel_export(CREDENTIALS['fxl_dev'], NavEnvironment.TEST)
    
    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("TEST SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Connection test: {'✓ PASSED' if connection_ok else '✗ FAILED'}")
    logger.info(f"Invoice query test: {'✓ PASSED' if query_ok else '✗ FAILED'}")
    # logger.info(f"Excel export test: {'✓ PASSED' if export_ok else '✗ FAILED'}")
    
    if all([connection_ok, query_ok]):
        logger.info("🎉 All tests passed!")
    else:
        logger.warning("⚠️  Some tests failed. Check the logs above.")


if __name__ == "__main__":
    main()