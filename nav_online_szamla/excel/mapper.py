"""
Field mapping logic for converting between InvoiceData and Excel row structures.

This module provides mapping functionality between the complex nested InvoiceData
objects and flat Excel row representations.
"""

import logging
from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List, Tuple, Any, Dict, Union

from ..models import InvoiceData, ManageInvoiceOperationType
from ..models.invoice_data import (
    InvoiceType, InvoiceHeadType, SupplierInfoType, CustomerInfoType,
    LineType, VatRateType, LineVatDataType, LinesType,
    SummaryType, SummaryNormalType, SummaryByVatRateType, InvoiceReferenceType, InvoiceMainType,
    LineNetAmountDataType, LineGrossAmountDataType,
    LineAmountsNormalType, LineOperationType,
    CustomerVatStatusType, UnitOfMeasureType,
    InvoiceDetailType, LineModificationReferenceType,
    VatRateNetDataType, VatRateVatDataType
)
from ..models.invoice_base import (
    TaxNumberType, AddressType, DetailedAddressType, SimpleAddressType,
    PaymentMethodType, InvoiceCategoryType, InvoiceAppearanceType
)
from .models import InvoiceHeaderRow, InvoiceLineRow
from .exceptions import ExcelMappingException

logger = logging.getLogger(__name__)


