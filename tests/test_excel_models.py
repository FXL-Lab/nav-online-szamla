"""
Unit tests for Excel data models.
"""

import pytest
from decimal import Decimal

from nav_online_szamla.excel.models import InvoiceHeaderRow, InvoiceLineRow


class TestInvoiceHeaderRow:
    """Test cases for InvoiceHeaderRow data model."""

    def test_header_row_creation_with_required_fields(self):
        """Test creating header row with required fields only."""
        header_row = InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            completeness_indicator=True
        )

        assert header_row.invoice_number == "TEST-001"
        assert header_row.invoice_issue_date == "2024-01-15"
        assert header_row.completeness_indicator is True

    def test_header_row_creation_with_all_fields(self):
        """Test creating header row with all fields."""
        header_row = InvoiceHeaderRow(
            # Basic invoice info
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            completeness_indicator=True,
            
            # Seller info
            seller_name="Test Supplier Ltd.",
            seller_tax_number_main="12345678",
            seller_tax_number_vat="2",
            seller_tax_number_county="01",
            seller_country_code="HU",
            seller_postal_code="1234",
            seller_city="Budapest",
            seller_address_detail="Test street 1",
            
            # Buyer info
            buyer_name="Test Customer Inc.",
            buyer_tax_number_main="87654321",
            buyer_tax_number_vat="2",
            buyer_tax_number_county="02",
            buyer_country_code="HU",
            buyer_postal_code="5678",
            buyer_city="Debrecen",
            buyer_address_detail="Buyer street 2",
            buyer_vat_status="DOMESTIC",
            buyer_community_vat_number="HU87654321",
            buyer_third_country_tax_number="EU123456",
            
            # Invoice details
            fulfillment_date="2024-01-15",
            payment_due_date="2024-02-15",
            payment_method="TRANSFER",
            invoice_currency="HUF",
            exchange_rate=1.0,
            small_business_indicator=False,
            cash_accounting_indicator=False,
            invoice_category="NORMAL",
            
            # Modification info
            original_invoice_number="ORIG-001",
            modification_date="2024-01-20",
            modification_index=1,
            
            # Amounts
            net_amount_original=2000.0,
            net_amount_huf=2000.0,
            vat_amount_original=540.0,
            vat_amount_huf=540.0,
            gross_amount_original=2540.0,
            gross_amount_huf=2540.0
        )

        # Verify all fields are set correctly
        assert header_row.invoice_number == "TEST-001"
        assert header_row.seller_name == "Test Supplier Ltd."
        assert header_row.buyer_name == "Test Customer Inc."
        assert header_row.net_amount_original == 2000.0
        assert header_row.modification_index == 1

    def test_header_row_default_values(self):
        """Test that optional fields have correct default values."""
        header_row = InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15"
        )

        # Test default values for optional fields
        assert header_row.completeness_indicator is None
        assert header_row.seller_name is None
        assert header_row.net_amount_original is None
        assert header_row.exchange_rate is None

    def test_header_row_with_decimal_amounts(self):
        """Test header row with Decimal amount values."""
        header_row = InvoiceHeaderRow(
            invoice_number="DECIMAL-001",
            invoice_issue_date="2024-01-15",
            net_amount_original=Decimal("1000.50"),
            vat_amount_original=Decimal("270.14"),
            gross_amount_original=Decimal("1270.64")
        )

        assert header_row.net_amount_original == Decimal("1000.50")
        assert header_row.vat_amount_original == Decimal("270.14")
        assert header_row.gross_amount_original == Decimal("1270.64")

    def test_header_row_string_representation(self):
        """Test string representation of header row."""
        header_row = InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            seller_name="Test Supplier"
        )

        str_repr = str(header_row)
        assert "InvoiceHeaderRow" in str_repr
        assert "TEST-001" in str_repr

    def test_header_row_equality(self):
        """Test equality comparison of header rows."""
        header_row1 = InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            seller_name="Test Supplier"
        )
        
        header_row2 = InvoiceHeaderRow(
            invoice_number="TEST-001",
            invoice_issue_date="2024-01-15",
            seller_name="Test Supplier"
        )
        
        header_row3 = InvoiceHeaderRow(
            invoice_number="TEST-002",
            invoice_issue_date="2024-01-15",
            seller_name="Test Supplier"
        )

        assert header_row1 == header_row2
        assert header_row1 != header_row3


