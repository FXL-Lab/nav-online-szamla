"""
Tests for data models.
NOTE: These tests are currently disabled because they test legacy model classes
that have been replaced by xsdata-generated models. The new models have different
structures and APIs.
"""

import pytest

from nav_online_szamla.models import (
    InvoiceDirectionType,
)
from nav_online_szamla.models_legacy import (
    NavCredentials,
)


class TestEnums:
    """Test enum classes."""

    def test_invoice_direction_enum(self):
        """Test InvoiceDirectionType enum."""
        assert InvoiceDirectionType.OUTBOUND.value == "OUTBOUND"
        assert InvoiceDirectionType.INBOUND.value == "INBOUND"


class TestNavCredentials:
    """Test NavCredentials data class."""

    def test_nav_credentials_basic(self):
        """Test basic NavCredentials creation."""
        credentials = NavCredentials(
            login="test_user",
            password="test_password",
            signer_key="test_key",
            tax_number="12345678",
        )

        assert credentials.login == "test_user"
        assert credentials.password == "test_password"
        assert credentials.signer_key == "test_key"
        assert credentials.tax_number == "12345678"

    def test_nav_credentials_validation(self):
        """Test NavCredentials validation."""
        # Test that all required fields must be provided
        with pytest.raises(TypeError):
            NavCredentials()

        with pytest.raises(TypeError):
            NavCredentials(login="test")


# All other model tests are disabled because they test legacy classes
# that have been replaced by xsdata-generated models

@pytest.mark.skip(reason="Legacy model classes have been replaced by xsdata-generated models")
class TestLegacyModels:
    """Placeholder for disabled legacy model tests."""
    
    def test_disabled(self):
        """All legacy model tests are disabled."""
        pass
