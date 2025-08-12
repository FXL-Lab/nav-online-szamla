"""
Test for query_invoice_data_with_xsdata and the generic parsing functionality.
"""

import pytest
import requests_mock
from nav_online_szamla.client import NavOnlineInvoiceClient
from nav_online_szamla.models_legacy import NavCredentials
from nav_online_szamla.models import InvoiceDirectionType, QueryInvoiceDataResponse, InvoiceData
from nav_online_szamla.exceptions import (
    NavApiException,
    NavValidationException,
    NavInvoiceNotFoundException,
    NavXmlParsingException,
)


class TestXsdataIntegration:
    """Test cases for xsdata integration with automatic XML serialization and parsing."""

    def _get_test_credentials(self):
        """Helper method to create test credentials."""
        return NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_signer_key",
            tax_number="12345678"
        )

    def _get_sample_response_xml(self):
        """Return a sample XML response based on real NAV API response."""
        return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<QueryInvoiceDataResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" 
                         xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common" 
                         xmlns:ns3="http://schemas.nav.gov.hu/OSA/3.0/base" 
                         xmlns:ns4="http://schemas.nav.gov.hu/OSA/3.0/data">
    <ns2:header>
        <ns2:requestId>test-request-123</ns2:requestId>
        <ns2:timestamp>2025-08-12T08:19:22.183Z</ns2:timestamp>
        <ns2:requestVersion>3.0</ns2:requestVersion>
        <ns2:headerVersion>1.0</ns2:headerVersion>
    </ns2:header>
    <ns2:result>
        <ns2:funcCode>OK</ns2:funcCode>
    </ns2:result>
    <software>
        <softwareId>NAVPYTHONCLIENT123</softwareId>
        <softwareName>NAV Python Client</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Python NAV Client</softwareDevName>
        <softwareDevContact>support@example.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>32703094</softwareDevTaxNumber>
    </software>
    <invoiceDataResult>
        <invoiceData>PEludm9pY2VEYXRhIHhtbG5zPSJodHRwOi8vc2NoZW1hcy5uYXYuZ292Lmh1L09TQS8zLjAvZGF0YSIgeG1sbnM6bnMyPSJodHRwOi8vc2NoZW1hcy5uYXYuZ292Lmh1L09TQS8zLjAvYmFzZSI+CiAgICA8aW52b2ljZU51bWJlcj5GWEwtMjAyNS02PC9pbnZvaWNlTnVtYmVyPgogICAgPGludm9pY2VJc3N1ZURhdGU+MjAyNS0wNy0wMzwvaW52b2ljZUlzc3VlRGF0ZT4KICAgIDxjb21wbGV0ZW5lc3NJbmRpY2F0b3I+ZmFsc2U8L2NvbXBsZXRlbmVzc0luZGljYXRvcj4KICAgIDxpbnZvaWNlTWFpbj4KICAgICAgICA8aW52b2ljZT4KICAgICAgICAgICAgPGludm9pY2VIZWFkPgogICAgICAgICAgICAgICAgPHN1cHBsaWVySW5mbz4KICAgICAgICAgICAgICAgICAgICA8c3VwcGxpZXJUYXhOdW1iZXI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxuczI6dGF4cGF5ZXJJZD4zMjcwMzA5NDwvbnMyOnRheHBheWVySWQ+CiAgICAgICAgICAgICAgICAgICAgICAgIDxuczI6dmF0Q29kZT4yPC9uczI6dmF0Q29kZT4KICAgICAgICAgICAgICAgICAgICAgICAgPG5zMjpjb3VudHlDb2RlPjAyPC9uczI6Y291bnR5Q29kZT4KICAgICAgICAgICAgICAgICAgICA8L3N1cHBsaWVyVGF4TnVtYmVyPgogICAgICAgICAgICAgICAgICAgIDxjb21tdW5pdHlWYXROdW1iZXI+SFUzMjcwMzA5NDwvY29tbXVuaXR5VmF0TnVtYmVyPgogICAgICAgICAgICAgICAgICAgIDxzdXBwbGllck5hbWU+RlhMIEtPUkzDgVRPTFQgRkVMRUzFkFNTw4lHxbAgVMOBUlNBU8OBRzwvc3VwcGxpZXJOYW1lPgogICAgICAgICAgICAgICAgPC9zdXBwbGllckluZm8+CiAgICAgICAgICAgICAgICA8Y3VzdG9tZXJJbmZvPgogICAgICAgICAgICAgICAgICAgIDxjdXN0b21lclZhdFN0YXR1cz5ET01FU1RJQzwvY3VzdG9tZXJWYXRTdGF0dXM+CiAgICAgICAgICAgICAgICAgICAgPGN1c3RvbWVyVmF0RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgPGN1c3RvbWVyVGF4TnVtYmVyPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPG5zMjp0YXhwYXllcklkPjIzOTA0NjQ0PC9uczI6dGF4cGF5ZXJJZD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxuczI6dmF0Q29kZT4yPC9uczI6dmF0Q29kZT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxuczI6Y291bnR5Q29kZT4xMzwvbnMyOmNvdW50eUNvZGU+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvY3VzdG9tZXJUYXhOdW1iZXI+CiAgICAgICAgICAgICAgICAgICAgPC9jdXN0b21lclZhdERhdGE+CiAgICAgICAgICAgICAgICAgICAgPGN1c3RvbWVyTmFtZT5LLVggQ29uc3VsdGluZyBLZnQuPC9jdXN0b21lck5hbWU+CiAgICAgICAgICAgICAgICA8L2N1c3RvbWVySW5mbz4KICAgICAgICAgICAgICAgIDxpbnZvaWNlRGV0YWlsPgogICAgICAgICAgICAgICAgICAgIDxpbnZvaWNlQ2F0ZWdvcnk+Tk9STUFMPC9pbnZvaWNlQ2F0ZWdvcnk+CiAgICAgICAgICAgICAgICAgICAgPGludm9pY2VEZWxpdmVyeURhdGU+MjAyNS0wNy0wMTwvaW52b2ljZURlbGl2ZXJ5RGF0ZT4KICAgICAgICAgICAgICAgICAgICA8cGVyaW9kaWNhbFNldHRsZW1lbnQ+ZmFsc2U8L3BlcmlvZGljYWxTZXR0bGVtZW50PgogICAgICAgICAgICAgICAgICAgIDxzbWFsbEJ1c2luZXNzSW5kaWNhdG9yPmZhbHNlPC9zbWFsbEJ1c2luZXNzSW5kaWNhdG9yPgogICAgICAgICAgICAgICAgICAgIDxjdXJyZW5jeUNvZGU+SFVGPC9jdXJyZW5jeUNvZGU+CiAgICAgICAgICAgICAgICAgICAgPGV4Y2hhbmdlUmF0ZT4xPC9leGNoYW5nZVJhdGU+CiAgICAgICAgICAgICAgICAgICAgPHBheW1lbnRNZXRob2Q+VFJBTlNGRVI8L3BheW1lbnRNZXRob2Q+CiAgICAgICAgICAgICAgICAgICAgPHBheW1lbnREYXRlPjIwMjUtMDctMTc8L3BheW1lbnREYXRlPgogICAgICAgICAgICAgICAgICAgIDxpbnZvaWNlQXBwZWFyYW5jZT5FTEVDVFJPTJDRPC9pbnZvaWNlQXBwZWFyYW5jZT4KICAgICAgICAgICAgICAgIDwvaW52b2ljZURldGFpbD4KICAgICAgICAgICAgPC9pbnZvaWNlSGVhZD4KICAgICAgICAgICAgPGludm9pY2VMaW5lcz4KICAgICAgICAgICAgICAgIDxtZXJnZWRJdGVtSW5kaWNhdG9yPmZhbHNlPC9tZXJnZWRJdGVtSW5kaWNhdG9yPgogICAgICAgICAgICAgICAgPGxpbmU+CiAgICAgICAgICAgICAgICAgICAgPGxpbmVOdW1iZXI+MTwvbGluZU51bWJlcj4KICAgICAgICAgICAgICAgICAgICA8YWR2YW5jZURhdGE+CiAgICAgICAgICAgICAgICAgICAgICAgIDxhZHZhbmNlSW5kaWNhdG9yPmZhbHNlPC9hZHZhbmNlSW5kaWNhdG9yPgogICAgICAgICAgICAgICAgICAgIDwvYWR2YW5jZURhdGE+CiAgICAgICAgICAgICAgICAgICAgPGxpbmVFeHByZXNzaW9uSW5kaWNhdG9yPnRydWU8L2xpbmVFeHByZXNzaW9uSW5kaWNhdG9yPgogICAgICAgICAgICAgICAgICAgIDxsaW5lRGVzY3JpcHRpb24+U3rDoW1sw6F6w6FzaSBmZWpsZXN6dMOpc2VrPC9saW5lRGVzY3JpcHRpb24+CiAgICAgICAgICAgICAgICAgICAgPHF1YW50aXR5PjE8L3F1YW50aXR5PgogICAgICAgICAgICAgICAgICAgIDx1bml0T2ZNZWFzdXJlPlBJRUNFPC91bml0T2ZNZWFzdXJlPgogICAgICAgICAgICAgICAgICAgIDx1bml0UHJpY2U+NjAwMDAwPC91bml0UHJpY2U+CiAgICAgICAgICAgICAgICAgICAgPHVuaXRQcmljZUhVRj42MDAwMDA8L3VuaXRQcmljZUhVRj4KICAgICAgICAgICAgICAgICAgICA8bGluZUFtb3VudHNOb3JtYWw+CiAgICAgICAgICAgICAgICAgICAgICAgIDxsaW5lTmV0QW1vdW50RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaW5lTmV0QW1vdW50PjYwMDAwMDwvbGluZU5ldEFtb3VudD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaW5lTmV0QW1vdW50SFVGPjYwMDAwMDwvbGluZU5ldEFtb3VudEhVRj4KICAgICAgICAgICAgICAgICAgICAgICAgPC9saW5lTmV0QW1vdW50RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgPGxpbmVWYXRSYXRlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPHZhdFBlcmNlbnRhZ2U+MC4yNzwvdmF0UGVyY2VudGFnZT4KICAgICAgICAgICAgICAgICAgICAgICAgPC9saW5lVmF0UmF0ZT4KICAgICAgICAgICAgICAgICAgICAgICAgPGxpbmVWYXREYXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGxpbmVWYXRBbW91bnQ+MTYyMDAwPC9saW5lVmF0QW1vdW50PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGxpbmVWYXRBbW91bnRIVUY+MTYyMDAwPC9saW5lVmF0QW1vdW50SFVGPgogICAgICAgICAgICAgICAgICAgICAgICA8L2xpbmVWYXREYXRhPgogICAgICAgICAgICAgICAgICAgICAgICA8bGluZUdyb3NzQW1vdW50RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaW5lR3Jvc3NBbW91bnROb3JtYWw+NzYyMDAwPC9saW5lR3Jvc3NBbW91bnROb3JtYWw+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8bGluZUdyb3NzQW1vdW50Tm9ybWFsSFVGPjc2MjAwMDwvbGluZUdyb3NzQW1vdW50Tm9ybWFsSFVGPgogICAgICAgICAgICAgICAgICAgICAgICA8L2xpbmVHcm9zc0Ftb3VudERhdGE+CiAgICAgICAgICAgICAgICAgICAgPC9saW5lQW1vdW50c05vcm1hbD4KICAgICAgICAgICAgICAgICAgICA8aW50ZXJtZWRpYXRlZFNlcnZpY2U+ZmFsc2U8L2ludGVybWVkaWF0ZWRTZXJ2aWNlPgogICAgICAgICAgICAgICAgPC9saW5lPgogICAgICAgICAgICA8L2ludm9pY2VMaW5lcz4KICAgICAgICAgICAgPGludm9pY2VTdW1tYXJ5PgogICAgICAgICAgICAgICAgPHN1bW1hcnlOb3JtYWw+CiAgICAgICAgICAgICAgICAgICAgPHN1bW1hcnlCeVZhdFJhdGU+CiAgICAgICAgICAgICAgICAgICAgICAgIDx2YXRSYXRlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPHZhdFBlcmNlbnRhZ2U+MC4yNzwvdmF0UGVyY2VudGFnZT4KICAgICAgICAgICAgICAgICAgICAgICAgPC92YXRSYXRlPgogICAgICAgICAgICAgICAgICAgICAgICA8dmF0UmF0ZU5ldERhdGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dmF0UmF0ZU5ldEFtb3VudD42MDAwMDA8L3ZhdFJhdGVOZXRBbW91bnQ+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dmF0UmF0ZU5ldEFtb3VudEhVRj42MDAwMDA8L3ZhdFJhdGVOZXRBbW91bnRIVUY+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvdmF0UmF0ZU5ldERhdGE+CiAgICAgICAgICAgICAgICAgICAgICAgIDx2YXRSYXRlVmF0RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx2YXRSYXRlVmF0QW1vdW50PjE2MjAwMDwvdmF0UmF0ZVZhdEFtb3VudD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx2YXRSYXRlVmF0QW1vdW50SFVGPjE2MjAwMDwvdmF0UmF0ZVZhdEFtb3VudEhVRj4KICAgICAgICAgICAgICAgICAgICAgICAgPC92YXRSYXRlVmF0RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgPHZhdFJhdGVHcm9zc0RhdGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8dmF0UmF0ZUdyb3NzQW1vdW50Pjc2MjAwMDwvdmF0UmF0ZUdyb3NzQW1vdW50PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPHZhdFJhdGVHcm9zc0Ftb3VudEhVRj43NjIwMDA8L3ZhdFJhdGVHcm9zc0Ftb3VudEhVRj4KICAgICAgICAgICAgICAgICAgICAgICAgPC92YXRSYXRlR3Jvc3NEYXRhPgogICAgICAgICAgICAgICAgICAgIDwvc3VtbWFyeUJ5VmF0UmF0ZT4KICAgICAgICAgICAgICAgICAgICA8aW52b2ljZU5ldEFtb3VudD42MDAwMDA8L2ludm9pY2VOZXRBbW91bnQ+CiAgICAgICAgICAgICAgICAgICAgPGludm9pY2VOZXRBbW91bnRIVUY+NjAwMDAwPC9pbnZvaWNlTmV0QW1vdW50SFVGPgogICAgICAgICAgICAgICAgICAgIDxpbnZvaWNlVmF0QW1vdW50PjE2MjAwMDwvaW52b2ljZVZhdEFtb3VudD4KICAgICAgICAgICAgICAgICAgICA8aW52b2ljZVZhdEFtb3VudEhVRj4xNjIwMDA8L2ludm9pY2VWYXRBbW91bnRIVUY+CiAgICAgICAgICAgICAgICA8L3N1bW1hcnlOb3JtYWw+CiAgICAgICAgICAgICAgICA8c3VtbWFyeUdyb3NzRGF0YT4KICAgICAgICAgICAgICAgICAgICA8aW52b2ljZUdyb3NzQW1vdW50Pjc2MjAwMDwvaW52b2ljZUdyb3NzQW1vdW50PgogICAgICAgICAgICAgICAgICAgIDxpbnZvaWNlR3Jvc3NBbW91bnRIVUY+NzYyMDAwPC9pbnZvaWNlR3Jvc3NBbW91bnRIVUY+CiAgICAgICAgICAgICAgICA8L3N1bW1hcnlHcm9zc0RhdGE+CiAgICAgICAgICAgIDwvaW52b2ljZVN1bW1hcnk+CiAgICAgICAgPC9pbnZvaWNlPgogICAgPC9pbnZvaWNlTWFpbj4KPC9JbnZvaWNlRGF0YT4=</invoiceData>
        <auditData>
            <insdate>2025-07-02T22:01:45Z</insdate>
            <insCusUser>qypaslqwjl08lih</insCusUser>
            <source>OSZ</source>
            <transactionId>5188BHEUOAEG6JTS</transactionId>
            <index>1</index>
            <originalRequestVersion>3.0</originalRequestVersion>
        </auditData>
        <compressedContentIndicator>false</compressedContentIndicator>
    </invoiceDataResult>
