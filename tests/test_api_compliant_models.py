"""
Tests for new API-compliant request types.

These tests ensure the new request types match the official NAV API documentation.
"""

import pytest
from datetime import datetime

from nav_online_szamla.models import (
    QueryInvoiceDigestRequest,
    QueryInvoiceCheckRequest,
    QueryInvoiceDataRequest,
    QueryInvoiceChainDigestRequest,
    MandatoryQueryParams,
    AdditionalQueryParams,
    RelationalQueryParams,
    TransactionQueryParams,
    InvoiceQueryParams,
    DateRange,
    DateTimeRange,
    OriginalInvoiceNumber,
    RelationalQueryParam,
    InvoiceDirection,
    InvoiceCategory,
    PaymentMethod,
    InvoiceAppearance,
    Source,
    QueryOperator,
    InvoiceOperation,
)


class TestDateRange:
    """Test DateRange model."""

    def test_date_range_creation(self):
        """Test creating a DateRange."""
        date_range = DateRange(date_from="2025-01-01", date_to="2025-01-31")

        assert date_range.date_from == "2025-01-01"
        assert date_range.date_to == "2025-01-31"


class TestDateTimeRange:
    """Test DateTimeRange model."""

    def test_datetime_range_creation(self):
        """Test creating a DateTimeRange."""
        datetime_range = DateTimeRange(
            date_time_from="2025-01-01T00:00:00.000Z",
            date_time_to="2025-01-31T23:59:59.999Z",
        )

        assert datetime_range.date_time_from == "2025-01-01T00:00:00.000Z"
        assert datetime_range.date_time_to == "2025-01-31T23:59:59.999Z"


class TestOriginalInvoiceNumber:
    """Test OriginalInvoiceNumber model."""

    def test_original_invoice_number_creation(self):
        """Test creating an OriginalInvoiceNumber."""
        orig_num = OriginalInvoiceNumber(original_invoice_number="INV-2025-001")

        assert orig_num.original_invoice_number == "INV-2025-001"


class TestMandatoryQueryParams:
    """Test MandatoryQueryParams model."""

    def test_mandatory_params_with_invoice_issue_date(self):
        """Test creating MandatoryQueryParams with invoice issue date."""
        params = MandatoryQueryParams(
            invoice_issue_date=DateRange(date_from="2025-01-01", date_to="2025-01-31")
        )

        assert params.invoice_issue_date is not None
        assert params.ins_date is None
        assert params.original_invoice_number is None

    def test_mandatory_params_with_ins_date(self):
        """Test creating MandatoryQueryParams with processing timestamp."""
        params = MandatoryQueryParams(
            ins_date=DateTimeRange(
                date_time_from="2025-01-01T00:00:00.000Z",
                date_time_to="2025-01-31T23:59:59.999Z",
            )
        )

        assert params.invoice_issue_date is None
        assert params.ins_date is not None
        assert params.original_invoice_number is None

    def test_mandatory_params_with_original_invoice_number(self):
        """Test creating MandatoryQueryParams with original invoice number."""
        params = MandatoryQueryParams(
            original_invoice_number=OriginalInvoiceNumber(
                original_invoice_number="INV-2025-001"
            )
        )

        assert params.invoice_issue_date is None
        assert params.ins_date is None
        assert params.original_invoice_number is not None


class TestAdditionalQueryParams:
    """Test AdditionalQueryParams model."""

    def test_additional_params_empty(self):
        """Test creating empty AdditionalQueryParams."""
        params = AdditionalQueryParams()

        assert params.tax_number is None
        assert params.group_member_tax_number is None
        assert params.name is None
        assert params.invoice_category is None
        assert params.payment_method is None
        assert params.invoice_appearance is None
        assert params.source is None
        assert params.currency is None

    def test_additional_params_full(self):
        """Test creating fully populated AdditionalQueryParams."""
        params = AdditionalQueryParams(
            tax_number="12345678",
            group_member_tax_number="87654321",
            name="Test Company",
            invoice_category=InvoiceCategory.NORMAL,
            payment_method=PaymentMethod.TRANSFER,
            invoice_appearance=InvoiceAppearance.ELECTRONIC,
            source=Source.XML,
            currency="HUF",
        )

        assert params.tax_number == "12345678"
        assert params.group_member_tax_number == "87654321"
        assert params.name == "Test Company"
        assert params.invoice_category == InvoiceCategory.NORMAL
        assert params.payment_method == PaymentMethod.TRANSFER
        assert params.invoice_appearance == InvoiceAppearance.ELECTRONIC
        assert params.source == Source.XML
        assert params.currency == "HUF"


