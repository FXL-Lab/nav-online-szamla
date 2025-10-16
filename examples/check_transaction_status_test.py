#!/usr/bin/env python3
"""
Simple test to check transaction status for a specific transaction ID.
This script queries the NAV API for transaction status and prints all results.
"""

import logging
import sys
import os

# Add parent directory to path to import nav_online_szamla
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.config import NavEnvironment
from nav_online_szamla.models_legacy import NavCredentials
from creds import FXL_DEV

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Check transaction status and print all results."""
    
    # Transaction ID to check
    transaction_id = "55EYEPG10L03TXW1"
    
    logger.info("============================================================")
    logger.info("NAV Online Számla API - Transaction Status Check")
    logger.info("============================================================")
    logger.info(f"Checking transaction ID: {transaction_id}")
    
    try:
        # Get credentials
        credentials = FXL_DEV
        logger.info(f"Using credentials for tax number: {credentials.tax_number}")
        
        # Initialize client
        environment = NavEnvironment.TEST
        
        client = NavOnlineInvoiceClient(
            credentials=credentials,
            environment=environment
        )
        
        # Query transaction status
        logger.info(f"Querying transaction status for: {transaction_id}")
        response = client.query_transaction_status(transaction_id)
        
        # Print response details
        logger.info("============================================================")
        logger.info("TRANSACTION STATUS RESPONSE")
        logger.info("============================================================")
        
        if hasattr(response, 'header'):
            logger.info(f"Request ID: {response.header.request_id}")
            logger.info(f"Timestamp: {response.header.timestamp}")
            logger.info(f"Request Version: {response.header.request_version}")
        
        if hasattr(response, 'result'):
            result = response.result
            if hasattr(result, 'func_code'):
                logger.info(f"Function Code: {result.func_code}")
            if hasattr(result, 'message'):
                logger.info(f"Result Message: {result.message}")
            if hasattr(result, 'error_code'):
                logger.info(f"Error Code: {result.error_code}")
        
        # Check if processing results are available directly on the response
        if hasattr(response, 'processing_results') and response.processing_results:
            processing_results = response.processing_results
            logger.info("============================================================")
            logger.info("PROCESSING RESULTS")
            logger.info("============================================================")
            
            # Try to get the processing result list
            if hasattr(processing_results, 'processing_result'):
                results_list = processing_results.processing_result
                if isinstance(results_list, list):
                    logger.info(f"Number of processing results: {len(results_list)}")
                    for i, processing_result in enumerate(results_list):
                        logger.info(f"\n--- Result {i + 1} ---")
                        logger.info(f"Index: {processing_result.index}")
                        logger.info(f"Invoice Status: {processing_result.invoice_status}")
                        logger.info(f"Invoice Status Type: {type(processing_result.invoice_status)}")
                        
                        if hasattr(processing_result, 'business_validation_messages') and processing_result.business_validation_messages:
                            logger.info("Business Validation Messages:")
                            for msg in processing_result.business_validation_messages:
                                logger.info(f"  - Code: {msg.validation_result_code}")
                                logger.info(f"    Error Code: {msg.validation_error_code}")
                                logger.info(f"    Message: {msg.message}")
                                if hasattr(msg, 'pointer') and msg.pointer:
                                    logger.info(f"    Pointer Tag: {msg.pointer.tag}")
                                    logger.info(f"    Pointer Value: {msg.pointer.value}")
                        
                        if hasattr(processing_result, 'technical_validation_messages') and processing_result.technical_validation_messages:
                            logger.info("Technical Validation Messages:")
                            for msg in processing_result.technical_validation_messages:
                                logger.info(f"  - Code: {msg.validation_result_code}")
                                logger.info(f"    Error Code: {msg.validation_error_code}")
                                logger.info(f"    Message: {msg.message}")
                else:
                    # Single result case
                    logger.info("Single processing result:")
                    logger.info(f"Index: {results_list.index}")
                    logger.info(f"Invoice Status: {results_list.invoice_status}")
                    logger.info(f"Invoice Status Type: {type(results_list.invoice_status)}")
            else:
                # Try to iterate directly
                logger.info("Processing results structure:")
                logger.info(f"Type: {type(processing_results)}")
                logger.info(f"Attributes: {dir(processing_results)}")
                try:
                    # Try to iterate directly
                    results_count = 0
                    for i, processing_result in enumerate(processing_results):
                        results_count += 1
                        logger.info(f"\n--- Result {i + 1} ---")
                        logger.info(f"Index: {processing_result.index}")
                        logger.info(f"Invoice Status: {processing_result.invoice_status}")
                        logger.info(f"Invoice Status Type: {type(processing_result.invoice_status)}")
                    logger.info(f"Total processing results: {results_count}")
                except Exception as e:
                    logger.error(f"Could not iterate processing results: {e}")
        else:
            logger.info("No processing results found in the response")
            
        # Also check software info if available
        if hasattr(response, 'software'):
            logger.info("============================================================")
            logger.info("SOFTWARE INFO")
            logger.info("============================================================")
            logger.info(f"Software ID: {response.software.software_id}")
            logger.info(f"Software Name: {response.software.software_name}")
            if hasattr(response.software, 'software_version'):
                logger.info(f"Software Version: {response.software.software_version}")
            elif hasattr(response.software, 'version'):
                logger.info(f"Software Version: {response.software.version}")
        
        # Create a summary
        success_count = 0
        failed_count = 0
        if hasattr(response, 'processing_results') and response.processing_results:
            processing_results = response.processing_results
            if hasattr(processing_results, 'processing_result'):
                results_list = processing_results.processing_result
                for result in results_list:
                    if hasattr(result, 'invoice_status'):
                        if result.invoice_status.name == 'DONE':
                            success_count += 1
                        elif result.invoice_status.name == 'ABORTED':
                            failed_count += 1
        
        logger.info("============================================================")
        logger.info("SUMMARY")
        logger.info("============================================================")
        logger.info(f"Transaction ID: {transaction_id}")
        logger.info(f"Total Results: {success_count + failed_count}")
        logger.info(f"✓ Successful: {success_count}")
        logger.info(f"✗ Failed: {failed_count}")
        logger.info(f"Status: {'COMPLETED' if failed_count == 0 else 'COMPLETED WITH ERRORS'}")
        
        logger.info("\n============================================================")
        logger.info("Test result: ✓ PASSED")
        logger.info("🎉 Transaction status check completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Test failed with error: {str(e)}")
        logger.exception("Full error details:")
        sys.exit(1)

if __name__ == "__main__":
    main()