</QueryInvoiceDataResponse>'''

    def _get_error_response_xml(self):
        """Return a sample error response."""
        return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<QueryInvoiceDataResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" 
                         xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common">
    <ns2:header>
        <ns2:requestId>test-request-123</ns2:requestId>
        <ns2:timestamp>2025-08-12T08:19:22.183Z</ns2:timestamp>
        <ns2:requestVersion>3.0</ns2:requestVersion>
        <ns2:headerVersion>1.0</ns2:headerVersion>
    </ns2:header>
    <ns2:result>
        <ns2:funcCode>ERROR</ns2:funcCode>
        <ns2:errorCode>INVOICE_NOT_FOUND</ns2:errorCode>
        <ns2:message>Invoice not found</ns2:message>
    </ns2:result>
</QueryInvoiceDataResponse>'''

    def test_query_invoice_data_with_xsdata_success(self):
        """Test successful invoice data query using xsdata."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        with requests_mock.Mocker() as m:
            # Mock the API response
            m.post(
                f"{client.base_url}queryInvoiceData",
                text=self._get_sample_response_xml(),
                status_code=200
            )

            # Test the method
            response = client.query_invoice_data_with_xsdata(
                invoice_number="FXL-2025-6",
                invoice_direction=InvoiceDirectionType.OUTBOUND
            )

            # Verify response type and structure
            assert isinstance(response, QueryInvoiceDataResponse)
            assert response.result.func_code.value == "OK"  # func_code is an enum
            assert response.invoice_data_result is not None
            assert response.invoice_data_result.invoice_data is not None
            
            # Verify audit data
            assert response.invoice_data_result.audit_data is not None
            assert response.invoice_data_result.audit_data.transaction_id == "5188BHEUOAEG6JTS"
            assert response.invoice_data_result.audit_data.source.value == "OSZ"  # source is also an enum
            
            # Verify that invoice_data has been parsed into an InvoiceData object
            print(response.invoice_data_result.invoice_data)
            assert isinstance(response.invoice_data_result.invoice_data, InvoiceData)
            assert response.invoice_data_result.invoice_data.invoice_number == "FXL-2025-6"
            assert response.invoice_data_result.invoice_data.invoice_issue_date == "2025-07-03"

    def test_query_invoice_data_with_xsdata_validation_error(self):
        """Test validation error when invoice number is empty."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        with pytest.raises(NavValidationException, match="Invoice number is required"):
            client.query_invoice_data_with_xsdata(
                invoice_number="",
                invoice_direction=InvoiceDirectionType.OUTBOUND
            )

    def test_query_invoice_data_with_xsdata_invoice_not_found(self):
        """Test handling when invoice is not found."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        # Response with no invoice data
        no_data_response = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<QueryInvoiceDataResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api" 
                         xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common">
    <ns2:header>
        <ns2:requestId>test-request-123</ns2:requestId>
        <ns2:timestamp>2025-08-12T08:19:22.183Z</ns2:timestamp>
        <ns2:requestVersion>3.0</ns2:requestVersion>
        <ns2:headerVersion>1.0</ns2:headerVersion>
    </ns2:header>
    <ns2:result>
        <ns2:funcCode>OK</ns2:funcCode>
    </ns2:result>
    <invoiceDataResult>
    </invoiceDataResult>
</QueryInvoiceDataResponse>'''

        with requests_mock.Mocker() as m:
            m.post(
                f"{client.base_url}queryInvoiceData",
                text=no_data_response,
                status_code=200
            )

            with pytest.raises(NavInvoiceNotFoundException, match="Invoice NOT-FOUND not found"):
                client.query_invoice_data_with_xsdata(
                    invoice_number="NOT-FOUND",
                    invoice_direction=InvoiceDirectionType.OUTBOUND
                )

    def test_parse_response_from_xml_generic_function(self):
        """Test the generic XML parsing function."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        # Test successful parsing
        response = client._parse_response_from_xml(
            self._get_sample_response_xml(), 
            QueryInvoiceDataResponse
        )
        
        assert isinstance(response, QueryInvoiceDataResponse)
        assert response.result.func_code.value == "OK"  # func_code is an enum
        assert response.invoice_data_result is not None

    def test_parse_response_from_xml_with_api_error(self):
        """Test generic parsing function with API error response."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        with pytest.raises(NavApiException, match="API Error: INVOICE_NOT_FOUND"):
            client._parse_response_from_xml(
                self._get_error_response_xml(), 
                QueryInvoiceDataResponse
            )

    def test_parse_response_from_xml_with_invalid_xml(self):
        """Test generic parsing function with invalid XML."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        invalid_xml = "This is not valid XML content"

        with pytest.raises(NavXmlParsingException, match="Failed to parse response XML"):
            client._parse_response_from_xml(invalid_xml, QueryInvoiceDataResponse)

    def test_create_query_invoice_data_request(self):
        """Test request creation using xsdata dataclasses."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        # Test request creation
        request = client.create_query_invoice_data_request(
            credentials=credentials,
            invoice_number="TEST-001",
            invoice_direction=InvoiceDirectionType.OUTBOUND,
            batch_index=1,
            supplier_tax_number="12345678"
        )

        # Verify request structure
        assert request.header is not None
        assert request.user is not None
        assert request.software is not None
        assert request.invoice_number_query is not None
        
        # Verify specific fields
        assert request.invoice_number_query.invoice_number == "TEST-001"
        assert request.invoice_number_query.invoice_direction == InvoiceDirectionType.OUTBOUND
        assert request.invoice_number_query.batch_index == 1
        assert request.invoice_number_query.supplier_tax_number == "12345678"

    def test_serialize_request_to_xml(self):
        """Test XML serialization functionality."""
        credentials = self._get_test_credentials()
        client = NavOnlineInvoiceClient(credentials)

        # Create a request
        request = client.create_query_invoice_data_request(
            credentials=credentials,
            invoice_number="TEST-001",
            invoice_direction=InvoiceDirectionType.OUTBOUND
        )

        # Serialize to XML
        xml_output = client._serialize_request_to_xml(request)

        # Verify XML structure
        assert xml_output.startswith('<?xml version="1.0" encoding="UTF-8"?>')
        assert 'QueryInvoiceDataRequest' in xml_output
        assert 'xmlns="http://schemas.nav.gov.hu/OSA/3.0/api"' in xml_output
        assert 'xmlns:common="http://schemas.nav.gov.hu/NTCA/1.0/common"' in xml_output
        assert 'TEST-001' in xml_output
        assert 'OUTBOUND' in xml_output
        
        # Verify proper namespace formatting
        assert 'common:header' in xml_output
        assert 'common:user' in xml_output
        assert 'ns0:' not in xml_output  # Should not have ns0 prefixes
        assert 'ns1:' not in xml_output  # Should not have ns1 prefixes


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
