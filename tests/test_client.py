"""
Tests for the main NAV client functionality.
"""

import pytest
import requests_mock
from datetime import datetime

from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.models import NavCredentials, InvoiceDirection, InvoiceDigest
from nav_online_szamla.exceptions import (
    NavValidationException,
    NavApiException,
    NavInvoiceNotFoundException,
)


class TestNavOnlineInvoiceClient:
    """Test cases for the NAV Online Invoice client."""

    def test_client_initialization_default(self):
        """Test client initialization with default settings."""
        client = NavOnlineInvoiceClient()

        assert (
            client.base_url == "https://api.onlineszamla.nav.gov.hu/invoiceService/v3/"
        )
        assert client.http_client is not None

    def test_client_initialization_custom_url(self):
        """Test client initialization with custom base URL."""
        custom_url = "https://test.api.onlineszamla.nav.gov.hu"
        client = NavOnlineInvoiceClient(base_url=custom_url)

        assert client.base_url == custom_url

    def test_client_initialization_custom_timeout(self):
        """Test client initialization with custom timeout."""
        client = NavOnlineInvoiceClient(timeout=60)

        # Timeout should be set properly for the http_client
        assert client.http_client is not None

    def test_token_exchange_success(self, sample_credentials):
        """Test successful token exchange."""
        client = NavOnlineInvoiceClient()

        with requests_mock.Mocker() as m:
            m.post(
                f"{client.base_url}tokenExchange",
                json={
                    "result": {
                        "funcCode": "OK",
                        "encodedExchangeToken": "encoded_token_123",
                    }
                },
            )

            token = client.get_token(sample_credentials)
            assert token == "encoded_token_123"

    def test_token_exchange_failure(self, sample_credentials):
        """Test token exchange failure."""
        client = NavOnlineInvoiceClient()

        with requests_mock.Mocker() as m:
            m.post(
                f"{client.base_url}tokenExchange",
                json={
                    "result": {
                        "funcCode": "ERROR",
                        "errorCode": "INVALID_CREDENTIALS",
                        "message": "Invalid authentication credentials",
                    }
                },
            )

            with pytest.raises(NavApiException, match="INVALID_CREDENTIALS"):
                client.get_token(sample_credentials)

    def test_query_invoice_digest_success(self, sample_credentials):
        """Test successful invoice digest query."""
        client = NavOnlineInvoiceClient()

        with requests_mock.Mocker() as m:
            # Mock token exchange
            m.post(
                f"{client.base_url}tokenExchange",
                json={
                    "result": {"funcCode": "OK", "encodedExchangeToken": "token_123"}
                },
            )

            # Mock query invoice digest
            m.post(
                f"{client.base_url}queryInvoiceDigest",
                text="""<?xml version="1.0" encoding="UTF-8"?>
                <QueryInvoiceDigestResponse>
                    <header>
                        <requestId>test-123</requestId>
                        <timestamp>2023-01-01T12:00:00Z</timestamp>
                        <requestVersion>3.0</requestVersion>
                        <headerVersion>1.0</headerVersion>
                    </header>
                    <result>
                        <funcCode>OK</funcCode>
                    </result>
                    <invoiceDigestResult>
                        <availableCount>1</availableCount>
                        <invoiceDigest>
                            <invoiceNumber>TEST001</invoiceNumber>
                            <invoiceDirection>OUTBOUND</invoiceDirection>
                            <batchIndex>1</batchIndex>
                            <invoiceOperation>CREATE</invoiceOperation>
                            <supplierTaxNumber>12345678</supplierTaxNumber>
                            <customerTaxNumber>87654321</customerTaxNumber>
                            <insDate>2023-01-01T10:00:00Z</insDate>
                            <completenessIndicator>true</completenessIndicator>
                            <originalRequestVersion>3.0</originalRequestVersion>
                        </invoiceDigest>
                    </invoiceDigestResult>
                </QueryInvoiceDigestResponse>""",
            )

            from nav_online_szamla.models import (
                QueryInvoiceDigestRequest,
                MandatoryQueryParams,
                InvoiceDirection,
                DateTimeRange,
                InvoiceQueryParams,
            )

            request = QueryInvoiceDigestRequest(
                page=1,
                invoice_direction=InvoiceDirection.OUTBOUND,
                invoice_query_params=InvoiceQueryParams(
                    mandatory_query_params=MandatoryQueryParams(
                        ins_date=DateTimeRange(
                            date_time_from="2023-01-01T00:00:00.000Z",
                            date_time_to="2023-01-31T23:59:59.999Z",
                        )
                    )
                ),
            )

            response = client.query_invoice_digest(sample_credentials, request)

            assert response.available_count == 1
            assert len(response.invoice_digests) == 1
            assert response.invoice_digests[0].invoice_number == "TEST001"
            assert (
                response.invoice_digests[0].invoice_direction
                == InvoiceDirection.OUTBOUND
            )

    def test_parse_invoice_digest_response_error(self, mock_error_response):
        """Test parsing of error response in invoice digest."""
        client = NavOnlineInvoiceClient()

        with pytest.raises(NavApiException, match="INVALID_CREDENTIALS"):
            client._parse_invoice_digest_response(mock_error_response)

    def test_parse_error_response(self, mock_error_response):
        """Test error response parsing."""
        client = NavOnlineInvoiceClient()

        error_info = client._parse_error_response(mock_error_response)

        assert error_info.error_code == "INVALID_CREDENTIALS"
        assert error_info.message == "Invalid authentication credentials"
        assert isinstance(error_info.timestamp, datetime)

    def test_get_invoice_detail_success(self, sample_credentials):
        """Test successful invoice detail retrieval."""
        client = NavOnlineInvoiceClient()

        with requests_mock.Mocker() as m:
            # Mock token exchange
            m.post(
                f"{client.base_url}tokenExchange",
                json={
                    "result": {"funcCode": "OK", "encodedExchangeToken": "token_123"}
                },
            )

            # Mock query invoice data
            m.post(
                f"{client.base_url}queryInvoiceData",
                text="""<?xml version="1.0" encoding="UTF-8"?>
                <QueryInvoiceDataResponse>
                    <header>
                        <requestId>test-123</requestId>
                        <timestamp>2023-01-01T12:00:00Z</timestamp>
                        <requestVersion>3.0</requestVersion>
                        <headerVersion>1.0</headerVersion>
                    </header>
                    <r>
                        <funcCode>OK</funcCode>
                    </r>
                    <invoiceDataResult>
                        <invoiceData>PGludm9pY2VEYXRhPjxpbnZvaWNlTnVtYmVyPlRFU1QwMDE8L2ludm9pY2VOdW1iZXI+PGludm9pY2VJc3N1ZURhdGU+MjAyMy0wMS0wMTwvaW52b2ljZUlzc3VlRGF0ZT48L2ludm9pY2VEYXRhPg==</invoiceData>
                    </invoiceDataResult>
                </QueryInvoiceDataResponse>""",
            )

            invoice_data = client.get_invoice_detail(
                sample_credentials, "TEST001", InvoiceDirection.OUTBOUND
            )

            assert invoice_data.invoice_number == "TEST001"
            assert invoice_data.issue_date is not None

    def test_query_invoice_check_success(self, sample_credentials):
        """Test successful invoice check query."""
        client = NavOnlineInvoiceClient()

        with requests_mock.Mocker() as m:
            # Mock token exchange
            m.post(
                f"{client.base_url}tokenExchange",
                json={
                    "result": {"funcCode": "OK", "encodedExchangeToken": "token_123"}
                },
            )

            # Mock query invoice check
            m.post(
                f"{client.base_url}queryInvoiceCheck",
                text="""<?xml version="1.0" encoding="UTF-8"?>
                <QueryInvoiceCheckResponse>
                    <header>
                        <requestId>test-123</requestId>
                        <timestamp>2023-01-01T12:00:00Z</timestamp>
                        <requestVersion>3.0</requestVersion>
                        <headerVersion>1.0</headerVersion>
                    </header>
                    <r>
                        <funcCode>OK</funcCode>
                    </r>
                    <invoiceCheckResult>
                        <queryResults>
                            <invoiceNumber>TEST001</invoiceNumber>
                            <batchIndex>1</batchIndex>
                            <invoiceDirection>OUTBOUND</invoiceDirection>
                            <queryResultCode>FOUND</queryResultCode>
                        </queryResults>
                    </invoiceCheckResult>
                </QueryInvoiceCheckResponse>""",
            )

            from nav_online_szamla.models import QueryInvoiceCheckRequest

            request = QueryInvoiceCheckRequest(
                invoice_number="TEST001",
                invoice_direction=InvoiceDirection.OUTBOUND,
                batch_index=1,
            )

            result = client.query_invoice_check(sample_credentials, request)

            # For now, just check that we get some result
            assert result is not None
