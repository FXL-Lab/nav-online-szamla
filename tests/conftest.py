"""
Test configuration and fixtures for the NAV Online Számla tests.
"""

import pytest
from decimal import Decimal
from tempfile import NamedTemporaryFile
from pathlib import Path

from nav_online_szamla.models_legacy import NavCredentials
from nav_online_szamla.models import InvoiceData, ManageInvoiceOperationType
from nav_online_szamla.models.invoice_data import (
    InvoiceMainType, InvoiceType, InvoiceHeadType, SupplierInfoType,
    CustomerInfoType, InvoiceDetailType, CustomerVatDataType, CustomerTaxNumberType
)
from nav_online_szamla.models.invoice_base import TaxNumberType, AddressType, SimpleAddressType
from nav_online_szamla.excel.models import InvoiceHeaderRow, InvoiceLineRow


@pytest.fixture
def sample_credentials():
    """Sample NAV credentials for testing."""
    return NavCredentials(
        login="test_user",
        password="test_password",
        signer_key="test_signer_key",
        tax_number="12345678",
    )


@pytest.fixture
def temp_excel_file():
    """Create temporary Excel file for testing."""
    with NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_file:
        yield temp_file.name
    # Cleanup
    Path(temp_file.name).unlink(missing_ok=True)


@pytest.fixture
def sample_invoice_data():
    """Create sample InvoiceData for Excel testing."""
    # Create supplier info
    supplier_tax_number = TaxNumberType(
        taxpayer_id="12345678",
        vat_code="2", 
        county_code="01"
    )
    supplier_address = AddressType(
        simple_address=SimpleAddressType(
            country_code="HU",
            postal_code="1234",
            city="Budapest",
            additional_address_detail="Test utca 1."
        )
    )
    supplier_info = SupplierInfoType(
        supplier_tax_number=supplier_tax_number,
        supplier_name="Test Supplier Ltd.",
        supplier_address=supplier_address
    )

    # Create customer info with proper nested structure
    customer_tax_number = CustomerTaxNumberType(
        taxpayer_id="87654321",
        vat_code="2",
        county_code="02"
    )
    customer_vat_data = CustomerVatDataType(
        customer_tax_number=customer_tax_number,
        community_vat_number="HU87654321",
        third_state_tax_id="EU123456"
    )
    customer_address = AddressType(
        simple_address=SimpleAddressType(
            country_code="HU",
            postal_code="5678",
            city="Debrecen",
            additional_address_detail="Buyer street 2."
        )
    )
    customer_info = CustomerInfoType(
        customer_vat_data=customer_vat_data,
        customer_name="Test Customer Inc.",
        customer_address=customer_address
    )

    # Create invoice detail
    from nav_online_szamla.models.invoice_base import PaymentMethodType, InvoiceCategoryType
    invoice_detail = InvoiceDetailType(
        invoice_category=InvoiceCategoryType.NORMAL,
        invoice_delivery_date="2024-01-15",
        payment_date="2024-02-15", 
        payment_method=PaymentMethodType.TRANSFER,
        currency_code="HUF",
        exchange_rate=Decimal("1.0"),
        small_business_indicator=False,
        cash_accounting_indicator=False
    )

    # Create invoice head
    invoice_head = InvoiceHeadType(
        supplier_info=supplier_info,
        customer_info=customer_info,
        invoice_detail=invoice_detail
    )

    # Create main invoice structure (without lines for simplicity)
    invoice = InvoiceType(
        invoice_head=invoice_head
    )
    invoice_main = InvoiceMainType(invoice=invoice)

    # Create invoice data
    invoice_data = InvoiceData(
        invoice_number="TEST-001",
        invoice_issue_date="2024-01-15",
        completeness_indicator=True
    )
    invoice_data.invoice_main = invoice_main

    return invoice_data


@pytest.fixture 
def sample_header_row():
    """Create sample InvoiceHeaderRow for testing."""
    return InvoiceHeaderRow(
        invoice_number="TEST-001",
        invoice_issue_date="2024-01-15",
        completeness_indicator=True,
        seller_name="Test Supplier Ltd.",
        buyer_name="Test Customer Inc.",
        net_amount_original=1000.0,
        gross_amount_original=1270.0
    )


@pytest.fixture
def sample_line_row():
    """Create sample InvoiceLineRow for testing."""
    return InvoiceLineRow(
        invoice_number="TEST-001",
        line_number=1,
        description="Test Product",
        quantity=1.0,
        unit_price=1000.0,
        net_amount_original=1000.0,
        gross_amount_original=1270.0
    )


@pytest.fixture
def mock_xml_response():
    """Mock XML response for testing."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDigestResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api">
    <header>
        <requestId>test123</requestId>
        <timestamp>2024-01-01T10:00:00.000Z</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <result>
        <funcCode>OK</funcCode>
    </result>
    <invoiceDigestResult>
        <currentPage>1</currentPage>
        <availablePage>1</availablePage>
        <invoiceDigest>
            <invoiceNumber>TEST001</invoiceNumber>
            <invoiceOperation>CREATE</invoiceOperation>
            <supplierName>Test Supplier</supplierName>
            <supplierTaxNumber>12345678</supplierTaxNumber>
            <customerName>Test Customer</customerName>
            <customerTaxNumber>87654321</customerTaxNumber>
            <issueDate>2024-01-15</issueDate>
            <completionDate>2024-01-15</completionDate>
            <invoiceNetAmount>10000</invoiceNetAmount>
            <invoiceVatAmount>2700</invoiceVatAmount>
            <invoiceGrossAmount>12700</invoiceGrossAmount>
            <currencyCode>HUF</currencyCode>
            <source>ELECTRONIC</source>
        </invoiceDigest>
    </invoiceDigestResult>
</QueryInvoiceDigestResponse>"""


@pytest.fixture
def mock_error_response():
    """Mock error XML response for testing."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<QueryInvoiceDigestResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api">
    <header>
        <requestId>test123</requestId>
        <timestamp>2024-01-01T10:00:00.000Z</timestamp>
        <requestVersion>3.0</requestVersion>
        <headerVersion>1.0</headerVersion>
    </header>
    <result>
        <funcCode>ERROR</funcCode>
        <errorCode>INVALID_CREDENTIALS</errorCode>
        <message>Invalid authentication credentials</message>
    </result>
</QueryInvoiceDigestResponse>"""
