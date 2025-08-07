"""
Tests for comprehensive invoice data retrieval functionality.
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock

from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.models import (
    NavCredentials,
    InvoiceDirection,
    QueryInvoiceDigestResponseType,
    InvoiceDigestType,
    InvoiceDetail,
    BasicResultType,
    BasicHeaderType,
)
from nav_online_szamla.exceptions import NavValidationException, NavApiException


class TestComprehensiveInvoiceData:
    """Test comprehensive invoice data retrieval functions."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return NavOnlineInvoiceClient()

    @pytest.fixture
    def credentials(self):
        """Create test credentials."""
        return NavCredentials(
            login="test_login",
            password="test_password",
            tax_number="12345678",
            signer_key="test_signer_key",
        )

    @pytest.fixture
    def sample_invoice_digest(self):
        """Create sample invoice digest."""
        return InvoiceDigestType(
            invoice_number="TEST001",
            invoice_direction=InvoiceDirection.OUTBOUND,
            batch_index=None,
            invoice_operation="CREATE",
            supplier_tax_number="12345678",
            customer_tax_number="87654321",
            ins_date=datetime.now(),
            completeness_indicator=True,
            original_request_version="3.0",
        )

    @pytest.fixture
    def sample_invoice_detail(self):
        """Create sample invoice detail."""
        return InvoiceDetail(
            invoice_number="TEST001",
            issue_date=datetime.now(),
            completion_date=None,
            currency_code="HUF",
            exchange_rate=None,
            supplier_info=None,
            customer_info=None,
            invoice_net_amount=10000.0,
            invoice_vat_amount=2700.0,
            invoice_gross_amount=12700.0,
            source="API",
            additional_data={},
        )

    def test_get_all_invoice_data_for_date_range_basic(
        self, client, credentials, sample_invoice_digest, sample_invoice_detail
    ):
        """Test basic comprehensive invoice data retrieval."""
        start_date = datetime.now() - timedelta(days=7)
        end_date = datetime.now()

        # Mock the digest response
        digest_response = QueryInvoiceDigestResponseType(
            header=BasicHeaderType(
                request_id="test_id",
                timestamp="2024-01-01T10:00:00Z",
                request_version="3.0",
                header_version="1.0",
            ),
            result=BasicResultType(func_code="OK", error_code=None, message=None),
            software=None,
            current_page=1,
            available_page=1,
            available_count=1,
            invoice_digests=[sample_invoice_digest],
        )

        with patch.object(client, "validate_credentials"):
            with patch.object(
                client, "query_invoice_digest", return_value=digest_response
            ):
                with patch.object(
                    client, "query_invoice_data", return_value=sample_invoice_detail
                ):

                    result = client.get_all_invoice_data_for_date_range(
                        credentials=credentials,
                        start_date=start_date,
                        end_date=end_date,
                        invoice_direction=InvoiceDirection.OUTBOUND,
                    )

                    assert len(result) == 1
                    assert result[0].invoice_number == "TEST001"
                    assert result[0].invoice_gross_amount == 12700.0

    def test_get_all_invoice_data_for_date_range_multiple_pages(
        self, client, credentials, sample_invoice_digest, sample_invoice_detail
    ):
        """Test comprehensive invoice data retrieval with multiple pages."""
        start_date = datetime.now() - timedelta(days=7)
        end_date = datetime.now()

        # Create different invoice digests for each page
        digest1 = InvoiceDigestType(
            invoice_number="TEST001",
            invoice_direction=InvoiceDirection.OUTBOUND,
            batch_index=None,
            invoice_operation="CREATE",
            supplier_tax_number="12345678",
            customer_tax_number="87654321",
            ins_date=datetime.now(),
            completeness_indicator=True,
            original_request_version="3.0",
        )

        digest2 = InvoiceDigestType(
            invoice_number="TEST002",
            invoice_direction=InvoiceDirection.OUTBOUND,
            batch_index=None,
            invoice_operation="CREATE",
            supplier_tax_number="12345678",
            customer_tax_number="87654321",
            ins_date=datetime.now(),
            completeness_indicator=True,
            original_request_version="3.0",
        )

        # Mock responses for different pages
        page1_response = QueryInvoiceDigestResponseType(
            header=BasicHeaderType(
                request_id="test_id",
                timestamp="2024-01-01T10:00:00Z",
                request_version="3.0",
                header_version="1.0",
            ),
            result=BasicResultType(func_code="OK", error_code=None, message=None),
            software=None,
            current_page=1,
            available_page=2,
            available_count=2,
            invoice_digests=[digest1],
        )

        page2_response = QueryInvoiceDigestResponseType(
            header=BasicHeaderType(
                request_id="test_id",
                timestamp="2024-01-01T10:00:00Z",
                request_version="3.0",
                header_version="1.0",
            ),
            result=BasicResultType(func_code="OK", error_code=None, message=None),
            software=None,
            current_page=2,
            available_page=2,
            available_count=2,
            invoice_digests=[digest2],
        )

        # Empty response for page 3 (no more data)
        page3_response = QueryInvoiceDigestResponseType(
            header=BasicHeaderType(
                request_id="test_id",
                timestamp="2024-01-01T10:00:00Z",
                request_version="3.0",
                header_version="1.0",
            ),
            result=BasicResultType(func_code="OK", error_code=None, message=None),
            software=None,
            current_page=3,
            available_page=2,
            available_count=2,
            invoice_digests=[],
        )

        # Create corresponding invoice details
        detail1 = InvoiceDetail(
            invoice_number="TEST001",
            issue_date=datetime.now(),
            completion_date=None,
            currency_code="HUF",
            exchange_rate=None,
            supplier_info=None,
            customer_info=None,
            invoice_net_amount=10000.0,
            invoice_vat_amount=2700.0,
            invoice_gross_amount=12700.0,
            source="API",
            additional_data={},
        )

        detail2 = InvoiceDetail(
            invoice_number="TEST002",
            issue_date=datetime.now(),
            completion_date=None,
            currency_code="HUF",
            exchange_rate=None,
            supplier_info=None,
            customer_info=None,
            invoice_net_amount=20000.0,
            invoice_vat_amount=5400.0,
            invoice_gross_amount=25400.0,
            source="API",
            additional_data={},
        )

        def mock_query_digest(credentials, request):
            if request.page == 1:
                return page1_response
            elif request.page == 2:
                return page2_response
            else:
                return page3_response

        def mock_query_data(credentials, request):
            if request.invoice_number == "TEST001":
                return detail1
            elif request.invoice_number == "TEST002":
                return detail2
            return None

        with patch.object(client, "validate_credentials"):
            with patch.object(
                client, "query_invoice_digest", side_effect=mock_query_digest
            ):
                with patch.object(
                    client, "query_invoice_data", side_effect=mock_query_data
                ):

                    result = client.get_all_invoice_data_for_date_range(
                        credentials=credentials,
                        start_date=start_date,
                        end_date=end_date,
                        invoice_direction=InvoiceDirection.OUTBOUND,
                    )

                    assert len(result) == 2
                    assert result[0].invoice_number == "TEST001"
                    assert result[1].invoice_number == "TEST002"
                    assert result[0].invoice_gross_amount == 12700.0
                    assert result[1].invoice_gross_amount == 25400.0

    def test_get_all_invoice_data_for_date_range_multiple_invoices(
        self, client, credentials, sample_invoice_digest, sample_invoice_detail
    ):
        """Test comprehensive invoice data retrieval with multiple invoices."""
        start_date = datetime.now() - timedelta(days=7)
        end_date = datetime.now()

        # Create 3 invoice digests
        digests = []
        for i in range(3):
            digest = InvoiceDigestType(
                invoice_number=f"TEST{i+1:03d}",
                invoice_direction=InvoiceDirection.OUTBOUND,
                batch_index=None,
                invoice_operation="CREATE",
                supplier_tax_number="12345678",
                customer_tax_number="87654321",
                ins_date=datetime.now(),
                completeness_indicator=True,
                original_request_version="3.0",
            )
            digests.append(digest)

        digest_response = QueryInvoiceDigestResponseType(
            header=BasicHeaderType(
                request_id="test_id",
                timestamp="2024-01-01T10:00:00Z",
                request_version="3.0",
                header_version="1.0",
            ),
            result=BasicResultType(func_code="OK", error_code=None, message=None),
            software=None,
            current_page=1,
            available_page=1,
            available_count=3,
            invoice_digests=digests,
        )

        def mock_query_data(credentials, request):
            return InvoiceDetail(
                invoice_number=request.invoice_number,
                issue_date=datetime.now(),
                completion_date=None,
                currency_code="HUF",
                exchange_rate=None,
                supplier_info=None,
                customer_info=None,
                invoice_net_amount=10000.0,
                invoice_vat_amount=2700.0,
                invoice_gross_amount=12700.0,
                source="API",
                additional_data={},
            )

        with patch.object(client, "validate_credentials"):
            with patch.object(
                client, "query_invoice_digest", return_value=digest_response
            ):
                with patch.object(
                    client, "query_invoice_data", side_effect=mock_query_data
                ):

                    # Get all invoices
                    result = client.get_all_invoice_data_for_date_range(
                        credentials=credentials,
                        start_date=start_date,
                        end_date=end_date,
                        invoice_direction=InvoiceDirection.OUTBOUND,
                    )

                    # Should get all 3 invoices
                    assert len(result) == 3

    def test_get_all_invoice_data_with_progress_callback(self, client, credentials):
        """Test comprehensive invoice data retrieval with progress callback."""
        start_date = datetime.now() - timedelta(days=7)
        end_date = datetime.now()

        progress_calls = []

        def progress_callback(current_count, total_estimated, current_invoice_number):
            progress_calls.append(
                (current_count, total_estimated, current_invoice_number)
            )

        # Mock single invoice
        digest = InvoiceDigestType(
            invoice_number="TEST001",
            invoice_direction=InvoiceDirection.OUTBOUND,
            batch_index=None,
            invoice_operation="CREATE",
            supplier_tax_number="12345678",
            customer_tax_number="87654321",
            ins_date=datetime.now(),
            completeness_indicator=True,
            original_request_version="3.0",
        )

        digest_response = QueryInvoiceDigestResponseType(
            header=BasicHeaderType(
                request_id="test_id",
                timestamp="2024-01-01T10:00:00Z",
                request_version="3.0",
                header_version="1.0",
            ),
            result=BasicResultType(func_code="OK", error_code=None, message=None),
            software=None,
            current_page=1,
            available_page=1,
            available_count=1,
            invoice_digests=[digest],
        )

        detail = InvoiceDetail(
            invoice_number="TEST001",
            issue_date=datetime.now(),
            completion_date=None,
            currency_code="HUF",
            exchange_rate=None,
            supplier_info=None,
            customer_info=None,
            invoice_net_amount=10000.0,
            invoice_vat_amount=2700.0,
            invoice_gross_amount=12700.0,
            source="API",
            additional_data={},
        )

        with patch.object(client, "validate_credentials"):
            with patch.object(
                client, "query_invoice_digest", return_value=digest_response
            ):
                with patch.object(client, "query_invoice_data", return_value=detail):

                    result = client.get_all_invoice_data_for_date_range_with_progress(
                        credentials=credentials,
                        start_date=start_date,
                        end_date=end_date,
                        invoice_direction=InvoiceDirection.OUTBOUND,
                        progress_callback=progress_callback,
                    )

                    assert len(result) == 1
                    assert len(progress_calls) == 1
                    assert progress_calls[0][0] == 1  # current_count
                    assert progress_calls[0][1] == 1  # total_estimated
                    assert progress_calls[0][2] == "TEST001"  # current_invoice_number

    def test_invalid_date_range(self, client, credentials):
        """Test validation of invalid date range."""
        start_date = datetime.now()
        end_date = datetime.now() - timedelta(days=1)  # End before start

        with pytest.raises(
            NavValidationException, match="Start date must be before end date"
        ):
            client.get_all_invoice_data_for_date_range(
                credentials=credentials, start_date=start_date, end_date=end_date
            )

    def test_date_range_too_large(self, client, credentials):
        """Test validation of date range that's too large."""
        start_date = datetime.now() - timedelta(
            days=400
        )  # More than MAX_DATE_RANGE_DAYS
        end_date = datetime.now()

        with patch.object(client, "validate_credentials"):
            with pytest.raises(NavValidationException, match="Date range too large"):
                client.get_all_invoice_data_for_date_range(
                    credentials=credentials, start_date=start_date, end_date=end_date
                )
