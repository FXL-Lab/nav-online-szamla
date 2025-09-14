"""
Unit tests for Excel importer functionality.
"""

import pytest
import pandas as pd
from pathlib import Path
from decimal import Decimal
from unittest.mock import Mock, patch, MagicMock
from io import StringIO

from nav_online_szamla.excel.importer import InvoiceExcelImporter
from nav_online_szamla.excel.exceptions import (
    ExcelProcessingException, ExcelValidationException, 
    ExcelStructureException, ExcelImportException
)
from nav_online_szamla.excel.models import InvoiceHeaderRow, InvoiceLineRow
from nav_online_szamla.models import InvoiceData, ManageInvoiceOperationType


class TestInvoiceExcelImporter:
    """Test cases for InvoiceExcelImporter."""

    @pytest.fixture
    def importer(self):
        """Create InvoiceExcelImporter instance."""
        return InvoiceExcelImporter()

    @pytest.fixture
    def sample_header_df(self):
        """Create sample header DataFrame for testing."""
        data = {
            'Számla sorszáma': ['TEST-001', 'TEST-002'],
            'Számla kelte': ['2024-01-15', '2024-01-16'],
            'Teljességi mutató': [True, True],
            'Eladó neve': ['Test Supplier', 'Another Supplier'],
            'Eladó adószáma (törzsszám)': ['12345678', '87654321'],
            'Eladó adószáma (ÁFA-kód)': ['2', '2'],
            'Eladó adószáma (megyekód)': ['01', '02'],
            'Eladó országkódja': ['HU', 'HU'],
            'Eladó irányítószáma': ['1234', '5678'],
            'Eladó településneve': ['Budapest', 'Debrecen'],
            'Eladó címének részletes adatai': ['Test street 1', 'Another street 2'],
            'Vevő neve': ['Test Customer', 'Another Customer'],
            'Vevő adószáma (törzsszám)': ['11111111', '22222222'],
            'Vevő adószáma (ÁFA-kód)': ['2', '2'],
            'Vevő adószáma (megyekód)': ['03', '04'],
            'Vevő országkódja': ['HU', 'HU'],
            'Vevő irányítószáma': ['9876', '5432'],
            'Vevő településneve': ['Szeged', 'Pécs'],
            'Vevő címének részletes adatai': ['Buyer street 1', 'Customer street 2'],
            'Vevő ÁFA státusza': ['DOMESTIC', 'DOMESTIC'],
            'Vevő közösségi adószáma': ['HU11111111', 'HU22222222'],
            'Vevő harmadik országbeli adószáma': [None, None],
            'Teljesítés dátuma': ['2024-01-15', '2024-01-16'],
            'Fizetési határidő': ['2024-02-15', '2024-02-16'],
            'Fizetési mód': ['TRANSFER', 'CASH'],
            'Számla pénzneme': ['HUF', 'HUF'],
            'Alkalmazott árfolyam': [1.0, 1.0],
            'Kisadózó jelzése': [False, False],
            'Pénzforgalmi elszámolás jelzése': [False, False],
            'Számla kategória': ['NORMAL', 'NORMAL'],
            'Eredeti számla sorszáma': [None, 'ORIG-001'],
            'Módosítás dátuma': [None, '2024-01-20'],
            'Módosítási index': [None, 1],
            'Nettó összeg (eredeti pénznem)': [1000.0, 2000.0],
            'Nettó összeg (HUF)': [1000.0, 2000.0],
            'ÁFA összege (eredeti pénznem)': [270.0, 540.0],
            'ÁFA összege (HUF)': [270.0, 540.0],
            'Bruttó összeg (eredeti pénznem)': [1270.0, 2540.0],
            'Bruttó összeg (HUF)': [1270.0, 2540.0]
        }
        return pd.DataFrame(data)

    @pytest.fixture
    def sample_lines_df(self):
        """Create sample lines DataFrame for testing."""
        data = {
            'Számla sorszáma': ['TEST-001', 'TEST-001', 'TEST-002'],
            'Tétel sorszáma': [1, 2, 1],
            'Tétel módosítás típusa': ['CREATE', 'CREATE', 'CREATE'],
            'Megnevezés': ['Product 1', 'Product 2', 'Service 1'],
            'Mennyiség': [1.0, 2.0, 1.0],
            'Mennyiségi egység': ['PIECE', 'PIECE', 'HOUR'],
            'Egységár': [1000.0, 500.0, 2000.0],
            'Nettó összeg (eredeti pénznem)': [1000.0, 1000.0, 2000.0],
            'Nettó összeg (HUF)': [1000.0, 1000.0, 2000.0],
            'ÁFA kulcs': [27.0, 27.0, 27.0],
            'ÁFA összege (eredeti pénznem)': [270.0, 270.0, 540.0],
            'ÁFA összege (HUF)': [270.0, 270.0, 540.0],
            'Bruttó összeg (eredeti pénznem)': [1270.0, 1270.0, 2540.0],
            'Bruttó összeg (HUF)': [1270.0, 1270.0, 2540.0]
        }
        return pd.DataFrame(data)

    @pytest.fixture
    def sample_excel_file_content(self, sample_header_df, sample_lines_df):
        """Create mock Excel file content."""
        return {
            'Fejléc adatok': sample_header_df,
            'Tétel adatok': sample_lines_df
        }

    def test_importer_initialization(self, importer):
        """Test that importer initializes correctly."""
        assert isinstance(importer, InvoiceExcelImporter)

    def test_import_from_excel_success(self, importer, sample_excel_file_content):
        """Test successful import from Excel."""
        with patch('pandas.read_excel') as mock_read_excel:
            # Configure mock to return sample data
            def mock_read_excel_side_effect(file_path, sheet_name, **kwargs):
                if sheet_name is None:
                    # Return all sheets as dict when sheet_name=None
                    return sample_excel_file_content
                return sample_excel_file_content[sheet_name]
            
            mock_read_excel.side_effect = mock_read_excel_side_effect

            # Test import
            result = importer.import_from_excel("test.xlsx")

            # Verify result
            assert isinstance(result, list)
            assert len(result) == 2  # Two invoices
            
            for invoice_data, operation_type in result:
                assert isinstance(invoice_data, InvoiceData)
                assert isinstance(operation_type, ManageInvoiceOperationType)
                assert invoice_data.invoice_number in ['TEST-001', 'TEST-002']

    def test_import_nonexistent_file(self, importer):
        """Test import with non-existent file."""
        with patch('pathlib.Path.exists', return_value=False):
            with pytest.raises(ExcelProcessingException, match="File does not exist"):
                importer.import_from_excel("nonexistent.xlsx")

    def test_import_invalid_file_extension(self, importer):
        """Test import with invalid file extension."""
        with pytest.raises(ExcelProcessingException, match="File must have .xlsx extension"):
            importer.import_from_excel("test.xls")

    @patch('pandas.read_excel')
    def test_import_missing_required_sheets(self, mock_read_excel, importer):
        """Test import with missing required sheets."""
        # Mock read_excel to raise exception for missing sheet
        mock_read_excel.side_effect = ValueError("Worksheet named 'Fejléc adatok' not found")

        with pytest.raises(ExcelStructureException, match="Required sheet 'Fejléc adatok' not found"):
            importer.import_from_excel("test.xlsx")

    def test_validate_excel_structure_success(self, importer, sample_header_df, sample_lines_df):
        """Test successful Excel structure validation."""
        # Should not raise exception
        importer._validate_excel_structure(sample_header_df, sample_lines_df)

    def test_validate_excel_structure_missing_columns(self, importer):
        """Test Excel structure validation with missing columns."""
        # Create DataFrame missing required columns
        invalid_header_df = pd.DataFrame({'invoice_number': ['TEST-001']})
        lines_df = pd.DataFrame()

        with pytest.raises(ExcelValidationException, match="Missing required header columns"):
            importer._validate_excel_structure(invalid_header_df, lines_df)

    def test_parse_header_sheet_success(self, importer, sample_header_df):
        """Test successful header sheet parsing."""
        result = importer._parse_header_sheet(sample_header_df)
        
        assert isinstance(result, list)
        assert len(result) == 2
        
        for header_row in result:
            assert isinstance(header_row, InvoiceHeaderRow)
            assert header_row.invoice_number in ['TEST-001', 'TEST-002']

    def test_parse_header_sheet_empty_df(self, importer):
        """Test header sheet parsing with empty DataFrame."""
        empty_df = pd.DataFrame()
        result = importer._parse_header_sheet(empty_df)
        assert result == []

    def test_parse_lines_sheet_success(self, importer, sample_lines_df):
        """Test successful lines sheet parsing."""
        result = importer._parse_lines_sheet(sample_lines_df)
        
        assert isinstance(result, dict)
        assert 'TEST-001' in result
        assert 'TEST-002' in result
        assert len(result['TEST-001']) == 2  # Two lines for TEST-001
        assert len(result['TEST-002']) == 1   # One line for TEST-002

    def test_parse_lines_sheet_empty_df(self, importer):
        """Test lines sheet parsing with empty DataFrame."""
        empty_df = pd.DataFrame()
        result = importer._parse_lines_sheet(empty_df)
        assert result == {}

    def test_convert_to_invoice_data_success(self, importer):
        """Test successful conversion to InvoiceData."""
        # Create sample header and line rows
        header_row = InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            completeness_indicator=True,
            seller_name="Test Supplier",
            buyer_name="Test Customer",
            net_amount_original=1000.0,
            gross_amount_original=1270.0
        )
        
        line_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            description="Test Product",
            quantity=1.0,
            unit_price=1000.0,
            net_amount_original=1000.0,
            gross_amount_original=1270.0
        )

        with patch('nav_online_szamla.excel.mapper.ExcelFieldMapper.header_row_to_invoice_data') as mock_header_mapper:
            with patch('nav_online_szamla.excel.mapper.ExcelFieldMapper.line_rows_to_invoice_lines') as mock_lines_mapper:
                # Mock return values
                mock_invoice_data = Mock(spec=InvoiceData)
                mock_invoice_data.invoice_number = "TEST-001"
                mock_invoice_data.invoice_main = Mock()
                mock_invoice_data.invoice_main.invoice = Mock()
                
                mock_header_mapper.return_value = (mock_invoice_data, ManageInvoiceOperationType.CREATE)
                mock_lines_mapper.return_value = Mock()

                # Test conversion
                result_invoice, result_operation = importer._convert_to_invoice_data(header_row, [line_row])

                # Verify result
                assert result_invoice == mock_invoice_data
                assert result_operation == ManageInvoiceOperationType.CREATE

    def test_convert_value_for_header_field_date(self, importer):
        """Test date field conversion."""
        # Test string date
        result = importer._convert_value_for_header_field('invoice_issue_date', '2024-01-15')
        assert result == '2024-01-15'

        # Test pandas timestamp
        timestamp = pd.Timestamp('2024-01-15')
        result = importer._convert_value_for_header_field('invoice_issue_date', timestamp)
        assert result == '2024-01-15'

    def test_convert_value_for_header_field_decimal(self, importer):
        """Test decimal field conversion."""
        result = importer._convert_value_for_header_field('net_amount_original', '1000.50')
        assert isinstance(result, Decimal)
        assert result == Decimal('1000.50')

    def test_convert_value_for_header_field_boolean(self, importer):
        """Test boolean field conversion."""
        # Test various boolean representations
        assert importer._convert_value_for_header_field('completeness_indicator', True) is True
        assert importer._convert_value_for_header_field('completeness_indicator', 'True') is True
        assert importer._convert_value_for_header_field('completeness_indicator', 1) is True
        assert importer._convert_value_for_header_field('completeness_indicator', False) is False

    def test_convert_value_for_line_field_integer(self, importer):
        """Test integer field conversion."""
        result = importer._convert_value_for_line_field('line_number', '5')
        assert result == 5
        assert isinstance(result, int)

    def test_convert_value_for_line_field_decimal(self, importer):
        """Test line decimal field conversion."""
        result = importer._convert_value_for_line_field('quantity', '2.5')
        assert isinstance(result, Decimal)
        assert result == Decimal('2.5')

    def test_is_date_field(self, importer):
        """Test date field identification."""
        assert importer._is_date_field('invoice_issue_date') is True
        assert importer._is_date_field('payment_due_date') is True
        assert importer._is_date_field('invoice_number') is False

    def test_is_decimal_field(self, importer):
        """Test decimal field identification."""
        assert importer._is_decimal_field('net_amount_original') is True
        assert importer._is_decimal_field('vat_amount_huf') is True
        assert importer._is_decimal_field('invoice_number') is False

    def test_is_boolean_field(self, importer):
        """Test boolean field identification."""
        assert importer._is_boolean_field('completeness_indicator') is True
        assert importer._is_boolean_field('small_business_indicator') is True
        assert importer._is_boolean_field('invoice_number') is False

    def test_is_integer_field(self, importer):
        """Test integer field identification."""
        assert importer._is_integer_field('line_number') is True
        assert importer._is_integer_field('modification_index') is True
        assert importer._is_integer_field('description') is False

    @patch('pandas.read_excel')
    def test_read_excel_file_pandas_error(self, mock_read_excel, importer):
        """Test Excel file reading with pandas error."""
        mock_read_excel.side_effect = Exception("Pandas read error")

        with pytest.raises(ExcelProcessingException, match="Failed to read Excel file"):
            importer.import_from_excel("test.xlsx")

    def test_header_row_validation_missing_invoice_number(self, importer):
        """Test header row validation with missing invoice number."""
        invalid_data = {'invoice_issue_date': '2024-01-15'}
        
        with pytest.raises(ExcelValidationException):
            importer._create_header_row_from_dict(invalid_data)

    def test_line_row_validation_missing_required_fields(self, importer):
        """Test line row validation with missing required fields."""
        invalid_data = {'invoice_number': 'TEST-001'}  # Missing line_number
        
        with pytest.raises(ExcelValidationException):
            importer._create_line_row_from_dict(invalid_data)

    def test_import_with_data_conversion_error(self, importer, sample_excel_file_content):
        """Test import handling data conversion errors."""
        with patch('pandas.read_excel') as mock_read_excel:
            def mock_read_excel_side_effect(file_path, sheet_name, **kwargs):
                if sheet_name is None:
                    # Return all sheets as dict when sheet_name=None
                    return sample_excel_file_content
                return sample_excel_file_content[sheet_name]
            
            mock_read_excel.side_effect = mock_read_excel_side_effect

            with patch.object(importer, '_convert_to_invoice_data') as mock_convert:
                mock_convert.side_effect = ExcelImportException("Conversion failed")

                result = importer.import_from_excel("test.xlsx")
                # Should handle the error gracefully
                assert isinstance(result, list)

    def test_empty_sheets_handling(self, importer):
        """Test handling of empty sheets."""
        empty_header_df = pd.DataFrame()
        empty_lines_df = pd.DataFrame()

        with patch('pandas.read_excel') as mock_read_excel:
            def mock_side_effect(file_path, sheet_name, **kwargs):
                if sheet_name is None:
                    return {
                        'Fejléc adatok': empty_header_df,
                        'Tétel adatok': empty_lines_df
                    }
                return empty_header_df if sheet_name == 'Fejléc adatok' else empty_lines_df
                
            mock_read_excel.side_effect = mock_side_effect

            result = importer.import_from_excel("test.xlsx")
            assert result == []  # Should return empty list