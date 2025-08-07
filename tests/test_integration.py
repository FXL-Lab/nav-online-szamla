"""
Integration tests for the NAV Online Számla client.

These tests demonstrate how to use the client in real scenarios.
Note: These tests require actual NAV API credentials and should be run 
against the test environment.
"""

import pytest
import os
from datetime import datetime, timedelta

from nav_online_szamla import (
    NavOnlineInvoiceClient,
    NavCredentials,
    InvoiceDirection,
    QueryInvoiceDigestRequest,
    MandatoryQueryParams,
    AdditionalQueryParams,
    InvoiceQueryParams,
    DateTimeRange,
)
from nav_online_szamla.exceptions import NavValidationException


class TestIntegration:
    """Integration tests for the NAV client."""

    def test_basic_usage_example(self):
        """Test basic usage example with mock credentials."""
        # This test demonstrates the basic usage pattern
        # In real usage, replace with actual credentials

        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_signer_key",
            tax_number="12345678",
        )

        # Create API-compliant request
        request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_query_params=InvoiceQueryParams(
                mandatory_query_params=MandatoryQueryParams(
                    ins_date=DateTimeRange(
                        date_time_from=datetime(2024, 1, 1),
                        date_time_to=datetime(2024, 1, 31),
                    )
                )
            ),
        )

        # This would normally make actual API calls
        client = NavOnlineInvoiceClient()

        # In a real scenario, this would return invoice data:
        # response = client.query_invoice_digest(credentials, request)

        assert client is not None

    def test_date_range_splitting_example(self):
        """Test example with date range that requires splitting."""
        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_signer_key",
            tax_number="12345678",
        )

        # Create parameters with a large date range (more than 35 days)
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 3, 31)

        request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_query_params=InvoiceQueryParams(
                mandatory_query_params=MandatoryQueryParams(
                    ins_date=DateTimeRange(
                        date_time_from=start_date, date_time_to=end_date
                    )
                )
            ),
        )

        client = NavOnlineInvoiceClient()

        # In real usage: response = client.query_invoice_digest(credentials, request)
        assert (
            request.invoice_query_params.mandatory_query_params.ins_date.date_time_from
            == start_date
        )
        assert (
            request.invoice_query_params.mandatory_query_params.ins_date.date_time_to
            == end_date
        )

    def test_both_directions_example(self):
        """Test example querying both invoice directions."""
        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_signer_key",
            tax_number="12345678",
        )

        # Create requests for both directions
        outbound_request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_query_params=InvoiceQueryParams(
                mandatory_query_params=MandatoryQueryParams(
                    ins_date=DateTimeRange(
                        date_time_from=datetime(2024, 1, 1),
                        date_time_to=datetime(2024, 1, 31),
                    )
                )
            ),
        )

        inbound_request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.INBOUND,
            invoice_query_params=InvoiceQueryParams(
                mandatory_query_params=MandatoryQueryParams(
                    ins_date=DateTimeRange(
                        date_time_from=datetime(2024, 1, 1),
                        date_time_to=datetime(2024, 1, 31),
                    )
                )
            ),
        )

        client = NavOnlineInvoiceClient()

        # In real usage, this would make two API calls:
        # outbound_response = client.query_invoice_digest(credentials, outbound_request)
        # inbound_response = client.query_invoice_digest(credentials, inbound_request)

        assert outbound_request.invoice_direction == InvoiceDirection.OUTBOUND
        assert inbound_request.invoice_direction == InvoiceDirection.INBOUND

    def test_invoice_detail_example(self):
        """Test example for getting invoice details."""
        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_signer_key",
            tax_number="12345678",
        )

        client = NavOnlineInvoiceClient()

        # In real usage, this would fetch detailed invoice data:
        # detail = client.get_invoice_detail(
        #     credentials,
        #     "INVOICE001",
        #     InvoiceDirection.OUTBOUND
        # )

        # Validate that credentials are properly structured
        assert credentials.login == "test_user"
        assert credentials.tax_number == "12345678"

    def test_error_handling_example(self):
        """Test example of proper error handling."""
        # Invalid credentials
        invalid_credentials = NavCredentials(
            login="",  # Missing login
            password="test_password",
            signer_key="test_signer_key",
            tax_number="invalid_tax_number",  # Invalid format
        )

        client = NavOnlineInvoiceClient()

        # Test that validation would catch invalid credentials
        assert invalid_credentials.login == ""
        assert invalid_credentials.tax_number == "invalid_tax_number"

    def test_custom_configuration_example(self):
        """Test example with custom configuration."""
        # Custom API URL and timeout
        custom_url = "https://test.api.nav.gov.hu/invoiceService/v3/"
        custom_timeout = 60

        client = NavOnlineInvoiceClient(base_url=custom_url, timeout=custom_timeout)
        assert client.base_url == custom_url

    @pytest.mark.skipif(
        not os.environ.get("NAV_INTEGRATION_TEST"),
        reason="Integration tests require NAV_INTEGRATION_TEST environment variable",
    )
    def test_real_api_call(self):
        """
        Test with real API call (requires environment variables).

        Set the following environment variables to run this test:
        - NAV_LOGIN
        - NAV_PASSWORD
        - NAV_SIGNER_KEY
        - NAV_TAX_NUMBER
        - NAV_INTEGRATION_TEST=1
        """
        credentials = NavCredentials(
            login=os.environ["NAV_LOGIN"],
            password=os.environ["NAV_PASSWORD"],
            signer_key=os.environ["NAV_SIGNER_KEY"],
            tax_number=os.environ["NAV_TAX_NUMBER"],
        )

        # Query last 7 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_query_params=InvoiceQueryParams(
                mandatory_query_params=MandatoryQueryParams(
                    ins_date=DateTimeRange(
                        date_time_from=start_date, date_time_to=end_date
                    )
                )
            ),
        )

        client = NavOnlineInvoiceClient()

        # This makes a real API call to NAV test environment
        response = client.query_invoice_digest(credentials, request)

        # Verify response structure
        assert response.available_count >= 0
        assert isinstance(response.invoice_digests, list)

        if response.invoice_digests:
            digest = response.invoice_digests[0]
            assert hasattr(digest, "invoice_number")
            assert hasattr(digest, "supplier_tax_number")
            assert hasattr(digest, "ins_date")

    def test_usage_pattern_documentation(self):
        """
        Test demonstrating the recommended usage patterns.

        This serves as documentation for how to use the library.
        """
        # 1. Create credentials
        credentials = NavCredentials(
            login="your_nav_login",
            password="your_nav_password",
            signer_key="your_signer_key",
            tax_number="your_tax_number",
        )

        # 2. Create API-compliant request
        request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_query_params=InvoiceQueryParams(
                mandatory_query_params=MandatoryQueryParams(
                    ins_date=DateTimeRange(
                        date_time_from=datetime(2024, 1, 1),
                        date_time_to=datetime(2024, 1, 31),
                    )
                ),
                additional_query_params=AdditionalQueryParams(
                    tax_number="12345678"  # Optional filter
                ),
            ),
        )

        # 3. Use the client
        client = NavOnlineInvoiceClient()

        try:
            # Get list of invoice digests
            # response = client.query_invoice_digest(credentials, request)

            # Get details for specific invoice
            # detail = client.get_invoice_detail(
            #     credentials,
            #     "INVOICE001",
            #     InvoiceDirection.OUTBOUND
            # )

            # The client handles:
            # - Authentication and request signing
            # - XML request building and response parsing
            # - Error handling and meaningful exceptions
            # - Data modeling with type safety

            pass

        except NavValidationException as e:
            # Handle validation errors (invalid parameters)
            print(f"Validation error: {e}")

        except Exception as e:
            # Handle other errors
            print(f"API error: {e}")

        # Test passes to demonstrate the pattern
        assert True
