# NAV Online Számla Python Client

A production-grade Python client library for the Hungarian NAV (National Tax and Customs Administration) Online Invoice API.

## Features

- **Object-oriented design** - Clean, maintainable code structure
- **Comprehensive error handling** - Meaningful exceptions for different error scenarios
- **Automatic retry logic** - Built-in retry with exponential backoff for network issues
- **Date range splitting** - Automatically handles large date ranges by splitting them into smaller chunks
- **Request signing** - Proper authentication and request signature generation
- **Type safety** - Full type hints and data validation
- **Well tested** - Comprehensive test suite with high coverage

## Installation

```bash
# Using poetry (recommended)
poetry add nav-online-szamla

# Using pip
pip install nav-online-szamla
```

## Quick Start

```python
from nav_online_szamla import (
    NavOnlineInvoiceClient, NavCredentials, 
    InvoiceDirection, QueryInvoiceDigestRequest, MandatoryQueryParams,
    InvoiceQueryParams, DateTimeRange
)
from datetime import datetime

# Create credentials
credentials = NavCredentials(
    login="your_nav_login",
    password="your_nav_password", 
    signer_key="your_signer_key",
    tax_number="your_tax_number"
)

# Create API-compliant request
request = QueryInvoiceDigestRequest(
    page=1,
    invoice_direction=InvoiceDirection.OUTBOUND,
    invoice_query_params=InvoiceQueryParams(
        mandatory_query_params=MandatoryQueryParams(
            ins_date=DateTimeRange(
                date_time_from=datetime(2024, 1, 1),
                date_time_to=datetime(2024, 1, 31)
            )
        )
    )
)

# Use the client
client = NavOnlineInvoiceClient()
try:
    # Get list of invoice digests
    response = client.query_invoice_digest(credentials, request)
    
    for digest in response.invoice_digests:
        print(f"Invoice: {digest.invoice_number}")
        print(f"Supplier: {digest.supplier_tax_number}")
        print(f"Direction: {digest.invoice_direction}")
    
    # Get detailed invoice information
    if response.invoice_digests:
        detail = client.get_invoice_detail(
            credentials,
            response.invoice_digests[0].invoice_number,
            response.invoice_digests[0].invoice_direction
        )
        print(f"Detailed info for: {detail.invoice_number}")
        
except Exception as e:
    print(f"Error: {e}")
```

## Usage Examples

### Query Different Invoice Directions

```python
from nav_online_szamla.models import AdditionalQueryParams

# Query outbound invoices (issued by you)
outbound_request = QueryInvoiceDigestRequest(
    page=1,
    invoice_direction=InvoiceDirection.OUTBOUND,
    invoice_query_params=InvoiceQueryParams(
        mandatory_query_params=MandatoryQueryParams(
            ins_date=DateTimeRange(
                date_time_from=datetime(2024, 1, 1),
                date_time_to=datetime(2024, 1, 31)
            )
        )
    )
)

# Query inbound invoices (received by you)
inbound_request = QueryInvoiceDigestRequest(
    page=1,
    invoice_direction=InvoiceDirection.INBOUND,
    invoice_query_params=InvoiceQueryParams(
        mandatory_query_params=MandatoryQueryParams(
            ins_date=DateTimeRange(
                date_time_from=datetime(2024, 1, 1),
                date_time_to=datetime(2024, 1, 31)
            )
        )
    )
)

# To query both directions, make separate requests
outbound_response = client.query_invoice_digest(credentials, outbound_request)
inbound_response = client.query_invoice_digest(credentials, inbound_request)
```

### Filter by Supplier

```python
request_with_filter = QueryInvoiceDigestRequest(
    page=1,
    invoice_direction=InvoiceDirection.INBOUND,
    invoice_query_params=InvoiceQueryParams(
        mandatory_query_params=MandatoryQueryParams(
            ins_date=DateTimeRange(
                date_time_from=datetime(2024, 1, 1),
                date_time_to=datetime(2024, 1, 31)
            )
        ),
        additional_query_params=AdditionalQueryParams(
            tax_number="12345678"  # Filter by specific supplier
        )
    )
)
```

### Handle Large Date Ranges

The NAV API supports up to 35 days per request. For longer periods, make multiple requests:

