"""
Unit tests for Excel exporter functionality.
"""

import pytest
import pandas as pd
from pathlib import Path
from decimal import Decimal
from unittest.mock import Mock, patch, mock_open

from nav_online_szamla.excel.exporter import InvoiceExcelExporter
from nav_online_szamla.excel.exceptions import ExcelProcessingException
from nav_online_szamla.models import InvoiceData, ManageInvoiceOperationType
from nav_online_szamla.models.invoice_data import (
    InvoiceMainType, InvoiceType, InvoiceHeadType, SupplierInfoType,
    CustomerInfoType, LinesType, LineType, SummaryType, InvoiceDetailType,
    SummaryNormalType, CustomerVatDataType, CustomerTaxNumberType
)
from nav_online_szamla.models.invoice_base import TaxNumberType, AddressType, SimpleAddressType


class TestInvoiceExcelExporter:
    """Test cases for InvoiceExcelExporter."""

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
            third_state_tax_id=None
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

        # Create line items with proper structure
        from nav_online_szamla.models.invoice_data import (
            LineAmountsNormalType, LineNetAmountDataType, LineVatDataType, 
            LineGrossAmountDataType, VatRateType, UnitOfMeasureType
        )
        
        # Create line amount structure
        line_net_amount_data = LineNetAmountDataType(
            line_net_amount=Decimal("1000.0"),
            line_net_amount_huf=Decimal("1000.0")
        )
        
        vat_rate = VatRateType(vat_percentage=Decimal("27.0"))
        
        line_vat_data = LineVatDataType(
            line_vat_amount=Decimal("270.0"),
            line_vat_amount_huf=Decimal("270.0")
        )
        
        line_gross_amount_data = LineGrossAmountDataType(
            line_gross_amount_normal=Decimal("1270.0"),
            line_gross_amount_normal_huf=Decimal("1270.0")
        )
        
        line_amounts_normal = LineAmountsNormalType(
            line_net_amount_data=line_net_amount_data,
            line_vat_rate=vat_rate,
            line_vat_data=line_vat_data,
            line_gross_amount_data=line_gross_amount_data
        )
        
        line = LineType(
            line_number=1,
            line_expression_indicator=True,
            line_description="Test Product",
            quantity=Decimal("1.0"),
            unit_of_measure=UnitOfMeasureType.PIECE,
            unit_price=Decimal("1000.0"),
            line_amounts_normal=line_amounts_normal
        )
        lines = LinesType(line=[line], merged_item_indicator=False)

        # Create summary
        summary_normal = SummaryNormalType(
            invoice_net_amount=Decimal("1000.0"),
            invoice_net_amount_huf=Decimal("1000.0"),
            invoice_vat_amount=Decimal("270.0"),
            invoice_vat_amount_huf=Decimal("270.0"),
            summary_by_vat_rate=[]
        )
        summary = SummaryType(
            summary_normal=summary_normal
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
    def exporter(self):
        """Create InvoiceExcelExporter instance."""
        return InvoiceExcelExporter()

    def test_exporter_initialization(self, exporter):
        """Test that exporter initializes correctly."""
        assert isinstance(exporter, InvoiceExcelExporter)

    def test_export_to_excel_success(self, exporter, sample_invoice_data, temp_excel_file):
        """Test successful export to Excel."""
        # Create invoice list with operation type
        invoice_list = [(sample_invoice_data, ManageInvoiceOperationType.CREATE)]
        
        # Test export - should complete without exception
        exporter.export_to_excel(invoice_list, temp_excel_file)
        
        # Verify file was created
        assert Path(temp_excel_file).exists()
        assert Path(temp_excel_file).stat().st_size > 0  # File should not be empty

    def test_export_empty_invoice_list(self, exporter):
        """Test export with empty invoice list."""
        with pytest.raises(ExcelProcessingException, match="No invoice data provided"):
            exporter.export_to_excel([], "test.xlsx")

    def test_export_invalid_invoice_data(self, exporter):
        """Test export with invalid invoice data."""
        invalid_data = "not an invoice"
        with pytest.raises(ExcelProcessingException):
            exporter.export_to_excel([(invalid_data, ManageInvoiceOperationType.CREATE)], "test.xlsx")

    @patch('nav_online_szamla.excel.exporter.ExcelFieldMapper.invoice_data_to_header_row')
    def test_mapping_error_handling(self, mock_mapper, exporter, sample_invoice_data):
        """Test error handling in field mapping."""
        # Setup mock to raise exception
        mock_mapper.side_effect = Exception("Mapping failed")

        invoice_list = [(sample_invoice_data, ManageInvoiceOperationType.CREATE)]

        with patch('nav_online_szamla.excel.exporter.pd.ExcelWriter'):
            exporter.export_to_excel(invoice_list, "test.xlsx")
            # Should handle the error gracefully and continue

    def test_create_template_excel(self, exporter):
        """Test creation of template Excel file."""
        with patch('nav_online_szamla.excel.exporter.Workbook') as mock_workbook:
            mock_wb_instance = Mock()
            mock_wb_instance.sheetnames = ['Sheet']
            
            # Mock the sheet that gets removed
            mock_default_sheet = Mock()
            # Configure __getitem__ to return the mock sheet
            mock_wb_instance.__getitem__ = Mock(return_value=mock_default_sheet)
            
            # Mock create_sheet for header and line sheets
            mock_header_ws = Mock()
            mock_line_ws = Mock()
            mock_wb_instance.create_sheet.side_effect = [mock_header_ws, mock_line_ws]
            
            mock_workbook.return_value = mock_wb_instance

            exporter.create_template_excel("template.xlsx")

            # Verify workbook was created and saved
            mock_workbook.assert_called_once()
            mock_wb_instance.save.assert_called_once_with("template.xlsx")

    def test_validate_file_path(self, exporter):
        """Test file path validation."""
        # Test with valid path
        valid_path = "test.xlsx"
        # Should not raise exception
        exporter._validate_file_path(valid_path)

        # Test with invalid extension
        with pytest.raises(ExcelProcessingException, match="File must have .xlsx extension"):
            exporter._validate_file_path("test.xls")

    def test_format_datetime_for_excel(self, exporter):
        """Test datetime formatting for Excel."""
        # Test with string date
        result = exporter._format_datetime_for_excel("2024-01-15")
        assert isinstance(result, pd.Timestamp)

        # Test with None
        result = exporter._format_datetime_for_excel(None)
        assert result is None

    def test_format_decimal_for_excel(self, exporter):
        """Test decimal formatting for Excel."""
        # Test with Decimal
        result = exporter._format_decimal_for_excel(Decimal("123.45"))
        assert result == 123.45

        # Test with None
        result = exporter._format_decimal_for_excel(None)
        assert result is None

        # Test with string number
        result = exporter._format_decimal_for_excel("123.45")
        assert result == 123.45

    @patch('builtins.open', new_callable=mock_open)
    @patch('nav_online_szamla.excel.exporter.Workbook')
    def test_export_file_creation(self, mock_workbook, mock_file, exporter, sample_invoice_data):
        """Test that export creates file correctly."""
        mock_wb_instance = Mock()
        mock_wb_instance.sheetnames = ['Sheet']
        
        # Mock the sheet that gets removed
        mock_default_sheet = Mock()
        mock_wb_instance.__getitem__ = Mock(return_value=mock_default_sheet)
        
        # Mock create_sheet for header and line sheets
        mock_header_ws = Mock()
        mock_line_ws = Mock()
        mock_wb_instance.create_sheet.side_effect = [mock_header_ws, mock_line_ws]
        
        mock_workbook.return_value = mock_wb_instance

        invoice_list = [(sample_invoice_data, ManageInvoiceOperationType.CREATE)]
        file_path = "test_output.xlsx"

        exporter.export_to_excel(invoice_list, file_path)

        # Verify workbook was created and saved
        mock_workbook.assert_called_once()
        mock_wb_instance.save.assert_called_once_with(file_path)

    def test_multiple_invoices_export(self, exporter, sample_invoice_data):
        """Test export with multiple invoices."""
        # Create second invoice
        invoice_data_2 = sample_invoice_data
        invoice_data_2.invoice_number = "TEST-002"

        invoice_list = [
            (sample_invoice_data, ManageInvoiceOperationType.CREATE),
            (invoice_data_2, ManageInvoiceOperationType.MODIFY)
        ]

        with patch('nav_online_szamla.excel.exporter.pd.ExcelWriter'):
            # Should not raise exception
            exporter.export_to_excel(invoice_list, "multi_test.xlsx")

    def test_column_mappings_completeness(self, exporter):
        """Test that all required column mappings are present."""
        from nav_online_szamla.excel.mapper import ExcelFieldMapper
        
        header_mappings = ExcelFieldMapper.HEADER_COLUMN_MAPPINGS
        line_mappings = ExcelFieldMapper.LINE_COLUMN_MAPPINGS
        
        # Check that mappings are not empty
        assert len(header_mappings) > 0
        assert len(line_mappings) > 0
        
        # Check for essential fields
        essential_header_fields = [
            'invoice_number', 'invoice_issue_date', 'seller_name', 
            'buyer_name', 'net_amount_original', 'gross_amount_original'
        ]
        
        for field in essential_header_fields:
            assert field in [v for v in header_mappings.values()]

    def test_error_logging(self, exporter, caplog):
        """Test that errors are properly logged."""
        with patch('nav_online_szamla.excel.exporter.ExcelFieldMapper.invoice_data_to_header_row') as mock_mapper:
            mock_mapper.side_effect = Exception("Test mapping error")

            with patch('nav_online_szamla.excel.exporter.Workbook'):
                invoice_list = [("invalid", ManageInvoiceOperationType.CREATE)]
                with pytest.raises(ExcelProcessingException):
                    exporter.export_to_excel(invoice_list, "error_test.xlsx")

                # Check that error was logged
                assert "Failed to convert header data for unknown" in caplog.text