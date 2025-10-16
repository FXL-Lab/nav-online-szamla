#!/usr/bin/env python3
"""
Simple NAV Invoice Submission Test Script

Submits invoices from an Excel file using process_excel_to_nav_results.
"""
import logging
from pathlib import Path
from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.config import NavEnvironment
from nav_online_szamla.exceptions import NavApiException, NavValidationException
from creds import CREDENTIALS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_invoice_submission(credentials, environment=NavEnvironment.TEST):
    """Test invoice submission from Excel file."""
    # Path to your existing Excel file with invoices
    input_excel_file = "invoice_submission_sample.xlsx"  # Update path if needed
    output_excel_file = "test_results/invoice_submission_results.xlsx"

    # Ensure output directory exists
    Path("test_results").mkdir(exist_ok=True)

    try:
        logger.info(f"Submitting invoices from Excel: {input_excel_file}")
        with NavOnlineInvoiceClient(credentials, environment=environment) as client:
            result_file = client.process_excel_to_nav_results(
                input_excel_file=input_excel_file,
                output_excel_file=output_excel_file,
                max_invoices_per_batch=100,
                polling_interval_seconds=3,
                max_polling_attempts=10
            )
        logger.info(f"✓ Invoice submission completed. Results saved to: {result_file}")
        return True
    except (NavApiException, NavValidationException) as e:
        logger.error(f"✗ NAV error: {e}")
        return False
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}")
        return False


def main():
    logger.info("=" * 60)
    logger.info("NAV Online Számla API - Invoice Submission Test")
    logger.info("=" * 60)
    logger.info(f"Using credentials for tax number: {CREDENTIALS['fxl_dev'].tax_number}")
    success = test_invoice_submission(CREDENTIALS['fxl_dev'], NavEnvironment.TEST)
    logger.info("=" * 60)
    logger.info(f"Test result: {'✓ PASSED' if success else '✗ FAILED'}")
    if success:
        logger.info("🎉 Invoice submission test passed!")
    else:
        logger.warning("⚠️  Invoice submission test failed.")

if __name__ == "__main__":
    main()
