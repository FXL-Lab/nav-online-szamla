"""
Tests for utility functions.
"""

from datetime import datetime

from nav_online_szamla.utils import (
    generate_password_hash,
    generate_custom_id,
    calculate_request_signature,
    validate_tax_number,
    split_date_range,
    format_timestamp_for_nav,
)


class TestPasswordHash:
    """Test password hashing functionality."""

    def test_generate_password_hash(self):
        """Test password hash generation."""
        password = "test_password"
        hash_result = generate_password_hash(password)

        # Should return uppercase hex string
        assert isinstance(hash_result, str)
        assert hash_result.isupper()
        assert len(hash_result) == 128  # SHA-512 produces 64 bytes = 128 hex chars

    def test_generate_password_hash_consistent(self):
        """Test that same password produces same hash."""
        password = "test_password"
        hash1 = generate_password_hash(password)
        hash2 = generate_password_hash(password)

        assert hash1 == hash2

    def test_generate_password_hash_different_passwords(self):
        """Test that different passwords produce different hashes."""
        hash1 = generate_password_hash("password1")
        hash2 = generate_password_hash("password2")

        assert hash1 != hash2


class TestCustomId:
    """Test custom ID generation."""

    def test_generate_custom_id_default_length(self):
        """Test custom ID generation with default length."""
        custom_id = generate_custom_id()

        assert isinstance(custom_id, str)
        assert len(custom_id) == 30

    def test_generate_custom_id_custom_length(self):
        """Test custom ID generation with custom length."""
        length = 15
        custom_id = generate_custom_id(length)

        assert len(custom_id) == length

    def test_generate_custom_id_unique(self):
        """Test that generated IDs are unique."""
        id1 = generate_custom_id()
        id2 = generate_custom_id()

        assert id1 != id2


class TestRequestSignature:
    """Test request signature calculation."""

    def test_calculate_request_signature(self):
        """Test request signature calculation."""
        request_id = "TEST123"
        timestamp = "2024-01-01T10:00:00.000Z"
        signer_key = "test_key"

        signature = calculate_request_signature(request_id, timestamp, signer_key)

        assert isinstance(signature, str)
        assert signature.isupper()
        assert len(signature) == 128  # SHA3-512 produces 64 bytes = 128 hex chars

    def test_calculate_request_signature_consistent(self):
        """Test that same inputs produce same signature."""
        request_id = "TEST123"
        timestamp = "2024-01-01T10:00:00.000Z"
        signer_key = "test_key"

        sig1 = calculate_request_signature(request_id, timestamp, signer_key)
        sig2 = calculate_request_signature(request_id, timestamp, signer_key)

        assert sig1 == sig2


class TestTaxNumberValidation:
    """Test tax number validation."""

    def test_validate_tax_number_valid(self):
        """Test valid tax number validation."""
        assert validate_tax_number("12345678") is True
        assert validate_tax_number("87654321") is True

    def test_validate_tax_number_invalid_length(self):
        """Test invalid tax number length."""
        assert validate_tax_number("1234567") is False  # Too short
        assert validate_tax_number("123456789") is False  # Too long

    def test_validate_tax_number_invalid_characters(self):
        """Test invalid tax number characters."""
        assert validate_tax_number("1234567a") is False
        assert validate_tax_number("12-34-567") is False
        assert validate_tax_number("12 34 56 78") is False


class TestDateRangeSplitting:
    """Test date range splitting functionality."""

    def test_split_date_range_within_limit(self):
        """Test splitting date range within max days limit."""
        ranges = split_date_range("2024-01-01", "2024-01-10", max_days=35)

        assert len(ranges) == 1
        assert ranges[0] == ("2024-01-01", "2024-01-10")

    def test_split_date_range_exceeds_limit(self):
        """Test splitting date range that exceeds max days limit."""
        ranges = split_date_range("2024-01-01", "2024-03-01", max_days=35)

        assert len(ranges) > 1
        assert ranges[0][0] == "2024-01-01"
        assert ranges[-1][1] == "2024-03-01"

    def test_split_date_range_single_day(self):
        """Test splitting single day range."""
        ranges = split_date_range("2024-01-01", "2024-01-01", max_days=35)

        assert len(ranges) == 1
        assert ranges[0] == ("2024-01-01", "2024-01-01")


class TestTimestampFormatting:
    """Test timestamp formatting for NAV API."""

    def test_format_timestamp_for_nav(self):
        """Test timestamp formatting."""
        dt = datetime(2024, 1, 1, 10, 30, 45, 123456)
        formatted = format_timestamp_for_nav(dt)

        assert formatted.endswith("Z")
        assert "T" in formatted
        assert "2024-01-01" in formatted

    def test_format_timestamp_for_nav_current_time(self):
        """Test timestamp formatting with current time."""
        formatted = format_timestamp_for_nav()

        assert isinstance(formatted, str)
        assert formatted.endswith("Z")
        assert "T" in formatted
