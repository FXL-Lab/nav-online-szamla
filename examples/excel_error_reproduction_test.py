#!/usr/bin/env python3
"""
Excel Export Error Reproduction Test

Test script to reproduce the Excel export error with Diego's specific invoice.
This will help us identify and fix the gross amount mapping issue.
"""
import datetime as dt
import logging
from pathlib import Path

# NAV imports
from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.config import NavEnvironment
from nav_online_szamla.models import InvoiceDirectionType
from nav_online_szamla.exceptions import NavApiException, NavValidationException, NavInvoiceNotFoundException

# Import credentials
from creds import DIEGO_PROD

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Changed to INFO level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def reproduce_excel_export_error():
    """
    Reproduce the Excel export error with Diego's specific invoice date range.
    """
    logger.info("=" * 80)
    logger.info("EXCEL EXPORT ERROR REPRODUCTION TEST")
    logger.info("=" * 80)
    
    # Use the exact date when the problematic invoice was issued
    invoice_date = "2025-07-23"  # From our previous test, we know this is the issue date
    start_date = dt.datetime.strptime(invoice_date, '%Y-%m-%d')
    end_date = start_date + dt.timedelta(days=1)  # Next day to ensure we get the invoice
    
    logger.info(f"Testing date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    logger.info(f"Expected to find invoice: 1001002131002/25")
    
    try:
        # Create results directory
        results_dir = Path("test_results")
        results_dir.mkdir(exist_ok=True)
        
        # Generate output file path
        timestamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = results_dir / f"error_reproduction_{timestamp}.xlsx"
        
        logger.info(f"Output file: {output_file}")
        
        with NavOnlineInvoiceClient(DIEGO_PROD, environment=NavEnvironment.PRODUCTION) as client:
            logger.info("🔌 Connected to NAV API")
            
            # Try to export the problematic date range to Excel
            logger.info("📄 Starting Excel export (this should reproduce the error)...")
            
            total_exported = client.export_invoices_to_excel_streaming(
                start_date=start_date,
                end_date=end_date,
                output_file=str(output_file),
                invoice_direction=InvoiceDirectionType.OUTBOUND,
                use_threading=True,  # Enable threading with 4 workers
                max_workers=4
            )
            
            logger.info(f"✅ Export completed successfully: {total_exported} invoices")
            
            if output_file.exists():
                file_size = output_file.stat().st_size
                logger.info(f"📁 File created: {file_size} bytes")
            
            return True
            
    except Exception as e:
        logger.error(f"❌ Export failed with error: {e}")
        logger.error(f"Error type: {type(e)}")
        
        # Print full traceback for debugging
        import traceback
        logger.error("Full traceback:")
        logger.error(traceback.format_exc())
        
        return False


def test_manual_invoice_data_structure():
    """
    Manually fetch the problematic invoice and examine its structure.
    This will help us understand what's missing in the invoice summary.
    """
    logger.info("\n" + "=" * 80)
    logger.info("MANUAL INVOICE STRUCTURE ANALYSIS")
    logger.info("=" * 80)
    
    try:
        with NavOnlineInvoiceClient(DIEGO_PROD, environment=NavEnvironment.PRODUCTION) as client:
            logger.info("🔍 Fetching the problematic invoice...")
            
            invoice_data = client.get_invoice_data(
                invoice_number="1001002131002/25",
                invoice_direction=InvoiceDirectionType.OUTBOUND
            )
            
            logger.info("✅ Invoice fetched successfully")
            
            # Examine the invoice summary structure
            logger.info("\n📋 ANALYZING INVOICE SUMMARY STRUCTURE:")
            
            if hasattr(invoice_data, 'invoice_main') and invoice_data.invoice_main:
                invoice_main = invoice_data.invoice_main
                logger.info(f"✓ invoice_main exists: {type(invoice_main)}")
                
                if hasattr(invoice_main, 'invoice') and invoice_main.invoice:
                    invoice = invoice_main.invoice
                    logger.info(f"✓ invoice exists: {type(invoice)}")
                    
                    if hasattr(invoice, 'invoice_summary') and invoice.invoice_summary:
                        summary = invoice.invoice_summary
                        logger.info(f"✓ invoice_summary exists: {type(summary)}")
                        
                        # Check what's in the summary
                        logger.info("📋 Invoice summary attributes:")
                        for attr in dir(summary):
                            if not attr.startswith('_'):
                                try:
                                    value = getattr(summary, attr)
                                    logger.info(f"  - {attr}: {type(value)} = {value}")
                                except Exception as e:
                                    logger.info(f"  - {attr}: Error getting value - {e}")
                        
                        # Check summary_normal specifically
                        if hasattr(summary, 'summary_normal') and summary.summary_normal:
                            normal = summary.summary_normal
                            logger.info(f"\n✓ summary_normal exists: {type(normal)}")
                            
                            logger.info("📋 Summary normal attributes:")
                            for attr in dir(normal):
                                if not attr.startswith('_'):
                                    try:
                                        value = getattr(normal, attr)
                                        logger.info(f"  - {attr}: {type(value)} = {value}")
                                    except Exception as e:
                                        logger.info(f"  - {attr}: Error getting value - {e}")
                            
                            # Specifically check for gross amount fields
                            logger.info("\n🔍 CHECKING FOR GROSS AMOUNT FIELDS:")
                            logger.info(f"  - hasattr(normal, 'invoice_gross_amount'): {hasattr(normal, 'invoice_gross_amount')}")
                            logger.info(f"  - hasattr(normal, 'invoice_gross_amount_huf'): {hasattr(normal, 'invoice_gross_amount_huf')}")
                            
                            if hasattr(normal, 'invoice_gross_amount'):
                                logger.info(f"  - invoice_gross_amount: {getattr(normal, 'invoice_gross_amount', 'N/A')}")
                            if hasattr(normal, 'invoice_gross_amount_huf'):
                                logger.info(f"  - invoice_gross_amount_huf: {getattr(normal, 'invoice_gross_amount_huf', 'N/A')}")
                        else:
                            logger.warning("❌ summary_normal is None or missing")
                    else:
                        logger.warning("❌ invoice_summary is None or missing")
                else:
                    logger.warning("❌ invoice is None or missing")
            else:
                logger.warning("❌ invoice_main is None or missing")
                
            return True
            
    except Exception as e:
        logger.error(f"❌ Analysis failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def main():
    """Main test function."""
    logger.info("Starting Excel export error reproduction...")
    
    # First, analyze the invoice structure manually
    logger.info("Step 1: Analyzing invoice data structure...")
    structure_ok = test_manual_invoice_data_structure()
    
    if not structure_ok:
        logger.error("❌ Failed to analyze invoice structure. Stopping.")
        return
    
    # Then try to reproduce the Excel export error
    logger.info("\nStep 2: Attempting to reproduce Excel export error...")
    export_ok = reproduce_excel_export_error()
    
    # Summary
    logger.info("\n" + "=" * 80)
    logger.info("TEST SUMMARY")
    logger.info("=" * 80)
    logger.info(f"Structure analysis: {'✓ PASSED' if structure_ok else '✗ FAILED'}")
    logger.info(f"Excel export test: {'✓ PASSED' if export_ok else '✗ FAILED (ERROR REPRODUCED)'}")
    
    if not export_ok:
        logger.info("🎯 Error successfully reproduced! Now we can fix the issue.")
    else:
        logger.info("🤔 Error not reproduced. The issue might be fixed already.")


if __name__ == "__main__":
    main()