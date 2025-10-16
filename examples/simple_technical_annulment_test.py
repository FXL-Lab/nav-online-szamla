#!/usr/bin/env python3
"""
Simple NAV Technical Annulment Test Script

Submits technical annulments from an Excel file using process_excel_to_nav_annulment_results.
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


def test_technical_annulment(credentials, environment=NavEnvironment.TEST):
    """Test technical annulment from Excel file."""
    # Path to your existing Excel file with annulment data
    input_excel_file = "technical_annulment_sample.xlsx"  # Update path if needed
    output_excel_file = "test_results/technical_annulment_results.xlsx"

    # Ensure output directory exists
    Path("test_results").mkdir(exist_ok=True)

    try:
        logger.info(f"Submitting technical annulments from Excel: {input_excel_file}")
        with NavOnlineInvoiceClient(credentials, environment=environment) as client:
            result_file = client.process_excel_to_nav_annulment_results(
                input_excel_file=input_excel_file,
                output_excel_file=output_excel_file,
                max_annulments_per_batch=50,
                polling_interval_seconds=3,
                max_polling_attempts=10
            )
        logger.info(f"✓ Technical annulment completed. Results saved to: {result_file}")
        return True
    except (NavApiException, NavValidationException) as e:
        logger.error(f"✗ NAV error: {e}")
        return False
    except FileNotFoundError as e:
        logger.error(f"✗ File not found: {e}")
        logger.info("Please create a technical_annulment_sample.xlsx file with the following columns:")
        logger.info("  - 'érvénytelenítési hivatkozás': Invoice reference to annul")
        logger.info("  - 'érvénytelenítési kód': Annulment code (ERRATIC, CANCEL, etc.)")
        logger.info("  - 'érvénytelenítési ok': Reason for annulment")
        return False
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}")
        return False


def main():
    logger.info("=" * 60)
    logger.info("NAV Online Számla API - Technical Annulment Test")
    logger.info("=" * 60)
    logger.info(f"Using credentials for tax number: {CREDENTIALS['fxl_dev'].tax_number}")
    
    logger.info("\nExpected Excel format:")
    logger.info("Columns required:")
    logger.info("  1. 'érvénytelenítési hivatkozás' - Invoice reference to annul")
    logger.info("  2. 'érvénytelenítési kód' - Annulment code (ERRATIC, CANCEL, STORNO)")
    logger.info("  3. 'érvénytelenítési ok' - Reason for annulment")
    logger.info("")
    
    success = test_technical_annulment(CREDENTIALS['fxl_dev'], NavEnvironment.TEST)
    logger.info("=" * 60)
    logger.info(f"Test result: {'✓ PASSED' if success else '✗ FAILED'}")
    if success:
        logger.info("🎉 Technical annulment test passed!")
    else:
        logger.warning("⚠️  Technical annulment test failed.")

if __name__ == "__main__":
    main()