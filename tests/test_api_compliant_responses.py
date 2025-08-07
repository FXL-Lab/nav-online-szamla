"""
Tests for API-compliant response types.
"""

import pytest
from datetime import datetime

from nav_online_szamla.models import (
    # Response types
    BasicHeaderType,
    BasicResultType,
    NotificationType,
    SoftwareType,
    BasicOnlineInvoiceResponseType,
    QueryInvoiceDigestResponseType,
    QueryInvoiceCheckResponseType,
    InvoiceDigestType,
    InvoiceCheckResultType,
    InvoiceDataType,
    # Dependencies
    InvoiceDirection,
    SupplierInfo,
    CustomerInfo,
    TaxNumber,
    Address,
)


class TestBasicTypes:
    """Test basic API response types."""

    def test_basic_header_type(self):
        """Test BasicHeaderType creation."""
        header = BasicHeaderType(
            request_id="test-123",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            request_version="3.0",
            header_version="1.0",
        )

        assert header.request_id == "test-123"
        assert header.timestamp == datetime(2024, 1, 1, 12, 0, 0)
        assert header.request_version == "3.0"
        assert header.header_version == "1.0"

    def test_notification_type(self):
        """Test NotificationType creation."""
        notification = NotificationType(
            notification_code="INFO001", notification_text="Information message"
        )

        assert notification.notification_code == "INFO001"
        assert notification.notification_text == "Information message"

    def test_basic_result_type_success(self):
        """Test BasicResultType for successful response."""
        result = BasicResultType(func_code="OK")

        assert result.func_code == "OK"
        assert result.error_code is None
        assert result.message is None
        assert result.notifications is None

    def test_basic_result_type_error(self):
        """Test BasicResultType for error response."""
        notification = NotificationType(
            notification_code="WARN001", notification_text="Warning message"
        )

        result = BasicResultType(
            func_code="ERROR",
            error_code="INVALID_CREDENTIALS",
            message="Authentication failed",
            notifications=[notification],
        )

        assert result.func_code == "ERROR"
        assert result.error_code == "INVALID_CREDENTIALS"
        assert result.message == "Authentication failed"
        assert len(result.notifications) == 1
        assert result.notifications[0].notification_code == "WARN001"

    def test_software_type(self):
        """Test SoftwareType creation."""
        software = SoftwareType(
            software_id="NAV-ONLINE-SZAMLA-01",
            software_name="NAV Online Számla",
            software_operation="LOCAL_SOFTWARE",
            software_main_version="1.0.0",
            software_dev_name="FXL Technology",
            software_dev_contact="info@fxltech.com",
            software_dev_country_code="HU",
            software_dev_tax_number="12345678",
        )

        assert software.software_id == "NAV-ONLINE-SZAMLA-01"
        assert software.software_name == "NAV Online Számla"
        assert software.software_operation == "LOCAL_SOFTWARE"
        assert software.software_main_version == "1.0.0"
        assert software.software_dev_name == "FXL Technology"
        assert software.software_dev_contact == "info@fxltech.com"
        assert software.software_dev_country_code == "HU"
        assert software.software_dev_tax_number == "12345678"


class TestBasicOnlineInvoiceResponseType:
    """Test BasicOnlineInvoiceResponseType."""

    def test_basic_response_creation(self):
        """Test basic response creation."""
        header = BasicHeaderType(
            request_id="test-123",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            request_version="3.0",
            header_version="1.0",
        )

        result = BasicResultType(func_code="OK")

        software = SoftwareType(
            software_id="NAV-ONLINE-SZAMLA-01",
            software_name="NAV Online Számla",
            software_operation="LOCAL_SOFTWARE",
            software_main_version="1.0.0",
            software_dev_name="FXL Technology",
            software_dev_contact="info@fxltech.com",
        )

        response = BasicOnlineInvoiceResponseType(
            header=header, result=result, software=software
        )

        assert response.header.request_id == "test-123"
        assert response.result.func_code == "OK"
        assert response.software.software_name == "NAV Online Számla"


