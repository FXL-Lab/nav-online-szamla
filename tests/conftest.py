"""
Test configuration and fixtures for the NAV Online Számla tests.
"""
import pytest
from datetime import datetime

from nav_online_szamla.models import NavCredentials, InvoiceDirection


@pytest.fixture
def sample_credentials():
    """Sample NAV credentials for testing."""
    return NavCredentials(
        login="test_user",
        password="test_password",
        signer_key="test_signer_key",
        tax_number="12345678"
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
