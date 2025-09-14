"""
Unit tests for Excel exceptions.
"""

import pytest

from nav_online_szamla.excel.exceptions import (
    ExcelProcessingException,
    ExcelValidationException,
    ExcelStructureException,
    ExcelMappingException,
    ExcelImportException
)


class TestExcelExceptions:
    """Test cases for Excel-related exceptions."""

    def test_excel_processing_exception(self):
        """Test ExcelProcessingException creation and inheritance."""
        message = "Processing failed"
        exception = ExcelProcessingException(message)
        
        assert str(exception) == message
        assert isinstance(exception, Exception)
        
        # Test raising the exception
        with pytest.raises(ExcelProcessingException, match=message):
            raise ExcelProcessingException(message)

    def test_excel_validation_exception(self):
        """Test ExcelValidationException creation and inheritance."""
        message = "Validation failed"
        exception = ExcelValidationException(message)
        
        assert str(exception) == message
        assert isinstance(exception, ExcelProcessingException)
        assert isinstance(exception, Exception)
        
        # Test raising the exception
        with pytest.raises(ExcelValidationException, match=message):
            raise ExcelValidationException(message)

    def test_excel_structure_exception(self):
        """Test ExcelStructureException creation and inheritance."""
        message = "Invalid Excel structure"
        exception = ExcelStructureException(message)
        
        assert str(exception) == message
        assert isinstance(exception, ExcelProcessingException)
        assert isinstance(exception, Exception)
        
        # Test raising the exception
        with pytest.raises(ExcelStructureException, match=message):
            raise ExcelStructureException(message)

    def test_excel_mapping_exception(self):
        """Test ExcelMappingException creation and inheritance."""
        message = "Mapping failed"
        exception = ExcelMappingException(message)
        
        assert str(exception) == message
        assert isinstance(exception, ExcelProcessingException)
        assert isinstance(exception, Exception)
        
        # Test raising the exception
        with pytest.raises(ExcelMappingException, match=message):
            raise ExcelMappingException(message)

    def test_excel_import_exception(self):
        """Test ExcelImportException creation and inheritance."""
        message = "Import failed"
        exception = ExcelImportException(message)
        
        assert str(exception) == message
        assert isinstance(exception, ExcelProcessingException)
        assert isinstance(exception, Exception)
        
        # Test raising the exception
        with pytest.raises(ExcelImportException, match=message):
            raise ExcelImportException(message)

    def test_exception_chaining(self):
        """Test exception chaining with from clause."""
        original_exception = ValueError("Original error")
        
        try:
            raise original_exception
        except ValueError as e:
            try:
                raise ExcelProcessingException("Processing failed") from e
            except ExcelProcessingException as chained_exception:
                assert str(chained_exception) == "Processing failed"
                assert chained_exception.__cause__ == original_exception

    def test_exception_with_details(self):
        """Test exceptions with detailed error information."""
        details = {
            'file_path': 'test.xlsx',
            'sheet_name': 'Fejléc adatok',
            'row_number': 5,
            'column_name': 'invoice_number'
        }
        
        message = f"Validation error in {details['sheet_name']} at row {details['row_number']}"
        exception = ExcelValidationException(message)
        
        # You could extend exceptions to store details
        exception.details = details
        
        assert hasattr(exception, 'details')
        assert exception.details['file_path'] == 'test.xlsx'

    def test_exception_hierarchy(self):
        """Test that exception hierarchy is correctly established."""
        # All Excel exceptions should inherit from ExcelProcessingException
        validation_exc = ExcelValidationException("test")
        structure_exc = ExcelStructureException("test")
        mapping_exc = ExcelMappingException("test")
        import_exc = ExcelImportException("test")
        
        # Test inheritance chain
        assert isinstance(validation_exc, ExcelProcessingException)
        assert isinstance(structure_exc, ExcelProcessingException)
        assert isinstance(mapping_exc, ExcelProcessingException)
        assert isinstance(import_exc, ExcelProcessingException)
        
        # Test that they're all Exceptions
        assert isinstance(validation_exc, Exception)
        assert isinstance(structure_exc, Exception)
        assert isinstance(mapping_exc, Exception)
        assert isinstance(import_exc, Exception)

    def test_catching_base_exception(self):
        """Test that base exception can catch all derived exceptions."""
        exceptions_to_test = [
            ExcelValidationException("validation error"),
            ExcelStructureException("structure error"),
            ExcelMappingException("mapping error"),
            ExcelImportException("import error")
        ]
        
        for exc in exceptions_to_test:
            with pytest.raises(ExcelProcessingException):
                raise exc

    def test_exception_message_formatting(self):
        """Test different ways of formatting exception messages."""
        # Simple string message
        exc1 = ExcelProcessingException("Simple error")
        assert str(exc1) == "Simple error"
        
        # Formatted string message
        file_name = "test.xlsx"
        exc2 = ExcelProcessingException(f"Error processing file: {file_name}")
        assert str(exc2) == "Error processing file: test.xlsx"
        
        # Multi-line message
        exc3 = ExcelProcessingException("Error occurred:\n- Invalid data\n- Missing columns")
        assert "Error occurred:" in str(exc3)
        assert "Invalid data" in str(exc3)

    def test_exception_without_message(self):
        """Test exceptions created without explicit message."""
        # Some exceptions might be raised without a message
        exc = ExcelProcessingException()
        # Should not raise an error when converted to string
        str_repr = str(exc)
        assert isinstance(str_repr, str)

    def test_exception_with_args(self):
        """Test exceptions with multiple arguments."""
        args = ("Error type", "test.xlsx", 42)
        exc = ExcelProcessingException(*args)
        
        assert exc.args == args
        # First argument typically becomes the message
        assert "Error type" in str(exc)

    def test_specific_exception_scenarios(self):
        """Test specific scenarios where each exception type would be used."""
        
        # ExcelValidationException: Data validation fails
        with pytest.raises(ExcelValidationException):
            raise ExcelValidationException("Invoice number is required but missing")
        
        # ExcelStructureException: File structure is wrong
        with pytest.raises(ExcelStructureException):
            raise ExcelStructureException("Required sheet 'Fejléc adatok' not found")
        
        # ExcelMappingException: Field mapping fails
        with pytest.raises(ExcelMappingException):
            raise ExcelMappingException("Cannot map field 'unknown_field' to invoice data")
        
        # ExcelImportException: Import process fails
        with pytest.raises(ExcelImportException):
            raise ExcelImportException("Failed to convert Excel data to InvoiceData objects")
        
        # ExcelProcessingException: General processing error
        with pytest.raises(ExcelProcessingException):
            raise ExcelProcessingException("Unable to read Excel file due to corruption")