class ExcelFieldMapper:
    """
    Handles bidirectional mapping between InvoiceData objects and Excel row structures.
    """
    
    # Column mappings constants for tests
    HEADER_COLUMN_MAPPINGS = {
        'Számla sorszáma': 'invoice_number',
        'Számla kelte': 'invoice_issue_date', 
        'Teljesítés dátuma': 'fulfillment_date',
        'Számla pénzneme': 'invoice_currency',
        'Alkalmazott árfolyam': 'exchange_rate',
        'Eladó adószáma (törzsszám)': 'seller_tax_number_main',
        'Eladó adószáma (ÁFA-kód)': 'seller_tax_number_vat',
        'Eladó adószáma (megyekód)': 'seller_tax_number_county',
        'Eladó neve': 'seller_name',
        'Eladó országkódja': 'seller_country_code',
        'Eladó irányítószáma': 'seller_postal_code',
        'Eladó települése': 'seller_city',
        'Eladó többi címadata': 'seller_address_detail',
        'Vevő adószáma (törzsszám)': 'buyer_tax_number_main',
        'Vevő adószáma (ÁFA-kód)': 'buyer_tax_number_vat',
        'Vevő adószáma (megyekód)': 'buyer_tax_number_county',
        'Vevő neve': 'buyer_name',
        'Vevő státusza': 'buyer_vat_status',
        'Vevő közösségi adószáma': 'buyer_community_vat_number',
        'Vevő harmadik országbeli adószáma': 'buyer_third_country_tax_number',
        'Vevő országkódja': 'buyer_country_code',
        'Vevő irányítószáma': 'buyer_postal_code',
        'Vevő települése': 'buyer_city',
        'Vevő többi címadata': 'buyer_address_detail',
        'Eredeti számla száma': 'original_invoice_number',
        'Módosító okirat kelte': 'modification_date',
        'Módosítás sorszáma': 'modification_index',
        'Számla nettó összege (a számla pénznemében)': 'net_amount_original',
        'Számla nettó összege (forintban)': 'net_amount_huf',
        'Számla ÁFA összege (a számla pénznemében)': 'vat_amount_original',
        'Számla ÁFA összege (forintban)': 'vat_amount_huf',
        'Számla bruttó összege (a számla pénznemében)': 'gross_amount_original',
        'Számla bruttó összege (forintban)': 'gross_amount_huf',
        'Fizetési határidő': 'payment_due_date',
        'Fizetési mód': 'payment_method',
        'Kisadózó jelölése': 'small_business_indicator',
        'Pénzforgalmi elszámolás jelölése': 'cash_accounting_indicator',
        'Számla típusa': 'invoice_category',
        'Az adatszolgáltatás maga a számla': 'completeness_indicator',
    }
    
    LINE_COLUMN_MAPPINGS = {
        'Számla sorszáma': 'invoice_number',
        'Tétel sorszáma': 'line_number',
        'Megnevezés': 'description',
        'Mennyiség': 'quantity',
        'Mértékegység': 'unit_of_measure',
        'Egységár': 'unit_price',
        'Nettó összeg (eredeti pénznem)': 'net_amount_original',
        'Nettó összeg (HUF)': 'net_amount_huf',
        'ÁFA kulcs': 'vat_rate',
        'ÁFA összeg (eredeti pénznem)': 'vat_amount_original',
        'ÁFA összeg (HUF)': 'vat_amount_huf',
        'Bruttó összeg (eredeti pénznem)': 'gross_amount_original',
        'Bruttó összeg (HUF)': 'gross_amount_huf',
        'Tétel módosítás típusa': 'line_modification_type',
    }

    # Header field mappings from Excel column names to our dataclass fields
    HEADER_COLUMNS = {
        'Számla sorszáma': 'invoice_number',
        'Számla kelte': 'invoice_issue_date', 
        'Teljesítés dátuma': 'fulfillment_date',
        'Számla pénzneme': 'invoice_currency',
        'Alkalmazott árfolyam': 'exchange_rate',
        'Eladó adószáma (törzsszám)': 'seller_tax_number_main',
        'Eladó adószáma (ÁFA-kód)': 'seller_tax_number_vat',
        'Eladó adószáma (megyekód)': 'seller_tax_number_county',
        'Eladó neve': 'seller_name',
        'Eladó országkódja': 'seller_country_code',
        'Eladó irányítószáma': 'seller_postal_code',
        'Eladó települése': 'seller_city',
        'Eladó többi címadata': 'seller_address_detail',
        'Vevő adószáma (törzsszám)': 'buyer_tax_number_main',
        'Vevő adószáma (ÁFA-kód)': 'buyer_tax_number_vat',
        'Vevő adószáma (megyekód)': 'buyer_tax_number_county',
        'Vevő neve': 'buyer_name',
        'Vevő státusza': 'buyer_vat_status',
        'Vevő közösségi adószáma': 'buyer_community_vat_number',
        'Vevő harmadik országbeli adószáma': 'buyer_third_country_tax_number',
        'Vevő országkódja': 'buyer_country_code',
        'Vevő irányítószáma': 'buyer_postal_code',
        'Vevő települése': 'buyer_city',
        'Vevő többi címadata': 'buyer_address_detail',
        'Eredeti számla száma': 'original_invoice_number',
        'Módosító okirat kelte': 'modification_date',
        'Módosítás sorszáma': 'modification_index',
        'Számla nettó összege (a számla pénznemében)': 'net_amount_original',
        'Számla nettó összege (forintban)': 'net_amount_huf',
        'Számla ÁFA összege (a számla pénznemében)': 'vat_amount_original',
        'Számla ÁFA összege (forintban)': 'vat_amount_huf',
        'Számla bruttó összege (a számla pénznemében)': 'gross_amount_original',
        'Számla bruttó összege (forintban)': 'gross_amount_huf',
        'Fizetési határidő': 'payment_due_date',
        'Fizetési mód': 'payment_method',
        'Kisadózó jelölése': 'small_business_indicator',
        'Pénzforgalmi elszámolás jelölése': 'cash_accounting_indicator',
        'Számla típusa': 'invoice_category',
        'Az adatszolgáltatás maga a számla': 'completeness_indicator',
    }

    # Line item field mappings
    LINE_COLUMNS = {
        'Számla sorszáma': 'invoice_number',
        'Vevő adószáma (törzsszám)': 'buyer_tax_number_main',
        'Vevő neve': 'buyer_name',
        'Eladó adószáma (törzsszám)': 'seller_tax_number_main',
        'Eladó neve': 'seller_name',
        'Tétel sorszáma': 'line_number',
        'Módosítással érintett tétel sorszáma': 'modified_line_number',
        'Módosítás jellege': 'line_modification_type',
        'Megnevezés': 'description',
        'Mennyiség': 'quantity',
        'Mennyiségi egység': 'unit_of_measure',
        'Egységár': 'unit_price',
        'Nettó összeg (a számla pénznemében)': 'net_amount_original',
        'Nettó összeg (forintban)': 'net_amount_huf',
        'Adó mértéke': 'vat_rate',
        'Áfamentesség jelölés': 'vat_exemption_indicator',
        'Áfamentesség esete': 'vat_exemption_case',
        'Áfamentesség leírása': 'vat_exemption_reason',
        'ÁFA törvény hatályán kívüli jelölés': 'out_of_scope_indicator',
        'ÁFA törvény hatályon kívüliségének esete': 'out_of_scope_case',
        'ÁFA törvény hatályon kívüliségének leírása': 'out_of_scope_reason',
        'Adóalap és felszámított adó eltérésének esete': 'tax_base_deviation_case',
        'Eltérő adóalap és felszámított adó adómérték, adótartalom': 'different_tax_rate_content',
        'Belföldi fordított adózás jelölés': 'domestic_reverse_charge_indicator',
        'Áthárított adót tartalmazó különbözet szerinti adózás': 'margin_scheme_with_vat',
        'Áthárított adót nem tartalmazó különbözet szerinti adózás': 'margin_scheme_without_vat',
        'Különbözet szerinti adózás': 'margin_scheme_indicator',
        'ÁFA összeg (a számla pénznemében)': 'vat_amount_original',
        'ÁFA összeg (forintban)': 'vat_amount_huf',
        'Bruttó összeg (a számla pénznemében)': 'gross_amount_original',
        'Bruttó összeg (forintban)': 'gross_amount_huf',
        'ÁFA tartalom': 'vat_content',
        'Előleg jelleg jelölése': 'advance_payment_indicator',
        'Tétel árfolyam': 'line_exchange_rate',
        'Tétel teljesítés dátuma': 'line_fulfillment_date',
        'Nincs felszámított áfa az áfa törvény 17. § alapján': 'no_vat_charge_indicator',
    }

    @classmethod
    def _format_county_code(cls, county_code: Optional[str]) -> Optional[str]:
        """Format county code to 2-digit format required by NAV."""
        if not county_code:
            return None
        
        # Ensure county code is 2 digits with leading zero if needed
        try:
            county_int = int(county_code)
            return f"{county_int:02d}"
        except (ValueError, TypeError):
            return county_code  # Return as-is if not a number

    @classmethod
    def _normalize_vat_percentage(cls, vat_percentage: Optional[Decimal]) -> Decimal:
        """Normalize VAT percentage to 0.0-1.0 range required by NAV."""
        if vat_percentage is None:
            return Decimal("0.0")
        
        # If percentage is > 1.0, assume it's in percentage format (e.g., 27.0 for 27%)
        # and convert to decimal format (e.g., 0.27)
        if vat_percentage > 1:
            return vat_percentage / 100
        return vat_percentage

    @classmethod
    def _normalize_header_row_values(cls, row: InvoiceHeaderRow) -> None:
        """Convert None values to appropriate defaults for Excel export."""
        # String fields should be empty strings instead of None
        string_fields = [
            'seller_name', 'seller_country_code', 'seller_postal_code', 'seller_city', 'seller_address_detail',
            'seller_tax_number_main', 'seller_tax_number_vat', 'seller_tax_number_county',
            'buyer_name', 'buyer_country_code', 'buyer_postal_code', 'buyer_city', 'buyer_address_detail',
            'buyer_tax_number_main', 'buyer_tax_number_vat', 'buyer_tax_number_county',
            'buyer_vat_status', 'buyer_community_vat_number', 'buyer_third_country_tax_number',
            'invoice_currency', 'payment_method', 'invoice_category', 'original_invoice_number'
        ]
        
        for field_name in string_fields:
            if getattr(row, field_name) is None:
                setattr(row, field_name, "")

    @classmethod
    def invoice_data_to_header_row(
        cls, 
        invoice_data: InvoiceData, 
        operation_type: ManageInvoiceOperationType
    ) -> InvoiceHeaderRow:
        """
        Convert InvoiceData object to InvoiceHeaderRow for Excel export.
        
        Args:
            invoice_data: The InvoiceData object to convert
            operation_type: The operation type associated with this invoice
            
        Returns:
            InvoiceHeaderRow: Flattened header data for Excel
            
        Raises:
            ExcelMappingException: If mapping fails
        """
        try:
            row = InvoiceHeaderRow()
            
            # Basic invoice data
            row.invoice_number = invoice_data.invoice_number
            row.invoice_issue_date = cls._parse_date(invoice_data.invoice_issue_date)
            row.completeness_indicator = invoice_data.completeness_indicator
            
            # Get the main invoice object
            if not invoice_data.invoice_main or not invoice_data.invoice_main.invoice:
                logger.warning("No invoice main data found")
                cls._normalize_header_row_values(row)
                return row
                
            invoice = invoice_data.invoice_main.invoice
            
            # Invoice head data
            if invoice.invoice_head:
                cls._map_invoice_head_to_header(invoice.invoice_head, row)
            
            # Invoice summary data
            if invoice.invoice_summary:
                cls._map_invoice_summary_to_header(invoice.invoice_summary, row)
                
            # Invoice reference (modification) data
            if invoice.invoice_reference:
                cls._map_invoice_reference_to_header(invoice.invoice_reference, row)
            
            # Normalize all None values to appropriate defaults
            cls._normalize_header_row_values(row)
            
            return row
            
        except Exception as e:
            logger.error(f"Failed to map InvoiceData to header row: {e}")
            raise ExcelMappingException(f"Header mapping failed: {e}")

    @classmethod
    def invoice_data_to_line_rows(
        cls, 
        invoice_data: InvoiceData, 
        operation_type: ManageInvoiceOperationType
    ) -> List[InvoiceLineRow]:
        """
        Convert InvoiceData object to list of InvoiceLineRow objects for Excel export.
        
        Args:
            invoice_data: The InvoiceData object to convert
            operation_type: The operation type associated with this invoice
            
        Returns:
            List[InvoiceLineRow]: List of line item data for Excel
            
        Raises:
            ExcelMappingException: If mapping fails
        """
        try:
            line_rows = []
            
            if not invoice_data.invoice_main or not invoice_data.invoice_main.invoice:
                return line_rows
                
            invoice = invoice_data.invoice_main.invoice
            
            # Get basic reference data
            seller_name = ""
            seller_tax_main = ""
            buyer_name = ""
            buyer_tax_main = ""
            
            if invoice.invoice_head:
                if invoice.invoice_head.supplier_info:
                    seller_name = invoice.invoice_head.supplier_info.supplier_name or ""
                    if invoice.invoice_head.supplier_info.supplier_tax_number:
                        seller_tax_main = invoice.invoice_head.supplier_info.supplier_tax_number.taxpayer_id or ""
                        
                if invoice.invoice_head.customer_info:
                    buyer_name = invoice.invoice_head.customer_info.customer_name or ""
                    if (invoice.invoice_head.customer_info.customer_vat_data and 
                        invoice.invoice_head.customer_info.customer_vat_data.customer_tax_number):
                        buyer_tax_main = invoice.invoice_head.customer_info.customer_vat_data.customer_tax_number.taxpayer_id or ""
            
            # Process line items
            if invoice.invoice_lines and invoice.invoice_lines.line:
                for line_data in invoice.invoice_lines.line:
                    line_row = InvoiceLineRow()
                    
                    # Basic reference data
                    line_row.invoice_number = invoice_data.invoice_number
                    line_row.seller_name = seller_name
                    line_row.seller_tax_number_main = seller_tax_main
                    line_row.buyer_name = buyer_name
                    line_row.buyer_tax_number_main = buyer_tax_main
                    
                    # Map line data
                    cls._map_line_to_line_row(line_data, line_row)
                    
                    line_rows.append(line_row)
            
            return line_rows
            
        except Exception as e:
            logger.error(f"Failed to map InvoiceData to line rows: {e}")
            raise ExcelMappingException(f"Line mapping failed: {e}")

    @classmethod
    def _map_invoice_head_to_header(cls, head: InvoiceHeadType, row: InvoiceHeaderRow) -> None:
        """Map invoice head data to header row."""
        if head.supplier_info:
            supplier = head.supplier_info
            row.seller_name = supplier.supplier_name
            
            if supplier.supplier_tax_number:
                tax_num = supplier.supplier_tax_number
                row.seller_tax_number_main = tax_num.taxpayer_id
                row.seller_tax_number_vat = tax_num.vat_code
                row.seller_tax_number_county = tax_num.county_code
                
            if supplier.supplier_address:
                cls._map_address_to_seller(supplier.supplier_address, row)
        
        if head.customer_info:
            customer = head.customer_info
            row.buyer_name = customer.customer_name
            row.buyer_vat_status = customer.customer_vat_status.value if customer.customer_vat_status else None
            
            # Extract community VAT number and third state tax ID from customer_vat_data
            if customer.customer_vat_data:
                row.buyer_community_vat_number = customer.customer_vat_data.community_vat_number
                row.buyer_third_country_tax_number = customer.customer_vat_data.third_state_tax_id
                
                # Extract tax number from customer_vat_data
                if customer.customer_vat_data.customer_tax_number:
                    tax_num = customer.customer_vat_data.customer_tax_number
                    if hasattr(tax_num, 'taxpayer_id'):
                        row.buyer_tax_number_main = tax_num.taxpayer_id
                    if hasattr(tax_num, 'vat_code'):
                        row.buyer_tax_number_vat = tax_num.vat_code
                    if hasattr(tax_num, 'county_code'):
                        row.buyer_tax_number_county = tax_num.county_code
            else:
                row.buyer_community_vat_number = None
                row.buyer_third_country_tax_number = None
                
            if customer.customer_address:
                cls._map_address_to_buyer(customer.customer_address, row)
        
        # Other head fields
        row.fulfillment_date = cls._parse_date(head.invoice_detail.invoice_delivery_date)
        row.payment_due_date = cls._parse_date(head.invoice_detail.payment_date) 
        row.payment_method = head.invoice_detail.payment_method.value if head.invoice_detail.payment_method else None
        row.invoice_currency = head.invoice_detail.currency_code
        row.exchange_rate = head.invoice_detail.exchange_rate
        row.small_business_indicator = head.invoice_detail.small_business_indicator
        row.cash_accounting_indicator = head.invoice_detail.cash_accounting_indicator
        row.invoice_category = head.invoice_detail.invoice_category.value if head.invoice_detail.invoice_category else None

    @classmethod
    def _map_invoice_summary_to_header(cls, summary: SummaryType, row: InvoiceHeaderRow) -> None:
        """Map invoice summary data to header row."""
        if summary.summary_normal:
            row.net_amount_original = summary.summary_normal.invoice_net_amount
            row.net_amount_huf = summary.summary_normal.invoice_net_amount_huf
            row.vat_amount_original = summary.summary_normal.invoice_vat_amount
            row.vat_amount_huf = summary.summary_normal.invoice_vat_amount_huf
            # Calculate gross amounts from net + vat
            if row.net_amount_original and row.vat_amount_original:
                row.gross_amount_original = row.net_amount_original + row.vat_amount_original
            if row.net_amount_huf and row.vat_amount_huf:
                row.gross_amount_huf = row.net_amount_huf + row.vat_amount_huf

    @classmethod
    def _map_invoice_reference_to_header(cls, reference: InvoiceReferenceType, row: InvoiceHeaderRow) -> None:
        """Map invoice reference (modification) data to header row."""
        row.original_invoice_number = reference.original_invoice_number
        row.modification_date = cls._parse_date(reference.modify_date)
        if reference.modification_index:
            row.modification_index = reference.modification_index

    @classmethod
    def _map_line_to_line_row(cls, line: LineType, row: InvoiceLineRow) -> None:
        """Map line data to line row."""
        row.line_number = line.line_number
        row.line_modification_type = (line.line_modification_reference.line_operation.value 
                                    if line.line_modification_reference and line.line_modification_reference.line_operation 
                                    else None)
        row.description = line.line_description
        
        # Quantities and prices
        row.quantity = line.quantity
        row.unit_of_measure = line.unit_of_measure.value if line.unit_of_measure else None
        row.unit_price = line.unit_price
        
        # Amounts
        if line.line_amounts_normal and line.line_amounts_normal.line_net_amount_data:
            net_data = line.line_amounts_normal.line_net_amount_data
            row.net_amount_original = net_data.line_net_amount
            row.net_amount_huf = net_data.line_net_amount_huf
            
        if line.line_amounts_normal and line.line_amounts_normal.line_vat_data:
            vat_data = line.line_amounts_normal.line_vat_data
            row.vat_amount_original = vat_data.line_vat_amount
            row.vat_amount_huf = vat_data.line_vat_amount_huf
            
        if line.line_amounts_normal and line.line_amounts_normal.line_vat_rate:
            row.vat_rate = line.line_amounts_normal.line_vat_rate.vat_percentage
            row.vat_exemption_indicator = getattr(line.line_amounts_normal, 'vat_exemption', None) is not None
            
        if line.line_amounts_normal and line.line_amounts_normal.line_gross_amount_data:
            gross_data = line.line_amounts_normal.line_gross_amount_data
            row.gross_amount_original = gross_data.line_gross_amount_normal
            row.gross_amount_huf = gross_data.line_gross_amount_normal_huf

    @classmethod
    def _map_address_to_seller(cls, address: AddressType, row: InvoiceHeaderRow) -> None:
        """Map address data to seller fields."""
        if hasattr(address, 'detailed_address') and address.detailed_address:
            addr = address.detailed_address
            row.seller_country_code = addr.country_code
            row.seller_postal_code = addr.postal_code  
            row.seller_city = addr.city
            # Combine address details
            addr_parts = [addr.street_name, addr.public_place_category, addr.number, 
                         addr.building, addr.staircase, addr.floor, addr.door]
            row.seller_address_detail = ' '.join(filter(None, addr_parts))
        elif hasattr(address, 'simple_address') and address.simple_address:
            addr = address.simple_address
            row.seller_country_code = addr.country_code
            row.seller_postal_code = addr.postal_code
            row.seller_city = addr.city
            row.seller_address_detail = addr.additional_address_detail

    @classmethod  
    def _map_address_to_buyer(cls, address: AddressType, row: InvoiceHeaderRow) -> None:
        """Map address data to buyer fields."""
        if hasattr(address, 'detailed_address') and address.detailed_address:
            addr = address.detailed_address
            row.buyer_country_code = addr.country_code
            row.buyer_postal_code = addr.postal_code
            row.buyer_city = addr.city
            # Combine address details
            addr_parts = [addr.street_name, addr.public_place_category, addr.number,
                         addr.building, addr.staircase, addr.floor, addr.door]
            row.buyer_address_detail = ' '.join(filter(None, addr_parts))
        elif hasattr(address, 'simple_address') and address.simple_address:
            addr = address.simple_address
            row.buyer_country_code = addr.country_code
            row.buyer_postal_code = addr.postal_code
            row.buyer_city = addr.city
            row.buyer_address_detail = addr.additional_address_detail

    @classmethod
    def _parse_date(cls, date_str: Optional[str]) -> Optional[str]:
        """Parse date string and return as standardized string format."""
        if not date_str:
            return None
        try:
            # Parse and reformat to standard format
            parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            try:
                parsed_date = datetime.strptime(date_str[:10], '%Y-%m-%d').date()
                return parsed_date.strftime('%Y-%m-%d')
            except ValueError:
                logger.warning(f"Could not parse date: {date_str}")
                return None

    @classmethod
    def _format_date(cls, date_obj: Optional[Union[date, str]]) -> Optional[str]:
        """Format date object to string."""
        if not date_obj:
            return None
        
        # If it's already a string, return as-is
        if isinstance(date_obj, str):
            return date_obj
            
        # If it's a date object, format it
        if isinstance(date_obj, date):
            return date_obj.strftime('%Y-%m-%d')
            
        # Try to convert other types
        try:
            return str(date_obj)
        except:
            return None

    @classmethod
    def header_row_to_invoice_data(cls, row: InvoiceHeaderRow) -> Tuple[InvoiceData, ManageInvoiceOperationType]:
        """
        Convert InvoiceHeaderRow back to InvoiceData object (for import).
        
        This is a complex reverse mapping that reconstructs the nested structure.
        
        Args:
            row: InvoiceHeaderRow with flat Excel data
            
        Returns:
            Tuple[InvoiceData, ManageInvoiceOperationType]: Reconstructed invoice data
        """
        try:
            # Create basic InvoiceData structure
            invoice_data = InvoiceData(
                invoice_number=row.invoice_number,
                invoice_issue_date=cls._format_date(row.invoice_issue_date),
                completeness_indicator=row.completeness_indicator or False
            )
            
            # Create invoice head from header row
            invoice_head = cls._build_invoice_head_from_row(row)
            
            # Create invoice summary from header row
            invoice_summary = cls._build_invoice_summary_from_row(row)
            
            # Create invoice reference if modification data exists
            invoice_reference = None
            if row.original_invoice_number or row.modification_date or row.modification_index:
                invoice_reference = cls._build_invoice_reference_from_row(row)
            
            # Create main invoice structure
            invoice = InvoiceType(
                invoice_head=invoice_head,
                invoice_summary=invoice_summary,
                invoice_reference=invoice_reference,
                # Lines will be added separately by the importer
                invoice_lines=None
            )
            
            invoice_main = InvoiceMainType(invoice=invoice)
            invoice_data.invoice_main = invoice_main
            
            # Default operation type (can be overridden)
            operation_type = ManageInvoiceOperationType.CREATE
            
            return invoice_data, operation_type
            
        except Exception as e:
            logger.error(f"Failed to convert header row to InvoiceData: {e}")
            raise ExcelMappingException(f"Header conversion failed: {e}")

    @classmethod
    def line_rows_to_invoice_lines(cls, rows: List[InvoiceLineRow]) -> LinesType:
        """
        Convert InvoiceLineRow objects to LinesType structure (for import).
        
        This reconstructs the line items structure from flat Excel data.
        
        Args:
            rows: List of InvoiceLineRow objects
            
        Returns:
            LinesType: Reconstructed lines structure
        """
        try:
            lines = []
            
            for row in rows:
                line = cls._build_line_from_row(row)
                if line:
                    lines.append(line)
            
            return LinesType(merged_item_indicator=False, line=lines) if lines else None
            
        except Exception as e:
            logger.error(f"Failed to convert line rows to LinesType: {e}")
            raise ExcelMappingException(f"Lines conversion failed: {e}")

    @classmethod
    def _build_invoice_head_from_row(cls, row: InvoiceHeaderRow) -> InvoiceHeadType:
        """Build InvoiceHeadType from header row data."""
        # Supplier info
        supplier_info = None
        if any([row.seller_name, row.seller_tax_number_main, row.seller_country_code]):
            supplier_tax_number = None
            if row.seller_tax_number_main:
                supplier_tax_number = TaxNumberType(
                    taxpayer_id=row.seller_tax_number_main,
                    vat_code=row.seller_tax_number_vat,
                    county_code=cls._format_county_code(row.seller_tax_number_county)
                )
            
            supplier_address = None
            if any([row.seller_country_code, row.seller_postal_code, row.seller_city]):
                supplier_address = cls._build_address_from_seller_fields(row)
            
            supplier_info = SupplierInfoType(
                supplier_tax_number=supplier_tax_number,
                supplier_name=row.seller_name,
                supplier_address=supplier_address
            )
        
        # Customer info
        customer_info = None
        if any([row.buyer_name, row.buyer_tax_number_main, row.buyer_country_code]):
            # Create customer VAT data if we have tax info or VAT numbers
            customer_vat_data = None
            if any([row.buyer_tax_number_main, row.buyer_community_vat_number, row.buyer_third_country_tax_number]):
                customer_tax_number = None
                if row.buyer_tax_number_main:
                    # Need to import CustomerTaxNumberType
                    from ..models.invoice_data import CustomerTaxNumberType
                    customer_tax_number = CustomerTaxNumberType(
                        taxpayer_id=row.buyer_tax_number_main,
                        vat_code=row.buyer_tax_number_vat,
                        county_code=cls._format_county_code(row.buyer_tax_number_county)
                    )
                
                from ..models.invoice_data import CustomerVatDataType
                customer_vat_data = CustomerVatDataType(
                    customer_tax_number=customer_tax_number,
                    community_vat_number=row.buyer_community_vat_number,
                    third_state_tax_id=row.buyer_third_country_tax_number
                )
            
            customer_address = None
            if any([row.buyer_country_code, row.buyer_postal_code, row.buyer_city]):
                customer_address = cls._build_address_from_buyer_fields(row)
            
            # Parse VAT status
            # Customer VAT status - NAV schema requires this field
            customer_vat_status = None
            if row.buyer_vat_status:
                try:
                    customer_vat_status = CustomerVatStatusType(row.buyer_vat_status)
                except ValueError:
                    logger.warning(f"Invalid customer VAT status: {row.buyer_vat_status}")
                    # Default to DOMESTIC if invalid
                    customer_vat_status = CustomerVatStatusType.DOMESTIC
            else:
                # Default to DOMESTIC if not provided
                customer_vat_status = CustomerVatStatusType.DOMESTIC
            customer_info = CustomerInfoType(
                customer_vat_status=customer_vat_status,
                customer_vat_data=customer_vat_data,
                customer_name=row.buyer_name,
                customer_address=customer_address
            )
        
        # Parse payment method
        payment_method = None
        if row.payment_method:
            try:
                payment_method = PaymentMethodType(row.payment_method)
            except ValueError:
                logger.warning(f"Invalid payment method: {row.payment_method}")
        
        # Parse invoice category - NAV schema requires this field early in structure
        invoice_category = None
        if row.invoice_category:
            try:
                invoice_category = InvoiceCategoryType(row.invoice_category)
            except ValueError:
                logger.warning(f"Invalid invoice category: {row.invoice_category}")
                invoice_category = InvoiceCategoryType.NORMAL
        else:
            # Default to NORMAL if not provided  
            invoice_category = InvoiceCategoryType.NORMAL
        
        # Create invoice detail with proper fields
        payment_method_enum = None
        if row.payment_method:
            try:
                payment_method_enum = PaymentMethodType(row.payment_method)
            except ValueError:
                payment_method_enum = PaymentMethodType.OTHER
                
        invoice_detail = InvoiceDetailType(
            invoice_category=invoice_category,
            invoice_delivery_date=cls._format_date(row.fulfillment_date),
            payment_date=cls._format_date(row.payment_due_date),
            payment_method=payment_method_enum,
            currency_code=row.invoice_currency or "HUF",
            exchange_rate=row.exchange_rate or Decimal("1.0"),
            small_business_indicator=row.small_business_indicator or False,
            cash_accounting_indicator=row.cash_accounting_indicator or False,
            invoice_appearance=InvoiceAppearanceType.ELECTRONIC  # Required field: indicates electronic invoice
        )
        
        return InvoiceHeadType(
            supplier_info=supplier_info,
            customer_info=customer_info,
            invoice_detail=invoice_detail
        )

    @classmethod
    def _build_invoice_summary_from_row(cls, row: InvoiceHeaderRow) -> SummaryType:
        """Build SummaryType from header row data."""
        # Create basic VAT rate summary - this is required
        vat_rate_net_data = VatRateNetDataType(
            vat_rate_net_amount=row.net_amount_original,
            vat_rate_net_amount_huf=row.net_amount_huf
        )
        
        vat_rate_vat_data = VatRateVatDataType(
            vat_rate_vat_amount=row.vat_amount_original,
            vat_rate_vat_amount_huf=row.vat_amount_huf
        )
        
        # Use the most common VAT rate (0.27 for 27% in Hungary) or 0% if no VAT
        vat_rate = VatRateType(vat_percentage=Decimal("0.27") if row.vat_amount_original and row.vat_amount_original > 0 else Decimal("0.0"))
        
        summary_by_vat_rate = SummaryByVatRateType(
            vat_rate=vat_rate,
            vat_rate_net_data=vat_rate_net_data,
            vat_rate_vat_data=vat_rate_vat_data
        )
        
        summary_normal = SummaryNormalType(
            summary_by_vat_rate=[summary_by_vat_rate],  # Required field, must come first
            invoice_net_amount=row.net_amount_original,
            invoice_net_amount_huf=row.net_amount_huf,
            invoice_vat_amount=row.vat_amount_original,
            invoice_vat_amount_huf=row.vat_amount_huf
        )
        return SummaryType(
            summary_normal=summary_normal
        )

    @classmethod
    def _build_invoice_reference_from_row(cls, row: InvoiceHeaderRow) -> InvoiceReferenceType:
        """Build InvoiceReferenceType from header row data."""
        return InvoiceReferenceType(
            original_invoice_number=row.original_invoice_number,
            modify_without_master=False,  # Default value - assuming we have master data
            modification_index=row.modification_index
        )

    @classmethod
    def _build_line_from_row(cls, row: InvoiceLineRow) -> LineType:
        """Build LineType from line row data."""
        # Parse line operation type
        line_operation = None
        if row.line_modification_type:
            try:
                line_operation = LineOperationType(row.line_modification_type)
            except ValueError:
                logger.warning(f"Invalid line operation: {row.line_modification_type}")
                line_operation = LineOperationType.CREATE
        else:
            line_operation = LineOperationType.CREATE
        
        # Parse unit of measure
        unit_of_measure = None
        if row.unit_of_measure:
            try:
                unit_of_measure = UnitOfMeasureType(row.unit_of_measure)
            except ValueError:
                logger.warning(f"Invalid unit of measure: {row.unit_of_measure}")
        
        # Build line amounts
        line_amounts_normal = None
        if any([row.net_amount_original, row.vat_amount_original, row.gross_amount_original]):
            # Net amount data
            line_net_amount = None
            if row.net_amount_original is not None or row.net_amount_huf is not None:
                line_net_amount = LineNetAmountDataType(
                    line_net_amount=row.net_amount_original,
                    line_net_amount_huf=row.net_amount_huf
                )
            
            # VAT data
            line_vat_rate = None
            line_vat_data = None
            
            if row.vat_rate is not None:
                normalized_vat_rate = cls._normalize_vat_percentage(row.vat_rate)
                line_vat_rate = VatRateType(vat_percentage=normalized_vat_rate)
                
            if row.vat_amount_original is not None or row.vat_amount_huf is not None:
                line_vat_data = LineVatDataType(
                    line_vat_amount=row.vat_amount_original,
                    line_vat_amount_huf=row.vat_amount_huf
                )
            
            # Gross amount data
            line_gross_amount_data = None
            if row.gross_amount_original is not None or row.gross_amount_huf is not None:
                line_gross_amount_data = LineGrossAmountDataType(
                    line_gross_amount_normal=row.gross_amount_original,
                    line_gross_amount_normal_huf=row.gross_amount_huf
                )
            
            line_amounts_normal = LineAmountsNormalType(
                line_net_amount_data=line_net_amount,
                line_vat_rate=line_vat_rate,
                line_vat_data=line_vat_data,
                line_gross_amount_data=line_gross_amount_data
            )
        
        # Build line modification reference if needed
        line_modification_reference = None
        if line_operation and line_operation != LineOperationType.CREATE:
            line_modification_reference = LineModificationReferenceType(
                line_number_reference=row.line_number or 1,
                line_operation=line_operation
            )
        
        return LineType(
            line_number=row.line_number or 1,
            line_modification_reference=line_modification_reference,
            line_expression_indicator=False,  # Required field: indicates if line has quantity expression
            line_description=row.description,
            quantity=row.quantity,
            unit_of_measure=unit_of_measure,
            unit_price=row.unit_price,
            line_amounts_normal=line_amounts_normal
        )

    @classmethod
    def _build_address_from_seller_fields(cls, row: InvoiceHeaderRow) -> AddressType:
        """Build AddressType from seller fields."""
        if not any([row.seller_country_code, row.seller_postal_code, row.seller_city]):
            return None
        
        # Use simple address for basic data
        simple_address = SimpleAddressType(
            country_code=row.seller_country_code,
            postal_code=row.seller_postal_code or "0000",
            city=row.seller_city,
            additional_address_detail=row.seller_address_detail
        )
        
        return AddressType(simple_address=simple_address)

    @classmethod
    def _build_address_from_buyer_fields(cls, row: InvoiceHeaderRow) -> AddressType:
        """Build AddressType from buyer fields."""
        if not any([row.buyer_country_code, row.buyer_postal_code, row.buyer_city]):
            return None
        
        # Use simple address for basic data
        simple_address = SimpleAddressType(
            country_code=row.buyer_country_code,
            postal_code=row.buyer_postal_code or "0000",
            city=row.buyer_city,
            additional_address_detail=row.buyer_address_detail
        )
        
        return AddressType(simple_address=simple_address)