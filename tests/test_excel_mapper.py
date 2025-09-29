"""
Unit tests for Excel field mapper functionality.
"""

import pytest
from decimal import Decimal
from datetime import datetime, date

from nav_online_szamla.excel.mapper import ExcelFieldMapper
from nav_online_szamla.excel.models import InvoiceHeaderRow, InvoiceLineRow
from nav_online_szamla.excel.exceptions import ExcelMappingException
from nav_online_szamla.models import InvoiceData, ManageInvoiceOperationType
from nav_online_szamla.models.invoice_data import (
    InvoiceMainType, InvoiceType, InvoiceHeadType, SupplierInfoType,
    CustomerInfoType, LinesType, LineType, SummaryType, InvoiceDetailType,
    CustomerVatDataType, CustomerTaxNumberType, LineAmountsNormalType,
    SummaryNormalType, SummaryGrossDataType
)
from nav_online_szamla.models.invoice_base import TaxNumberType, AddressType, SimpleAddressType


class TestExcelFieldMapper:
    """Test cases for ExcelFieldMapper."""

    @pytest.fixture
    def sample_invoice_data(self):
        """Create sample InvoiceData for testing."""
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

        # Create line items
        line = LineType(
            line_number=1,
            line_description="Test Product",
            quantity=Decimal("2.0"),
            unit_price=Decimal("1000.0")
        )
        lines = LinesType(line=[line])

        # Create summary
        summary_normal = SummaryNormalType(
            invoice_net_amount=Decimal("2000.0"),
            invoice_net_amount_huf=Decimal("2000.0"),
            invoice_vat_amount=Decimal("540.0"),
            invoice_vat_amount_huf=Decimal("540.0"),
            summary_by_vat_rate=[]
        )
        summary_gross_data = SummaryGrossDataType(
            invoice_gross_amount=Decimal("2540.0"),
            invoice_gross_amount_huf=Decimal("2540.0")
        )
        summary = SummaryType(
            summary_normal=summary_normal,
            summary_gross_data=summary_gross_data
        )

        # Create main invoice structure
        invoice = InvoiceType(
            invoice_head=invoice_head,
            invoice_lines=lines,
            invoice_summary=summary
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
    def sample_header_row(self):
        """Create sample InvoiceHeaderRow for testing."""
        return InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            completeness_indicator=True,
            seller_name="Test Supplier Ltd.",
            seller_tax_number_main="12345678",
            seller_tax_number_vat="2",
            seller_tax_number_county="01",
            seller_country_code="HU",
            seller_postal_code="1234",
            seller_city="Budapest",
            seller_address_detail="Test utca 1.",
            buyer_name="Test Customer Inc.",
            buyer_tax_number_main="87654321",
            buyer_tax_number_vat="2",
            buyer_tax_number_county="02",
            buyer_country_code="HU",
            buyer_postal_code="5678",
            buyer_city="Debrecen",
            buyer_address_detail="Buyer street 2.",
            buyer_vat_status="DOMESTIC",
            buyer_community_vat_number="HU87654321",
            buyer_third_country_tax_number="EU123456",
            fulfillment_date="2024-01-15",
            payment_due_date="2024-02-15",
            payment_method="TRANSFER",
            invoice_currency="HUF",
            exchange_rate=1.0,
            small_business_indicator=False,
            cash_accounting_indicator=False,
            invoice_category="NORMAL",
            net_amount_original=2000.0,
            net_amount_huf=2000.0,
            vat_amount_original=540.0,
            vat_amount_huf=540.0,
            gross_amount_original=2540.0,
            gross_amount_huf=2540.0
        )

    @pytest.fixture
    def sample_line_rows(self):
        """Create sample InvoiceLineRow list for testing."""
        return [
            InvoiceLineRow(
                invoice_number="TEST-001",
                line_number=1,
                line_modification_type="CREATE",
                description="Test Product 1",
                quantity=1.0,
                unit_of_measure="PIECE",
                unit_price=1000.0,
                net_amount_original=1000.0,
                net_amount_huf=1000.0,
                vat_rate=27.0,
                vat_amount_original=270.0,
                vat_amount_huf=270.0,
                gross_amount_original=1270.0,
                gross_amount_huf=1270.0
            ),
            InvoiceLineRow(
                invoice_number="TEST-001",
                line_number=2,
                line_modification_type="CREATE",
                description="Test Product 2",
                quantity=1.0,
                unit_of_measure="PIECE",
                unit_price=1000.0,
                net_amount_original=1000.0,
                net_amount_huf=1000.0,
                vat_rate=27.0,
                vat_amount_original=270.0,
                vat_amount_huf=270.0,
                gross_amount_original=1270.0,
                gross_amount_huf=1270.0
            )
        ]

    def test_column_mappings_exist(self):
        """Test that column mappings are properly defined."""
        assert hasattr(ExcelFieldMapper, 'HEADER_COLUMNS')
        assert hasattr(ExcelFieldMapper, 'LINE_COLUMNS')
        
        # Test mappings are dictionaries and not empty
        assert isinstance(ExcelFieldMapper.HEADER_COLUMNS, dict)
        assert isinstance(ExcelFieldMapper.LINE_COLUMNS, dict)
        assert len(ExcelFieldMapper.HEADER_COLUMNS) > 0
        assert len(ExcelFieldMapper.LINE_COLUMNS) > 0

    def test_invoice_data_to_header_row_success(self, sample_invoice_data):
        """Test successful conversion from InvoiceData to header row."""
        result = ExcelFieldMapper.invoice_data_to_header_row(
            sample_invoice_data, ManageInvoiceOperationType.CREATE
        )

        assert isinstance(result, InvoiceHeaderRow)
        assert result.invoice_number == "TEST-001"
        assert result.invoice_issue_date == "2024-01-15"
        assert result.seller_name == "Test Supplier Ltd."
        assert result.buyer_name == "Test Customer Inc."
        assert result.net_amount_original == 2000.0

    def test_invoice_data_to_header_row_with_none_values(self):
        """Test conversion with minimal invoice data."""
        invoice_data = InvoiceData(
            invoice_number="MINIMAL-001",
            invoice_issue_date="2024-01-15",
            completeness_indicator=True
        )

        result = ExcelFieldMapper.invoice_data_to_header_row(
            invoice_data, ManageInvoiceOperationType.CREATE
        )

        assert isinstance(result, InvoiceHeaderRow)
        assert result.invoice_number == "MINIMAL-001"
        assert result.seller_name == ""  # Should default to empty string

    def test_invoice_data_to_line_rows_success(self, sample_invoice_data):
        """Test successful conversion from InvoiceData to line rows."""
        result = ExcelFieldMapper.invoice_data_to_line_rows(sample_invoice_data, ManageInvoiceOperationType.CREATE)

        assert isinstance(result, list)
        assert len(result) == 1  # One line in sample data
        assert isinstance(result[0], InvoiceLineRow)
        assert result[0].invoice_number == "TEST-001"
        assert result[0].line_number == 1
        assert result[0].description == "Test Product"

    def test_invoice_data_to_line_rows_no_lines(self):
        """Test conversion with no line items."""
        invoice_data = InvoiceData(
            invoice_number="NO-LINES-001",
            invoice_issue_date="2024-01-15",
            completeness_indicator=True
        )

        result = ExcelFieldMapper.invoice_data_to_line_rows(invoice_data, ManageInvoiceOperationType.CREATE)
        assert result == []

    def test_header_row_to_invoice_data_success(self, sample_header_row):
        """Test successful conversion from header row to InvoiceData."""
        result_invoice, result_operation = ExcelFieldMapper.header_row_to_invoice_data(sample_header_row)

        assert isinstance(result_invoice, InvoiceData)
        assert isinstance(result_operation, ManageInvoiceOperationType)
        assert result_invoice.invoice_number == "TEST-001"
        assert result_invoice.invoice_issue_date == "2024-01-15"
        
        # Test nested structures were created correctly
        assert result_invoice.invoice_main is not None
        assert result_invoice.invoice_main.invoice is not None
        assert result_invoice.invoice_main.invoice.invoice_head is not None

    def test_line_rows_to_invoice_lines_success(self, sample_line_rows):
        """Test successful conversion from line rows to LinesType."""
        result = ExcelFieldMapper.line_rows_to_invoice_lines(sample_line_rows)

        assert isinstance(result, LinesType)
        assert result.line is not None
        assert len(result.line) == 2
        assert all(isinstance(line, LineType) for line in result.line)

    def test_line_rows_to_invoice_lines_empty_list(self):
        """Test conversion with empty line rows."""
        result = ExcelFieldMapper.line_rows_to_invoice_lines([])
        assert result is None

    def test_format_date_various_inputs(self):
        """Test date formatting with various input types."""
        # Test string date
        result = ExcelFieldMapper._format_date("2024-01-15")
        assert result == "2024-01-15"

        # Test datetime object
        dt = datetime(2024, 1, 15)
        result = ExcelFieldMapper._format_date(dt)
        assert result == "2024-01-15"

        # Test date object
        d = date(2024, 1, 15)
        result = ExcelFieldMapper._format_date(d)
        assert result == "2024-01-15"

        # Test None
        result = ExcelFieldMapper._format_date(None)
        assert result is None

    def test_build_invoice_head_from_row(self, sample_header_row):
        """Test building InvoiceHeadType from header row."""
        result = ExcelFieldMapper._build_invoice_head_from_row(sample_header_row)

        assert isinstance(result, InvoiceHeadType)
        assert result.supplier_info is not None
        assert result.customer_info is not None
        assert result.invoice_detail is not None

    def test_build_invoice_summary_from_row(self, sample_header_row):
        """Test building SummaryType from header row."""
        result = ExcelFieldMapper._build_invoice_summary_from_row(sample_header_row)

        assert isinstance(result, SummaryType)
        assert result.summary_normal is not None
        assert result.summary_normal.invoice_net_amount == 2000.0

    def test_build_invoice_reference_from_row_with_modification_data(self):
        """Test building InvoiceReferenceType with modification data."""
        header_row = InvoiceHeaderRow(
            invoice_number="TEST-001",
            original_invoice_number="ORIG-001",
            modification_date="2024-01-20",
            modification_index=1
        )

        result = ExcelFieldMapper._build_invoice_reference_from_row(header_row)

        assert result is not None
        assert result.original_invoice_number == "ORIG-001"
        assert result.modification_index == 1

    def test_build_line_from_row(self, sample_line_rows):
        """Test building LineType from line row."""
        line_row = sample_line_rows[0]
        result = ExcelFieldMapper._build_line_from_row(line_row)

        assert isinstance(result, LineType)
        assert result.line_number == 1
        assert result.line_description == "Test Product 1"
        assert result.quantity == 1.0

    def test_build_address_from_seller_fields(self):
        """Test building AddressType from seller fields."""
        header_row = InvoiceHeaderRow(
            seller_country_code="HU",
            seller_postal_code="1234",
            seller_city="Budapest",
            seller_address_detail="Test street 1"
        )

        result = ExcelFieldMapper._build_address_from_seller_fields(header_row)

        assert isinstance(result, AddressType)
        assert result.simple_address is not None
        assert result.simple_address.country_code == "HU"
        assert result.simple_address.city == "Budapest"

    def test_build_address_from_buyer_fields(self):
        """Test building AddressType from buyer fields."""
        header_row = InvoiceHeaderRow(
            buyer_country_code="HU",
            buyer_postal_code="5678",
            buyer_city="Debrecen",
            buyer_address_detail="Buyer street 2"
        )

        result = ExcelFieldMapper._build_address_from_buyer_fields(header_row)

        assert isinstance(result, AddressType)
        assert result.simple_address is not None
        assert result.simple_address.country_code == "HU"
        assert result.simple_address.city == "Debrecen"

    def test_build_address_with_missing_required_fields(self):
        """Test address building with missing required fields."""
        header_row = InvoiceHeaderRow()  # No address fields set

        result = ExcelFieldMapper._build_address_from_seller_fields(header_row)
        assert result is None

    def test_map_address_to_seller(self):
        """Test mapping address to seller fields."""
        address = AddressType(
            simple_address=SimpleAddressType(
                country_code="HU",
                postal_code="1234",
                city="Budapest",
                additional_address_detail="Test street 1"
            )
        )
        
        row = InvoiceHeaderRow()
        ExcelFieldMapper._map_address_to_seller(address, row)

        assert row.seller_country_code == "HU"
        assert row.seller_postal_code == "1234"
        assert row.seller_city == "Budapest"
        assert row.seller_address_detail == "Test street 1"

    def test_map_address_to_buyer(self):
        """Test mapping address to buyer fields."""
        address = AddressType(
            simple_address=SimpleAddressType(
                country_code="HU",
                postal_code="5678",
                city="Debrecen",
                additional_address_detail="Buyer street 2"
            )
        )
        
        row = InvoiceHeaderRow()
        ExcelFieldMapper._map_address_to_buyer(address, row)

        assert row.buyer_country_code == "HU"
        assert row.buyer_postal_code == "5678"
        assert row.buyer_city == "Debrecen"
        assert row.buyer_address_detail == "Buyer street 2"

    def test_error_handling_in_mapping(self):
        """Test error handling in mapping functions."""
        # Test with invalid data that should raise ExcelMappingException
        invalid_invoice = "not an invoice object"

        with pytest.raises(ExcelMappingException):
            ExcelFieldMapper.invoice_data_to_header_row(invalid_invoice, ManageInvoiceOperationType.CREATE)

    def test_mapping_with_decimal_values(self):
        """Test mapping with Decimal values."""
        header_row = InvoiceHeaderRow(
            net_amount_original=Decimal("1000.50"),
            vat_amount_original=Decimal("270.14"),
            gross_amount_original=Decimal("1270.64")
        )

        # Test that Decimal values are handled correctly
        assert header_row.net_amount_original == Decimal("1000.50")
        assert header_row.vat_amount_original == Decimal("270.14")

    def test_nested_structure_reconstruction_completeness(self, sample_header_row, sample_line_rows):
        """Test that nested structure reconstruction is complete."""
        invoice_data, operation_type = ExcelFieldMapper.header_row_to_invoice_data(sample_header_row)
        lines_type = ExcelFieldMapper.line_rows_to_invoice_lines(sample_line_rows)

        # Add lines to invoice
        if invoice_data.invoice_main and invoice_data.invoice_main.invoice:
            invoice_data.invoice_main.invoice.invoice_lines = lines_type

        # Verify complete structure exists
        assert invoice_data.invoice_main is not None
        assert invoice_data.invoice_main.invoice is not None
        assert invoice_data.invoice_main.invoice.invoice_head is not None
        assert invoice_data.invoice_main.invoice.invoice_head.supplier_info is not None
        assert invoice_data.invoice_main.invoice.invoice_head.customer_info is not None
        assert invoice_data.invoice_main.invoice.invoice_summary is not None
        assert invoice_data.invoice_main.invoice.invoice_lines is not None

    def test_roundtrip_mapping_consistency(self, sample_invoice_data):
        """Test that forward and reverse mapping are consistent."""
        # Forward mapping: InvoiceData -> Excel rows
        header_row = ExcelFieldMapper.invoice_data_to_header_row(
            sample_invoice_data, ManageInvoiceOperationType.CREATE
        )
        line_rows = ExcelFieldMapper.invoice_data_to_line_rows(sample_invoice_data, ManageInvoiceOperationType.CREATE)

        # Reverse mapping: Excel rows -> InvoiceData
        reconstructed_invoice, operation_type = ExcelFieldMapper.header_row_to_invoice_data(header_row)
        lines_type = ExcelFieldMapper.line_rows_to_invoice_lines(line_rows)

        # Basic consistency checks
        assert reconstructed_invoice.invoice_number == sample_invoice_data.invoice_number
        assert reconstructed_invoice.invoice_issue_date == sample_invoice_data.invoice_issue_date
        assert operation_type == ManageInvoiceOperationType.CREATE