class TestRelationalQueryParams:
    """Test RelationalQueryParams model."""

    def test_relational_params_empty(self):
        """Test creating empty RelationalQueryParams."""
        params = RelationalQueryParams()

        assert params.invoice_delivery is None
        assert params.payment_date is None
        assert params.invoice_net_amount is None
        assert params.invoice_net_amount_huf is None
        assert params.invoice_vat_amount is None
        assert params.invoice_vat_amount_huf is None

    def test_relational_params_with_amount_filter(self):
        """Test creating RelationalQueryParams with amount filter."""
        params = RelationalQueryParams(
            invoice_net_amount=RelationalQueryParam(
                query_operator=QueryOperator.GTE, query_value="10000.00"
            ),
            payment_date=RelationalQueryParam(
                query_operator=QueryOperator.EQ, query_value="2025-01-15"
            ),
        )

        assert params.invoice_net_amount is not None
        assert params.invoice_net_amount.query_operator == QueryOperator.GTE
        assert params.invoice_net_amount.query_value == "10000.00"
        assert params.payment_date is not None
        assert params.payment_date.query_operator == QueryOperator.EQ
        assert params.payment_date.query_value == "2025-01-15"


class TestTransactionQueryParams:
    """Test TransactionQueryParams model."""

    def test_transaction_params_empty(self):
        """Test creating empty TransactionQueryParams."""
        params = TransactionQueryParams()

        assert params.transaction_id is None
        assert params.index is None
        assert params.invoice_operation is None

    def test_transaction_params_full(self):
        """Test creating fully populated TransactionQueryParams."""
        params = TransactionQueryParams(
            transaction_id="TXN123456",
            index=1,
            invoice_operation=InvoiceOperation.CREATE,
        )

        assert params.transaction_id == "TXN123456"
        assert params.index == 1
        assert params.invoice_operation == InvoiceOperation.CREATE


class TestInvoiceQueryParams:
    """Test InvoiceQueryParams model."""

    def test_invoice_query_params_minimal(self):
        """Test creating minimal InvoiceQueryParams."""
        mandatory_params = MandatoryQueryParams(
            invoice_issue_date=DateRange(date_from="2025-01-01", date_to="2025-01-31")
        )

        params = InvoiceQueryParams(mandatory_query_params=mandatory_params)

        assert params.mandatory_query_params is not None
        assert params.additional_query_params is None
        assert params.relational_query_params is None
        assert params.transaction_query_params is None

    def test_invoice_query_params_full(self):
        """Test creating full InvoiceQueryParams."""
        mandatory_params = MandatoryQueryParams(
            invoice_issue_date=DateRange(date_from="2025-01-01", date_to="2025-01-31")
        )

        additional_params = AdditionalQueryParams(
            invoice_category=InvoiceCategory.NORMAL
        )

        relational_params = RelationalQueryParams(
            invoice_net_amount=RelationalQueryParam(
                query_operator=QueryOperator.GTE, query_value="1000.00"
            )
        )

        transaction_params = TransactionQueryParams(
            invoice_operation=InvoiceOperation.CREATE
        )

        params = InvoiceQueryParams(
            mandatory_query_params=mandatory_params,
            additional_query_params=additional_params,
            relational_query_params=relational_params,
            transaction_query_params=transaction_params,
        )

        assert params.mandatory_query_params is not None
        assert params.additional_query_params is not None
        assert params.relational_query_params is not None
        assert params.transaction_query_params is not None


class TestQueryInvoiceDigestRequest:
    """Test QueryInvoiceDigestRequest model."""

    def test_query_invoice_digest_request(self):
        """Test creating QueryInvoiceDigestRequest."""
        mandatory_params = MandatoryQueryParams(
            invoice_issue_date=DateRange(date_from="2025-01-01", date_to="2025-01-31")
        )

        query_params = InvoiceQueryParams(mandatory_query_params=mandatory_params)

        request = QueryInvoiceDigestRequest(
            page=1,
            invoice_direction=InvoiceDirection.OUTBOUND,
            invoice_query_params=query_params,
        )

        assert request.page == 1
        assert request.invoice_direction == InvoiceDirection.OUTBOUND
        assert request.invoice_query_params is not None


