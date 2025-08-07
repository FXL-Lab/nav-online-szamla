"""
Tests for the main NAV client functionality.
"""

import pytest
import requests_mock
from datetime import datetime

from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.models import (
    InvoiceDirection,
    QueryInvoiceDigestRequest,
    InvoiceQueryParams,
    MandatoryQueryParams,
    DateTimeRange,
)
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
                    <r>
                        <funcCode>OK</funcCode>
                    </r>
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

            request = QueryInvoiceDigestRequest(
                page=1,
                invoice_direction=InvoiceDirection.OUTBOUND,
                invoice_query_params=InvoiceQueryParams(
                    mandatory_query_params=MandatoryQueryParams(
                        ins_date=DateTimeRange(
                            date_time_from=datetime(2023, 1, 1),
                            date_time_to=datetime(2023, 1, 31),
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

    def test_query_invoice_digest_success_duplicate(self, sample_credentials):
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
                    <r>
                        <funcCode>OK</funcCode>
                    </r>
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

            request = QueryInvoiceDigestRequest(
                page=1,
                invoice_direction=InvoiceDirection.OUTBOUND,
                invoice_query_params=InvoiceQueryParams(
                    mandatory_query_params=MandatoryQueryParams(
                        ins_date=DateTimeRange(
                            date_time_from=datetime(2023, 1, 1),
                            date_time_to=datetime(2023, 1, 31),
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
