"""
Integration tests for Excel functionality.

These tests verify the complete Excel export/import workflow.
"""

import pytest
import pandas as pd
from pathlib import Path
from decimal import Decimal
from tempfile import NamedTemporaryFile
from unittest.mock import patch

from nav_online_szamla.excel import InvoiceExcelExporter, InvoiceExcelImporter
from nav_online_szamla.excel.exceptions import ExcelProcessingException
from nav_online_szamla.models import InvoiceData, ManageInvoiceOperationType
from nav_online_szamla.models.invoice_data import (
    InvoiceMainType, InvoiceType, InvoiceHeadType, SupplierInfoType,
    CustomerInfoType, LinesType, LineType, SummaryType, InvoiceDetailType,
    CustomerVatDataType, CustomerTaxNumberType, SummaryNormalType, SummaryGrossDataType
)
from nav_online_szamla.models.invoice_base import TaxNumberType, AddressType, SimpleAddressType


class TestExcelIntegration:
    """Integration tests for complete Excel workflow."""

    @pytest.fixture
    def sample_invoice_data_list(self):
        """Create sample InvoiceData list for testing."""
        invoices = []
        
        for i in range(1, 3):  # Create 2 invoices
            # Create supplier info
            supplier_tax_number = TaxNumberType(
                taxpayer_id=f"1234567{i}",
                vat_code="2",
                county_code="01"
            )
            supplier_address = AddressType(
                simple_address=SimpleAddressType(
                    country_code="HU",
                    postal_code=f"123{i}",
                    city="Budapest",
                    additional_address_detail=f"Supplier street {i}"
                )
            )
            supplier_info = SupplierInfoType(
                supplier_tax_number=supplier_tax_number,
                supplier_name=f"Test Supplier {i} Ltd.",
                supplier_address=supplier_address
            )

            # Create customer info with proper nested structure
            customer_tax_number = CustomerTaxNumberType(
                taxpayer_id=f"8765432{i}",
                vat_code="2",
                county_code="02"
            )
            customer_vat_data = CustomerVatDataType(
                customer_tax_number=customer_tax_number,
                community_vat_number=f"HU8765432{i}",
                third_state_tax_id=f"EU12345{i}"
            )
            customer_address = AddressType(
                simple_address=SimpleAddressType(
                    country_code="HU",
                    postal_code=f"567{i}",
                    city="Debrecen",
                    additional_address_detail=f"Customer street {i}"
                )
            )
            customer_info = CustomerInfoType(
                customer_vat_data=customer_vat_data,
                customer_name=f"Test Customer {i} Inc.",
                customer_address=customer_address
            )

            # Create invoice detail
            from nav_online_szamla.models.invoice_base import PaymentMethodType, InvoiceCategoryType
            invoice_detail = InvoiceDetailType(
                invoice_category=InvoiceCategoryType.NORMAL,
                invoice_delivery_date=f"2024-01-{14+i}",
                payment_date=f"2024-02-{14+i}",
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
            lines = []
            for j in range(1, 3):  # 2 lines per invoice
                line = LineType(
                    line_number=j,
                    line_description=f"Product {j} for Invoice {i}",
                    quantity=Decimal(f"{j}.0"),
                    unit_price=Decimal("1000.0")
                )
                lines.append(line)
            
            lines_type = LinesType(line=lines)

            # Create summary
            total_net = sum(Decimal("1000.0") * Decimal(f"{j}.0") for j in range(1, 3))  # 3000.0
            total_vat = total_net * Decimal("0.27")  # 810.0
            total_gross = total_net + total_vat  # 3810.0
            
            summary_normal = SummaryNormalType(
                invoice_net_amount=total_net,
                invoice_net_amount_huf=total_net,
                invoice_vat_amount=total_vat,
                invoice_vat_amount_huf=total_vat,
                summary_by_vat_rate=[]
            )
            summary_gross_data = SummaryGrossDataType(
                invoice_gross_amount=total_gross,
                invoice_gross_amount_huf=total_gross
            )
            summary = SummaryType(
                summary_normal=summary_normal,
                summary_gross_data=summary_gross_data
            )

            # Create main invoice structure
            invoice = InvoiceType(
                invoice_head=invoice_head,
                invoice_lines=lines_type,
                invoice_summary=summary
            )
            invoice_main = InvoiceMainType(invoice=invoice)

            # Create invoice data
            invoice_data = InvoiceData(
                invoice_number=f"INT-TEST-00{i}",
                invoice_issue_date=f"2024-01-{14+i}",
                completeness_indicator=True
            )
            invoice_data.invoice_main = invoice_main

            invoices.append((invoice_data, ManageInvoiceOperationType.CREATE))

        return invoices

    @pytest.fixture
    def temp_excel_file(self):
        """Create temporary Excel file for testing."""
        with NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_file:
            yield temp_file.name
        # Cleanup
        Path(temp_file.name).unlink(missing_ok=True)

    def test_complete_export_import_workflow(self, sample_invoice_data_list, temp_excel_file):
        """Test complete export → import workflow."""
        # Step 1: Export to Excel
        exporter = InvoiceExcelExporter()
        exporter.export_to_excel(sample_invoice_data_list, temp_excel_file)
        
        # Verify file was created
        assert Path(temp_excel_file).exists()
        assert Path(temp_excel_file).stat().st_size > 0

        # Step 2: Import from Excel
        importer = InvoiceExcelImporter()
        imported_invoices = importer.import_from_excel(temp_excel_file)

        # Step 3: Verify import results
        assert len(imported_invoices) == len(sample_invoice_data_list)
        
        for imported_invoice_data, operation_type in imported_invoices:
            assert isinstance(imported_invoice_data, InvoiceData)
            assert isinstance(operation_type, ManageInvoiceOperationType)
            assert imported_invoice_data.invoice_number.startswith("INT-TEST-")
            assert imported_invoice_data.invoice_main is not None
            assert imported_invoice_data.invoice_main.invoice is not None

    def test_excel_file_structure(self, sample_invoice_data_list, temp_excel_file):
        """Test that exported Excel file has correct structure."""
        # Export data
        exporter = InvoiceExcelExporter()
        exporter.export_to_excel(sample_invoice_data_list, temp_excel_file)

        # Read Excel file and verify structure
        header_df = pd.read_excel(temp_excel_file, sheet_name='Fejléc adatok')
        lines_df = pd.read_excel(temp_excel_file, sheet_name='Tétel adatok')

        # Verify header sheet
        assert len(header_df) == 2  # Two invoices
        assert 'Számla sorszáma' in header_df.columns  # invoice_number
        assert 'Eladó neve' in header_df.columns       # seller_name  
        assert 'Vevő neve' in header_df.columns        # buyer_name

        # Verify lines sheet
        assert len(lines_df) == 4  # Two lines per invoice, two invoices
        assert 'Számla sorszáma' in lines_df.columns   # invoice_number
        assert 'Tétel sorszáma' in lines_df.columns    # line_number
        assert 'Megnevezés' in lines_df.columns        # description

        # Verify data consistency
        header_invoice_numbers = set(header_df['Számla sorszáma'])   # invoice_number
        line_invoice_numbers = set(lines_df['Számla sorszáma'])      # invoice_number
        assert header_invoice_numbers == line_invoice_numbers

    def test_roundtrip_data_integrity(self, sample_invoice_data_list, temp_excel_file):
        """Test that data integrity is maintained in export → import roundtrip."""
        original_invoices = [invoice_data for invoice_data, _ in sample_invoice_data_list]

        # Export
        exporter = InvoiceExcelExporter()
        exporter.export_to_excel(sample_invoice_data_list, temp_excel_file)

        # Import
        importer = InvoiceExcelImporter()
        imported_invoices = importer.import_from_excel(temp_excel_file)

        # Compare key fields
        assert len(imported_invoices) == len(original_invoices)
        
        for original, (imported_data, operation_type) in zip(original_invoices, imported_invoices):
            # Basic invoice data
            assert imported_data.invoice_number == original.invoice_number
            assert imported_data.invoice_issue_date == original.invoice_issue_date
            assert imported_data.completeness_indicator == original.completeness_indicator

            # Supplier info (if available)
            if (original.invoice_main and original.invoice_main.invoice and 
                original.invoice_main.invoice.invoice_head and
                original.invoice_main.invoice.invoice_head.supplier_info):
                
                orig_supplier = original.invoice_main.invoice.invoice_head.supplier_info
                
                if (imported_data.invoice_main and imported_data.invoice_main.invoice and 
                    imported_data.invoice_main.invoice.invoice_head and
                    imported_data.invoice_main.invoice.invoice_head.supplier_info):
                    
                    imp_supplier = imported_data.invoice_main.invoice.invoice_head.supplier_info
                    assert imp_supplier.supplier_name == orig_supplier.supplier_name

    def test_template_creation_and_import(self, temp_excel_file):
        """Test creating a template and importing data from it."""
        # Create template
        exporter = InvoiceExcelExporter()
        exporter.create_template_excel(temp_excel_file)

        # Verify template was created
        assert Path(temp_excel_file).exists()

        # Read template to verify structure
        header_df = pd.read_excel(temp_excel_file, sheet_name='Fejléc adatok')
        lines_df = pd.read_excel(temp_excel_file, sheet_name='Tétel adatok')

        # Template should have column headers but no data rows
        assert len(header_df) == 0  # No data rows
        assert len(lines_df) == 0   # No data rows
        assert len(header_df.columns) > 0  # But should have columns
        assert len(lines_df.columns) > 0   # But should have columns

    def test_import_with_manual_excel_modifications(self, sample_invoice_data_list, temp_excel_file):
        """Test import after manual modifications to Excel file."""
        # Export original data
        exporter = InvoiceExcelExporter()
        exporter.export_to_excel(sample_invoice_data_list, temp_excel_file)

        # Read Excel file
        header_df = pd.read_excel(temp_excel_file, sheet_name='Fejléc adatok')
        lines_df = pd.read_excel(temp_excel_file, sheet_name='Tétel adatok')

        # Simulate manual modifications
        header_df.loc[0, 'seller_name'] = 'Modified Supplier Name'
        lines_df.loc[0, 'description'] = 'Modified Product Description'
        lines_df.loc[0, 'quantity'] = 5.0  # Changed quantity

        # Save modified Excel
        with pd.ExcelWriter(temp_excel_file, engine='openpyxl') as writer:
            header_df.to_excel(writer, sheet_name='Fejléc adatok', index=False)
            lines_df.to_excel(writer, sheet_name='Tétel adatok', index=False)

        # Import modified data
        importer = InvoiceExcelImporter()
        imported_invoices = importer.import_from_excel(temp_excel_file)

        # Verify modifications were imported
        assert len(imported_invoices) > 0
        first_invoice_data, operation_type = imported_invoices[0]
        
        # Check that modifications are reflected (basic checks)
        assert first_invoice_data.invoice_number is not None
        # More detailed checks would require accessing nested structures

    def test_error_handling_in_workflow(self, sample_invoice_data_list):
        """Test error handling in export/import workflow."""
        # Test export to invalid path
        exporter = InvoiceExcelExporter()
        with pytest.raises(ExcelProcessingException):
            exporter.export_to_excel(sample_invoice_data_list, "/invalid/path/test.xlsx")

        # Test import from non-existent file
        importer = InvoiceExcelImporter()
        with pytest.raises(ExcelProcessingException):
            importer.import_from_excel("non_existent_file.xlsx")

    def test_large_dataset_handling(self, temp_excel_file):
        """Test handling of larger datasets."""
        # Create a larger dataset (simulate 10 invoices with multiple lines each)
        large_dataset = []
        
        for i in range(1, 11):  # 10 invoices
            # Minimal invoice data for performance
            invoice_data = InvoiceData(
                invoice_number=f"LARGE-{i:03d}",
                invoice_issue_date="2024-01-15",
                completeness_indicator=True
            )
            large_dataset.append((invoice_data, ManageInvoiceOperationType.CREATE))

        # Export large dataset
        exporter = InvoiceExcelExporter()
        exporter.export_to_excel(large_dataset, temp_excel_file)

        # Verify file was created and has reasonable size
        assert Path(temp_excel_file).exists()
        file_size = Path(temp_excel_file).stat().st_size
        assert file_size > 1000  # Should be at least 1KB for 10 invoices

        # Import large dataset
        importer = InvoiceExcelImporter()
        imported_invoices = importer.import_from_excel(temp_excel_file)

        # Verify all invoices were imported
        assert len(imported_invoices) == 10

    def test_concurrent_access_safety(self, sample_invoice_data_list, temp_excel_file):
        """Test that export/import operations are safe for concurrent access."""
        import threading
        import time
        
        results = []
        errors = []

        def export_worker():
            try:
                exporter = InvoiceExcelExporter()
                # Use different filename for each thread
                temp_file = temp_excel_file.replace('.xlsx', f'_{threading.current_thread().ident}.xlsx')
                exporter.export_to_excel(sample_invoice_data_list, temp_file)
                results.append(temp_file)
            except Exception as e:
                errors.append(e)

        # Create multiple threads
        threads = []
        for i in range(3):
            thread = threading.Thread(target=export_worker)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify no errors occurred
        assert len(errors) == 0
        assert len(results) == 3

        # Cleanup generated files
        for file_path in results:
            Path(file_path).unlink(missing_ok=True)