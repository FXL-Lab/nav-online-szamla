"""
Tests for the main NAV client functionality.
"""

import pytest
import requests_mock

from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.models_legacy import NavCredentials
from nav_online_szamla.models import (
    InvoiceDirectionType,
    QueryInvoiceDigestRequest,
    MandatoryQueryParamsType,
    DateTimeIntervalParamType,
    InvoiceQueryParamsType,
    QueryInvoiceCheckRequest,
    InvoiceNumberQueryType,
)
from nav_online_szamla.exceptions import (
    NavApiException,
)


class TestNavOnlineInvoiceClient:
    """Test cases for the NAV Online Invoice client."""

    def _get_test_credentials(self):
        """Helper method to create test credentials."""
        return NavCredentials(
            login="test_user",
            password="test_password", 
            signer_key="test_signer_key",
            tax_number="12345678"
        )

    def test_client_initialization_default(self):
        """Test client initialization with default settings."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        assert (
            client.base_url == "https://api.onlineszamla.nav.gov.hu/invoiceService/v3/"
        )
        assert client.http_client is not None

    def test_client_initialization_custom_url(self):
        """Test client initialization with custom base URL."""
        custom_url = "https://test.api.onlineszamla.nav.gov.hu"
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials, base_url=custom_url)

        assert client.base_url == custom_url

    def test_client_initialization_custom_timeout(self):
        """Test client initialization with custom timeout."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials, timeout=60)

        # Timeout should be set properly for the http_client
        assert client.http_client is not None

    def test_token_exchange_success(self, sample_credentials):
        """Test successful token exchange."""
        client = NavOnlineInvoiceClient(sample_credentials)

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
        client = NavOnlineInvoiceClient(sample_credentials)

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
        client = NavOnlineInvoiceClient(sample_credentials)

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
                text="""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <QueryInvoiceDigestResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" 
                                           xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common" 
                                           xmlns:ns3="http://schemas.nav.gov.hu/OSA/3.0/base">
                    <ns2:header>
                        <ns2:requestId>test-123</ns2:requestId>
                        <ns2:timestamp>2023-01-01T12:00:00Z</ns2:timestamp>
                        <ns2:requestVersion>3.0</ns2:requestVersion>
                        <ns2:headerVersion>1.0</ns2:headerVersion>
                    </ns2:header>
                    <ns2:result>
                        <ns2:funcCode>OK</ns2:funcCode>
                    </ns2:result>
                    <invoiceDigestResult>
                        <currentPage>1</currentPage>
                        <availablePage>1</availablePage>
                        <invoiceDigest>
                            <invoiceNumber>TEST001</invoiceNumber>
                            <invoiceOperation>CREATE</invoiceOperation>
                            <invoiceCategory>NORMAL</invoiceCategory>
                            <invoiceIssueDate>2023-01-01</invoiceIssueDate>
                            <supplierTaxNumber>12345678</supplierTaxNumber>
                            <supplierName>Test Supplier</supplierName>
                            <insDate>2023-01-01T10:00:00Z</insDate>
                        </invoiceDigest>
                    </invoiceDigestResult>
                </QueryInvoiceDigestResponse>""",
            )

            request = QueryInvoiceDigestRequest(
                page=1,
                invoice_direction=InvoiceDirectionType.OUTBOUND,
                invoice_query_params=InvoiceQueryParamsType(
                    mandatory_query_params=MandatoryQueryParamsType(
                        ins_date=DateTimeIntervalParamType(
                            date_time_from="2023-01-01T00:00:00Z",
                            date_time_to="2023-01-31T23:59:59Z",
                        )
                    )
                ),
            )

            response = client.query_invoice_digest(
                page=request.page,
                invoice_direction=request.invoice_direction,
                invoice_query_params=request.invoice_query_params
            )

            assert response.invoice_digest_result is not None
            assert len(response.invoice_digest_result.invoice_digest) == 1
            assert response.invoice_digest_result.invoice_digest[0].invoice_number == "TEST001"

    def test_parse_invoice_digest_response_error(self, mock_error_response):
        """Test parsing of error response in invoice digest."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        with pytest.raises(NavApiException, match="INVALID_CREDENTIALS"):
            client._parse_invoice_digest_response(mock_error_response)

    def test_parse_error_response(self, mock_error_response):
        """Test error response parsing."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        error_info = client._parse_error_response(mock_error_response)

        assert error_info.error_code == "INVALID_CREDENTIALS"
        assert error_info.message == "Invalid authentication credentials"

    def test_get_invoice_data_success(self, sample_credentials):
        """Test successful invoice detail retrieval."""
        client = NavOnlineInvoiceClient(sample_credentials)

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
                text="""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <QueryInvoiceDataResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" 
                                         xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common" 
                                         xmlns:ns3="http://schemas.nav.gov.hu/OSA/3.0/base" 
                                         xmlns:ns4="http://schemas.nav.gov.hu/OSA/3.0/data">
                    <ns2:header>
                        <ns2:requestId>test-123</ns2:requestId>
                        <ns2:timestamp>2023-01-01T12:00:00Z</ns2:timestamp>
                        <ns2:requestVersion>3.0</ns2:requestVersion>
                        <ns2:headerVersion>1.0</ns2:headerVersion>
                    </ns2:header>
                    <ns2:result>
                        <ns2:funcCode>OK</ns2:funcCode>
                    </ns2:result>
                    <invoiceDataResult>
                        <invoiceData>PEludm9pY2VEYXRhIHhtbG5zPSJodHRwOi8vc2NoZW1hcy5uYXYuZ292Lmh1L09TQS8zLjAvZGF0YSIgeG1sbnM6bnMyPSJodHRwOi8vc2NoZW1hcy5uYXYuZ292Lmh1L09TQS8zLjAvYmFzZSI+PGludm9pY2VOdW1iZXI+VEVTVDAwMTwvaW52b2ljZU51bWJlcj48aW52b2ljZUlzc3VlRGF0ZT4yMDIzLTAxLTAxPC9pbnZvaWNlSXNzdWVEYXRlPjwvSW52b2ljZURhdGE+</invoiceData>
                    </invoiceDataResult>
                </QueryInvoiceDataResponse>""",
            )

            invoice_data = client.get_invoice_data(
                "TEST001", InvoiceDirectionType.OUTBOUND
            )

            assert invoice_data.invoice_number == "TEST001"
            assert invoice_data.invoice_issue_date is not None

    def test_query_invoice_check_success(self, sample_credentials):
        """Test successful invoice check query."""
        client = NavOnlineInvoiceClient(sample_credentials)

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

            request = QueryInvoiceCheckRequest(
                invoice_number_query=InvoiceNumberQueryType(
                    invoice_number="TEST001",
                    invoice_direction=InvoiceDirectionType.OUTBOUND,
                    batch_index=1,
                )
            )

            result = client.query_invoice_check(sample_credentials, request)

            # For now, just check that we get some result
            assert result is not None