class TestInvoiceLineRow:
    """Test cases for InvoiceLineRow data model."""

    def test_line_row_creation_with_required_fields(self):
        """Test creating line row with required fields only."""
        line_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            description="Test Product"
        )

        assert line_row.invoice_number == "TEST-001"
        assert line_row.line_number == 1
        assert line_row.description == "Test Product"

    def test_line_row_creation_with_all_fields(self):
        """Test creating line row with all fields."""
        line_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            line_modification_type="CREATE",
            description="Test Product",
            quantity=Decimal("2.0"),
            unit_of_measure="PIECE",
            unit_price=Decimal("1000.0"),
            net_amount_original=Decimal("2000.0"),
            net_amount_huf=Decimal("2000.0"),
            vat_rate=Decimal("27.0"),
            vat_amount_original=Decimal("540.0"),
            vat_amount_huf=Decimal("540.0"),
            gross_amount_original=Decimal("2540.0"),
            gross_amount_huf=Decimal("2540.0")
        )

        # Verify all fields are set correctly
        assert line_row.invoice_number == "TEST-001"
        assert line_row.line_number == 1
        assert line_row.line_modification_type == "CREATE"
        assert line_row.description == "Test Product"
        assert line_row.quantity == Decimal("2.0")
        assert line_row.unit_price == Decimal("1000.0")
        assert line_row.net_amount_original == Decimal("2000.0")

    def test_line_row_default_values(self):
        """Test that optional fields have correct default values."""
        line_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1
        )

        # Test default values for optional fields
        assert line_row.description is None
        assert line_row.quantity is None
        assert line_row.unit_price is None
        assert line_row.vat_rate is None

    def test_line_row_with_decimal_values(self):
        """Test line row with Decimal values."""
        line_row = InvoiceLineRow(
            invoice_number="DECIMAL-001",
            line_number=1,
            quantity=Decimal("1.5"),
            unit_price=Decimal("666.67"),
            net_amount_original=Decimal("1000.01")
        )

        assert line_row.quantity == Decimal("1.5")
        assert line_row.unit_price == Decimal("666.67")
        assert line_row.net_amount_original == Decimal("1000.01")

    def test_line_row_with_integer_line_number(self):
        """Test line row with integer line number."""
        line_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=5,
            description="Line 5"
        )

        assert line_row.line_number == 5
        assert isinstance(line_row.line_number, int)

    def test_line_row_string_representation(self):
        """Test string representation of line row."""
        line_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            description="Test Product"
        )

        str_repr = str(line_row)
        assert "InvoiceLineRow" in str_repr
        assert "TEST-001" in str_repr

    def test_line_row_equality(self):
        """Test equality comparison of line rows."""
        line_row1 = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            description="Test Product",
            quantity=Decimal("2.0")
        )
        
        line_row2 = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            description="Test Product",
            quantity=Decimal("2.0")
        )
        
        line_row3 = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=2,  # Different line number
            description="Test Product",
            quantity=Decimal("2.0")
        )

        assert line_row1 == line_row2
        assert line_row1 != line_row3

    def test_line_row_with_float_values(self):
        """Test line row accepts float values for numeric fields."""
        line_row = InvoiceLineRow(
            invoice_number="FLOAT-001",
            line_number=1,
            quantity=2.5,  # float
            unit_price=100.0,  # float
            vat_rate=27.0  # float
        )

        assert line_row.quantity == 2.5
        assert line_row.unit_price == 100.0
        assert line_row.vat_rate == 27.0

    def test_line_row_modification_types(self):
        """Test line row with different modification types."""
        create_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            line_modification_type="CREATE"
        )
        
        modify_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            line_modification_type="MODIFY"
        )
        
        delete_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            line_modification_type="DELETE"
        )

        assert create_row.line_modification_type == "CREATE"
        assert modify_row.line_modification_type == "MODIFY"
        assert delete_row.line_modification_type == "DELETE"

    def test_line_row_unit_of_measure_values(self):
        """Test line row with different unit of measure values."""
        piece_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=1,
            unit_of_measure="PIECE"
        )
        
        hour_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=2,
            unit_of_measure="HOUR"
        )
        
        kg_row = InvoiceLineRow(
            invoice_number="TEST-001",
            line_number=3,
            unit_of_measure="KG"
        )

        assert piece_row.unit_of_measure == "PIECE"
        assert hour_row.unit_of_measure == "HOUR"
        assert kg_row.unit_of_measure == "KG"


class TestDataModelIntegration:
    """Test integration between header and line row models."""

    def test_invoice_reference_consistency(self):
        """Test that header and line rows reference the same invoice."""
        invoice_number = "INTEGRATION-001"
        
        header_row = InvoiceHeaderRow(
            invoice_number=invoice_number,
            invoice_issue_date="2024-01-15"
        )
        
        line_rows = [
            InvoiceLineRow(
                invoice_number=invoice_number,
                line_number=1,
                description="Product 1"
            ),
            InvoiceLineRow(
                invoice_number=invoice_number,
                line_number=2,
                description="Product 2"
            )
        ]

        # Verify consistency
        assert header_row.invoice_number == invoice_number
        for line_row in line_rows:
            assert line_row.invoice_number == invoice_number

    def test_amount_consistency_validation(self):
        """Test validation of amount consistency between header and lines."""
        # This would be a business logic test to ensure that
        # header totals match the sum of line amounts
        header_row = InvoiceHeaderRow(
            invoice_number="AMOUNTS-001",
            net_amount_original=2000.0,
            gross_amount_original=2540.0
        )
        
        line_rows = [
            InvoiceLineRow(
                invoice_number="AMOUNTS-001",
                line_number=1,
                net_amount_original=1000.0,
                gross_amount_original=1270.0
            ),
            InvoiceLineRow(
                invoice_number="AMOUNTS-001",
                line_number=2,
                net_amount_original=1000.0,
                gross_amount_original=1270.0
            )
        ]

        # Calculate totals from lines
        total_net = sum(line.net_amount_original or 0 for line in line_rows)
        total_gross = sum(line.gross_amount_original or 0 for line in line_rows)

        # Verify consistency
        assert total_net == header_row.net_amount_original
        assert total_gross == header_row.gross_amount_original