class TestQueryInvoiceCheckRequest:
    """Test QueryInvoiceCheckRequest model."""

    def test_query_invoice_check_request_minimal(self):
        """Test creating minimal QueryInvoiceCheckRequest."""
        request = QueryInvoiceCheckRequest(
            invoice_number="INV-2025-001", invoice_direction=InvoiceDirection.OUTBOUND
        )

        assert request.invoice_number == "INV-2025-001"
        assert request.invoice_direction == InvoiceDirection.OUTBOUND
        assert request.batch_index is None
        assert request.supplier_tax_number is None

    def test_query_invoice_check_request_full(self):
        """Test creating full QueryInvoiceCheckRequest."""
        request = QueryInvoiceCheckRequest(
            invoice_number="INV-2025-001",
            invoice_direction=InvoiceDirection.INBOUND,
            batch_index=1,
            supplier_tax_number="12345678",
        )

        assert request.invoice_number == "INV-2025-001"
        assert request.invoice_direction == InvoiceDirection.INBOUND
        assert request.batch_index == 1
        assert request.supplier_tax_number == "12345678"


class TestQueryInvoiceDataRequest:
    """Test QueryInvoiceDataRequest model."""

    def test_query_invoice_data_request_minimal(self):
        """Test creating minimal QueryInvoiceDataRequest."""
        request = QueryInvoiceDataRequest(
            invoice_number="INV-2025-001", invoice_direction=InvoiceDirection.OUTBOUND
        )

        assert request.invoice_number == "INV-2025-001"
        assert request.invoice_direction == InvoiceDirection.OUTBOUND
        assert request.batch_index is None
        assert request.supplier_tax_number is None

    def test_query_invoice_data_request_full(self):
        """Test creating full QueryInvoiceDataRequest."""
        request = QueryInvoiceDataRequest(
            invoice_number="INV-2025-001",
            invoice_direction=InvoiceDirection.INBOUND,
            batch_index=2,
            supplier_tax_number="87654321",
        )

        assert request.invoice_number == "INV-2025-001"
        assert request.invoice_direction == InvoiceDirection.INBOUND
        assert request.batch_index == 2
        assert request.supplier_tax_number == "87654321"


class TestQueryInvoiceChainDigestRequest:
    """Test QueryInvoiceChainDigestRequest model."""

    def test_query_invoice_chain_digest_request_minimal(self):
        """Test creating minimal QueryInvoiceChainDigestRequest."""
        request = QueryInvoiceChainDigestRequest(
            page=1,
            invoice_number="INV-2025-001",
            invoice_direction=InvoiceDirection.OUTBOUND,
        )

        assert request.page == 1
        assert request.invoice_number == "INV-2025-001"
        assert request.invoice_direction == InvoiceDirection.OUTBOUND
        assert request.tax_number is None

    def test_query_invoice_chain_digest_request_full(self):
        """Test creating full QueryInvoiceChainDigestRequest."""
        request = QueryInvoiceChainDigestRequest(
            page=2,
            invoice_number="INV-2025-001",
            invoice_direction=InvoiceDirection.INBOUND,
            tax_number="12345678",
        )

        assert request.page == 2
        assert request.invoice_number == "INV-2025-001"
        assert request.invoice_direction == InvoiceDirection.INBOUND
        assert request.tax_number == "12345678"


class TestNewEnums:
    """Test new enum values."""

    def test_invoice_category_enum(self):
        """Test InvoiceCategory enum values."""
        assert InvoiceCategory.NORMAL.value == "NORMAL"
        assert InvoiceCategory.SIMPLIFIED.value == "SIMPLIFIED"
        assert InvoiceCategory.AGGREGATE.value == "AGGREGATE"

    def test_payment_method_enum(self):
        """Test PaymentMethod enum values."""
        assert PaymentMethod.TRANSFER.value == "TRANSFER"
        assert PaymentMethod.CASH.value == "CASH"
        assert PaymentMethod.CARD.value == "CARD"
        assert PaymentMethod.VOUCHER.value == "VOUCHER"
        assert PaymentMethod.OTHER.value == "OTHER"

    def test_invoice_appearance_enum(self):
        """Test InvoiceAppearance enum values."""
        assert InvoiceAppearance.PAPER.value == "PAPER"
        assert InvoiceAppearance.ELECTRONIC.value == "ELECTRONIC"
        assert InvoiceAppearance.EDI.value == "EDI"
        assert InvoiceAppearance.UNKNOWN.value == "UNKNOWN"

    def test_source_enum(self):
        """Test Source enum values."""
        assert Source.WEB.value == "WEB"
        assert Source.XML.value == "XML"
        assert Source.MGM.value == "MGM"
        assert Source.OPG.value == "OPG"

    def test_query_operator_enum(self):
        """Test QueryOperator enum values."""
        assert QueryOperator.EQ.value == "EQ"
        assert QueryOperator.GT.value == "GT"
        assert QueryOperator.GTE.value == "GTE"
        assert QueryOperator.LT.value == "LT"
        assert QueryOperator.LTE.value == "LTE"