```python
# For longer periods, split into multiple requests
from datetime import timedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

all_digests = []
current_date = start_date

while current_date < end_date:
    next_date = min(current_date + timedelta(days=34), end_date)
    
    request = QueryInvoiceDigestRequest(
        page=1,
        invoice_direction=InvoiceDirection.OUTBOUND,
        invoice_query_params=InvoiceQueryParams(
            mandatory_query_params=MandatoryQueryParams(
                ins_date=DateTimeRange(
                    date_time_from=current_date,
                    date_time_to=next_date
                )
            )
        )
    )
    
    response = client.query_invoice_digest(credentials, request)
    all_digests.extend(response.invoice_digests)
    
    current_date = next_date + timedelta(days=1)
```

## Error Handling

The library provides specific exception types for different error scenarios:

```python
from nav_online_szamla.exceptions import (
    NavValidationException, NavNetworkException, 
    NavApiException, NavInvoiceNotFoundException
)

try:
    response = client.query_invoice_digest(credentials, request)
except NavValidationException as e:
    print(f"Validation error: {e}")
except NavNetworkException as e:
    print(f"Network error: {e}")
except NavApiException as e: 
    print(f"API error: {e}")
except NavInvoiceNotFoundException as e:
    print(f"Invoice not found: {e}")
```

## API-Compliant Request Types (Recommended)

The library now provides request types that exactly match the official NAV API documentation structure. These are recommended for new development as they provide better type safety and match the API specification exactly.

### Basic Usage with API-Compliant Types

```python
from nav_online_szamla import (
    NavOnlineInvoiceClient, NavCredentials, InvoiceDirection,
    QueryInvoiceDigestRequest, MandatoryQueryParams, InvoiceQueryParams,
    DateRange, AdditionalQueryParams, InvoiceCategory, PaymentMethod
)

# Create credentials
credentials = NavCredentials(
    login="your_nav_login",
    password="your_nav_password",
    signer_key="your_signer_key", 
    tax_number="your_tax_number"
)

# Create mandatory query parameters (one of these is required)
mandatory_params = MandatoryQueryParams(
    invoice_issue_date=DateRange(
        date_from="2025-01-01",
        date_to="2025-01-31"
    )
)

# Optional: Add filters
additional_params = AdditionalQueryParams(
    invoice_category=InvoiceCategory.NORMAL,
    payment_method=PaymentMethod.TRANSFER,
    currency="HUF"
)

# Create the full query parameters
query_params = InvoiceQueryParams(
    mandatory_query_params=mandatory_params,
    additional_query_params=additional_params
)

# Create the request
request = QueryInvoiceDigestRequest(
    page=1,
    invoice_direction=InvoiceDirection.OUTBOUND,
    invoice_query_params=query_params
)

# Execute the query
with NavOnlineInvoiceClient() as client:
    invoices = client.query_invoice_digest(credentials, request)
    print(f"Found {len(invoices)} invoices")
```

### Query by Processing Timestamp

```python
from nav_online_szamla import DateTimeRange

# Query by processing timestamp instead of issue date
mandatory_params = MandatoryQueryParams(
    ins_date=DateTimeRange(
        date_time_from="2025-01-01T00:00:00.000Z",
        date_time_to="2025-01-31T23:59:59.999Z"
    )
)
```

### Advanced Filtering with Relational Queries

```python
from nav_online_szamla import RelationalQueryParams, RelationalQueryParam, QueryOperator

# Add amount and date filters
relational_params = RelationalQueryParams(
    invoice_net_amount=RelationalQueryParam(
        query_operator=QueryOperator.GTE,
        query_value="10000.00"
    ),
    payment_date=RelationalQueryParam(
        query_operator=QueryOperator.EQ,
        query_value="2025-01-15"
    )
)

query_params = InvoiceQueryParams(
    mandatory_query_params=mandatory_params,
    relational_query_params=relational_params
)
```

### Transaction-Based Queries

```python
from nav_online_szamla import TransactionQueryParams, InvoiceOperation

# Filter by transaction details
transaction_params = TransactionQueryParams(
    transaction_id="TXN123456",
    invoice_operation=InvoiceOperation.CREATE
)

query_params = InvoiceQueryParams(
    mandatory_query_params=mandatory_params,
    transaction_query_params=transaction_params
)
```

