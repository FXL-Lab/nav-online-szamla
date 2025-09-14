"""
Test configuration for Excel functionality.

Run with: poetry run python -m pytest tests/test_excel_*.py
"""

import pytest
import sys
from pathlib import Path

# Add test fixtures and configurations here if needed
sys.path.insert(0, str(Path(__file__).parent.parent))

# Test markers for different test categories
pytest_markers = {
    "unit": "Unit tests - fast, isolated tests",
    "integration": "Integration tests - test component interactions", 
    "slow": "Slow tests - may take longer to complete",
    "excel": "Excel functionality tests"
}

# Configure test discovery
def pytest_configure(config):
    """Configure pytest with custom markers."""
    for marker, description in pytest_markers.items():
        config.addinivalue_line("markers", f"{marker}: {description}")

# Test collection modifications
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers automatically."""
    for item in items:
        # Add excel marker to all Excel tests
        if "test_excel_" in item.nodeid:
            item.add_marker(pytest.mark.excel)
        
        # Add integration marker to integration tests
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
            
        # Add slow marker to tests that might be slower
        if any(slow_indicator in item.nodeid for slow_indicator in 
               ["large_dataset", "concurrent_access", "workflow"]):
            item.add_marker(pytest.mark.slow)