class TestInvoiceDigestType:
    """Test InvoiceDigestType."""

    def test_invoice_digest_minimal(self):
        """Test minimal invoice digest creation."""
        digest = InvoiceDigestType(
            invoice_number="TEST001",
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_operation="CREATE",
            invoice_category="NORMAL",
            invoice_issue_date=datetime(2024, 1, 1),
            supplier_tax_number="12345678",
            supplier_name="Test Supplier",
            ins_date=datetime(2024, 1, 1, 10, 0, 0),
            batch_index=1,
        )

        assert digest.invoice_number == "TEST001"
        assert digest.batch_index == 1
        assert digest.invoice_operation == "CREATE"
        assert digest.invoice_category == "NORMAL"
        assert digest.supplier_tax_number == "12345678"
        assert digest.supplier_name == "Test Supplier"
        assert digest.ins_date == datetime(2024, 1, 1, 10, 0, 0)

    def test_invoice_digest_full(self):
        """Test full invoice digest creation."""
        digest = InvoiceDigestType(
            invoice_number="TEST001",
            invoice_direction=InvoiceDirection.OUTBOUND,
            batch_index=1,
            invoice_operation="CREATE",
            invoice_category="NORMAL",
            invoice_issue_date=datetime(2024, 1, 1),
            supplier_tax_number="12345678",
            supplier_group_member_tax_number="87654321",
            supplier_name="Test Supplier",
            customer_tax_number="11111111",
            customer_group_member_tax_number="22222222",
            customer_name="Test Customer",
            payment_method="CASH",
            payment_date=datetime(2024, 1, 15),
            invoice_appearance="PAPER",
            source="WEB",
            invoice_delivery_date=datetime(2024, 1, 1),
            currency="HUF",
            invoice_net_amount=10000.0,
            invoice_net_amount_huf=10000.0,
            invoice_vat_amount=2700.0,
            invoice_vat_amount_huf=2700.0,
            transaction_id="trans-123",
            index=1,
            original_invoice_number="ORIG001",
            modification_index=1,
            ins_date=datetime(2024, 1, 1, 10, 0, 0),
            completeness_indicator=True,
        )

        assert digest.invoice_number == "TEST001"
        assert digest.customer_name == "Test Customer"
        assert digest.payment_method == "CASH"
        assert digest.currency == "HUF"
        assert digest.invoice_net_amount == 10000.0
        assert digest.invoice_vat_amount == 2700.0
        assert digest.completeness_indicator is True


class TestQueryInvoiceDigestResponseType:
    """Test QueryInvoiceDigestResponseType."""

    def test_query_digest_response(self):
        """Test query digest response creation."""
        header = BasicHeaderType(
            request_id="test-123",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            request_version="3.0",
            header_version="1.0",
        )

        result = BasicResultType(func_code="OK")

        digest = InvoiceDigestType(
            invoice_number="TEST001",
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_operation="CREATE",
            invoice_category="NORMAL",
            invoice_issue_date=datetime(2024, 1, 1),
            supplier_tax_number="12345678",
            supplier_name="Test Supplier",
            ins_date=datetime(2024, 1, 1, 10, 0, 0),
            batch_index=1,
        )

        response = QueryInvoiceDigestResponseType(
            header=header,
            result=result,
            current_page=1,
            available_page=5,
            invoice_digests=[digest],
        )

        assert response.header.request_id == "test-123"
        assert response.result.func_code == "OK"
        assert response.current_page == 1
        assert response.available_page == 5
        assert len(response.invoice_digests) == 1
        assert response.invoice_digests[0].invoice_number == "TEST001"


class TestInvoiceCheckResultType:
    """Test InvoiceCheckResultType."""

    def test_invoice_check_result(self):
        """Test invoice check result creation."""
        result = InvoiceCheckResultType(
            invoice_number="TEST001",
            batch_index=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            query_result_code="FOUND",
        )

        assert result.invoice_number == "TEST001"
        assert result.batch_index == 1
        assert result.invoice_direction == InvoiceDirection.OUTBOUND
        assert result.query_result_code == "FOUND"


class TestQueryInvoiceCheckResponseType:
    """Test QueryInvoiceCheckResponseType."""

    def test_query_check_response(self):
        """Test query check response creation."""
        header = BasicHeaderType(
            request_id="test-123",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            request_version="3.0",
            header_version="1.0",
        )

        result = BasicResultType(func_code="OK")

        check_result = InvoiceCheckResultType(
            invoice_number="TEST001",
            batch_index=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            query_result_code="FOUND",
        )

        response = QueryInvoiceCheckResponseType(
            header=header, result=result, query_results=[check_result]
        )

        assert response.header.request_id == "test-123"
        assert response.result.func_code == "OK"
        assert len(response.query_results) == 1
        assert response.query_results[0].query_result_code == "FOUND"


class TestInvoiceDataType:
    """Test InvoiceDataType."""

    def test_invoice_data_creation(self):
        """Test invoice data creation."""
        address = Address(
            country_code="HU",
            postal_code="1234",
            city="Budapest",
            street_name="Test utca",
            public_place_category="utca",
            number="1",
        )

        supplier_info = SupplierInfo(
            tax_number=TaxNumber(taxpayer_id="12345678"),
            name="Test Supplier",
            address=address,
        )

        customer_info = CustomerInfo(name="Test Customer")

        invoice_data = InvoiceDataType(
            invoice_number="TEST001",
            invoice_issue_date=datetime.now(),
            completeness_indicator=True,
            invoice_direction=InvoiceDirection.OUTBOUND,
            supplier_info=supplier_info,
            customer_info=customer_info,
            invoice_main={"invoiceCategory": "NORMAL", "currencyCode": "HUF"},
        )

        assert invoice_data.invoice_number == "TEST001"
        assert invoice_data.invoice_direction == InvoiceDirection.OUTBOUND
        assert invoice_data.supplier_info.name == "Test Supplier"
        assert invoice_data.customer_info.name == "Test Customer"
        assert invoice_data.invoice_main["currencyCode"] == "HUF"
        assert invoice_data.completeness_indicator is True
        assert invoice_data.invoice_summary is None  # Now optional