### Check if Invoice Exists

```python
from nav_online_szamla import QueryInvoiceCheckRequest

# Simple invoice existence check
check_request = QueryInvoiceCheckRequest(
    invoice_number="INV-2025-001",
    invoice_direction=InvoiceDirection.OUTBOUND
)

exists = client.query_invoice_check(credentials, check_request)
print(f"Invoice exists: {exists}")
```

### Get Full Invoice Data

```python
from nav_online_szamla import QueryInvoiceDataRequest

# Get complete invoice data
data_request = QueryInvoiceDataRequest(
    invoice_number="INV-2025-001", 
    invoice_direction=InvoiceDirection.OUTBOUND
)

invoice_detail = client.query_invoice_data(credentials, data_request)
if invoice_detail:
    print(f"Invoice: {invoice_detail.invoice_number}")
else:
    print("Invoice not found")
```

### Available Enum Values

The library provides enums that match the API specification exactly:

```python
# Invoice categories
InvoiceCategory.NORMAL
InvoiceCategory.SIMPLIFIED  
InvoiceCategory.AGGREGATE

# Payment methods
PaymentMethod.TRANSFER
PaymentMethod.CASH
PaymentMethod.CARD
PaymentMethod.VOUCHER
PaymentMethod.OTHER

# Invoice appearances
InvoiceAppearance.PAPER
InvoiceAppearance.ELECTRONIC
InvoiceAppearance.EDI
InvoiceAppearance.UNKNOWN

# Query operators for relational queries
QueryOperator.EQ   # Equal
QueryOperator.GT   # Greater than
QueryOperator.GTE  # Greater than or equal
QueryOperator.LT   # Less than
QueryOperator.LTE  # Less than or equal

# Invoice operations
InvoiceOperation.CREATE
InvoiceOperation.MODIFY
InvoiceOperation.STORNO
```

## Configuration

### Custom API URL and Timeout

```python
# Use test environment
client = NavOnlineInvoiceClient(
    base_url="https://api-test.onlineszamla.nav.gov.hu/invoiceService/v3/",
    timeout=60
)

# Production environment (default)
client = NavOnlineInvoiceClient()  # Uses production URL
```

## Data Models

The library provides structured data models for all responses:

```python
# Invoice digest (from list queries)
invoice = invoices[0]
print(f"Number: {invoice.invoice_number}")
print(f"Operation: {invoice.invoice_operation}")  # CREATE, MODIFY, STORNO
print(f"Supplier: {invoice.supplier_name}")
print(f"Customer: {invoice.customer_name}")
print(f"Net amount: {invoice.invoice_net_amount}")
print(f"VAT amount: {invoice.invoice_vat_amount}")
print(f"Gross amount: {invoice.invoice_gross_amount}")
print(f"Currency: {invoice.currency_code}")
print(f"Issue date: {invoice.issue_date}")

# Detailed invoice information
detail = client.get_invoice_detail(...)
print(f"Supplier info: {detail.supplier_info}")
print(f"Customer info: {detail.customer_info}")
print(f"Additional data: {detail.additional_data}")
```

## Development

### Running Tests

```bash
# Install development dependencies
poetry install --with dev,test

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=nav_online_szamla

# Run specific test file
poetry run pytest tests/test_client.py
```

### Integration Tests

For integration tests with the real NAV API, set environment variables:

```bash
export NAV_LOGIN="your_test_login"
export NAV_PASSWORD="your_test_password" 
export NAV_SIGNER_KEY="your_test_signer_key"
export NAV_TAX_NUMBER="your_test_tax_number"
export NAV_INTEGRATION_TEST=1

poetry run pytest tests/test_integration.py::test_real_api_call
```

## Requirements

- Python 3.8+
- requests
- tenacity (for retry logic)
- python-dateutil

## License

This project is licensed under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`poetry run pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Support

For issues and questions:

1. Check the [GitHub Issues](https://github.com/your-repo/nav-online-szamla/issues)
2. Review the [NAV API documentation](https://onlineszamla.nav.gov.hu/)
3. Create a new issue if needed

## Changelog

### v0.0.1 (Initial Release)

- Basic invoice querying functionality
- Invoice detail retrieval
- Comprehensive error handling
- Automatic date range splitting
- Full test coverage
- Type safety with data models