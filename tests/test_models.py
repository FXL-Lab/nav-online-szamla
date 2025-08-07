"""
Tests for data models.
"""

import pytest
from datetime import datetime

from nav_online_szamla.models import (
    TaxNumber,
    Address,
    SupplierInfo,
    CustomerInfo,
    InvoiceDirection,
    InvoiceOperation,
    CustomerVatStatus,
    InvoiceDigest,
    NavCredentials,
)


class TestEnums:
    """Test enum classes."""

    def test_invoice_direction_enum(self):
        """Test InvoiceDirection enum."""
        assert InvoiceDirection.OUTBOUND.value == "OUTBOUND"
        assert InvoiceDirection.INBOUND.value == "INBOUND"

    def test_invoice_operation_enum(self):
        """Test InvoiceOperation enum."""
        assert InvoiceOperation.CREATE.value == "CREATE"
        assert InvoiceOperation.MODIFY.value == "MODIFY"
        assert InvoiceOperation.STORNO.value == "STORNO"

    def test_customer_vat_status_enum(self):
        """Test CustomerVatStatus enum."""
        assert CustomerVatStatus.DOMESTIC.value == "DOMESTIC"
        assert CustomerVatStatus.PRIVATE_PERSON.value == "PRIVATE_PERSON"
        assert CustomerVatStatus.OTHER.value == "OTHER"


class TestTaxNumber:
    """Test TaxNumber data class."""

    def test_tax_number_basic(self):
        """Test basic TaxNumber creation."""
        tax_number = TaxNumber(taxpayer_id="12345678")

        assert tax_number.taxpayer_id == "12345678"
        assert tax_number.vat_code is None
        assert tax_number.county_code is None

    def test_tax_number_full(self):
        """Test full TaxNumber creation."""
        tax_number = TaxNumber(taxpayer_id="12345678", vat_code="1", county_code="02")

        assert tax_number.taxpayer_id == "12345678"
        assert tax_number.vat_code == "1"
        assert tax_number.county_code == "02"


class TestAddress:
    """Test Address data class."""

    def test_address_basic(self):
        """Test basic Address creation."""
        address = Address(country_code="HU", postal_code="1234", city="Budapest")

        assert address.country_code == "HU"
        assert address.postal_code == "1234"
        assert address.city == "Budapest"
        assert address.additional_address_detail is None

    def test_address_detailed(self):
        """Test detailed Address creation."""
        address = Address(
            country_code="HU",
            postal_code="1234",
            city="Budapest",
            additional_address_detail="Apartment 5",
            street_name="Test Street",
            public_place_category="utca",
            number="42",
        )

        assert address.additional_address_detail == "Apartment 5"
        assert address.street_name == "Test Street"
        assert address.public_place_category == "utca"
        assert address.number == "42"


class TestSupplierInfo:
    """Test SupplierInfo data class."""

    def test_supplier_info(self):
        """Test SupplierInfo creation."""
        tax_number = TaxNumber(taxpayer_id="12345678")
        address = Address(country_code="HU", postal_code="1234", city="Budapest")

        supplier = SupplierInfo(
            tax_number=tax_number, name="Test Supplier Ltd.", address=address
        )

        assert supplier.tax_number == tax_number
        assert supplier.name == "Test Supplier Ltd."
        assert supplier.address == address


class TestCustomerInfo:
    """Test CustomerInfo data class."""

    def test_customer_info_minimal(self):
        """Test minimal CustomerInfo creation."""
        customer = CustomerInfo(name="Test Customer")

        assert customer.name == "Test Customer"
        assert customer.tax_number is None
        assert customer.vat_status is None

    def test_customer_info_full(self):
        """Test full CustomerInfo creation."""
        tax_number = TaxNumber(taxpayer_id="87654321")
        address = Address(country_code="HU", postal_code="5678", city="Szeged")

        customer = CustomerInfo(
            name="Test Customer",
            tax_number=tax_number,
            vat_status=CustomerVatStatus.DOMESTIC,
            address=address,
            community_vat_number="HU12345678",
            third_country_tax_number="TC123456",
        )

        assert customer.name == "Test Customer"
        assert customer.tax_number == tax_number
        assert customer.vat_status == CustomerVatStatus.DOMESTIC
        assert customer.address == address
        assert customer.community_vat_number == "HU12345678"
        assert customer.third_country_tax_number == "TC123456"


class TestInvoiceDigest:
    """Test InvoiceDigest data class."""

    def test_invoice_digest(self):
        """Test InvoiceDigest creation."""
        issue_date = datetime(2024, 1, 15)
        completion_date = datetime(2024, 1, 15)

        digest = InvoiceDigest(
            invoice_number="TEST001",
            batch_index=None,
            invoice_operation=InvoiceOperation.CREATE,
            supplier_name="Test Supplier",
            supplier_tax_number="12345678",
            customer_name="Test Customer",
            customer_tax_number="87654321",
            issue_date=issue_date,
            completion_date=completion_date,
            invoice_net_amount=10000.0,
            invoice_vat_amount=2700.0,
            invoice_gross_amount=12700.0,
            currency_code="HUF",
            source="ELECTRONIC",
        )

        assert digest.invoice_number == "TEST001"
        assert digest.batch_index is None
        assert digest.invoice_operation == InvoiceOperation.CREATE
        assert digest.supplier_name == "Test Supplier"
        assert digest.supplier_tax_number == "12345678"
        assert digest.customer_name == "Test Customer"
        assert digest.customer_tax_number == "87654321"
        assert digest.issue_date == issue_date
        assert digest.completion_date == completion_date
        assert digest.invoice_net_amount == 10000.0
        assert digest.invoice_vat_amount == 2700.0
        assert digest.invoice_gross_amount == 12700.0
        assert digest.currency_code == "HUF"
        assert digest.source == "ELECTRONIC"


class TestNavCredentials:
    """Test NavCredentials data class."""

    def test_nav_credentials_basic(self):
        """Test NavCredentials with all required fields."""
        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_key",
            tax_number="32703094",
        )

        assert credentials.login == "test_user"
        assert credentials.password == "test_password"
        assert credentials.signer_key == "test_key"
        assert credentials.tax_number == "32703094"

    def test_nav_credentials_custom(self):
        """Test NavCredentials with custom tax number."""
        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_key",
            tax_number="12345678",
        )

        assert credentials.tax_number == "12345678"
