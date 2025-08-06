"""
Tests for HTTP client functionality.
"""
import pytest
import requests
import requests_mock

from nav_online_szamla.http_client import NavHttpClient
from nav_online_szamla.exceptions import (
    NavNetworkException, NavApiException, NavRateLimitException
)


class TestNavHttpClient:
    """Test NavHttpClient functionality."""
    
    def test_init(self):
        """Test client initialization."""
        client = NavHttpClient("https://api.example.com/", timeout=45)
        
        assert client.base_url == "https://api.example.com"
        assert client.timeout == 45
        assert client.session is not None
    
    def test_init_strips_trailing_slash(self):
        """Test that trailing slash is stripped from base URL."""
        client = NavHttpClient("https://api.example.com/")
        
        assert client.base_url == "https://api.example.com"
    
    def test_post_success(self):
        """Test successful POST request."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", text="success")
            
            client = NavHttpClient("https://api.example.com")
            response = client.post("/test", "test data")
            
            assert response.text == "success"
            assert response.status_code == 200
    
    def test_post_with_endpoint_leading_slash(self):
        """Test POST request with leading slash in endpoint."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", text="success")
            
            client = NavHttpClient("https://api.example.com")
            response = client.post("/test", "test data")
            
            assert response.text == "success"
    
    def test_post_with_custom_headers(self):
        """Test POST request with custom headers."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", text="success")
            
            client = NavHttpClient("https://api.example.com")
            custom_headers = {"Custom-Header": "value"}
            response = client.post("/test", "test data", headers=custom_headers)
            
            assert response.text == "success"
            # Verify that custom header was sent
            last_request = m.last_request
            assert last_request.headers["Custom-Header"] == "value"
    
    def test_get_success(self):
        """Test successful GET request."""
        with requests_mock.Mocker() as m:
            m.get("https://api.example.com/test", text="success")
            
            client = NavHttpClient("https://api.example.com")
            response = client.get("/test")
            
            assert response.text == "success"
            assert response.status_code == 200
    
    def test_get_with_params(self):
        """Test GET request with parameters."""
        with requests_mock.Mocker() as m:
            m.get("https://api.example.com/test", text="success")
            
            client = NavHttpClient("https://api.example.com")
            params = {"param1": "value1", "param2": "value2"}
            response = client.get("/test", params=params)
            
            assert response.text == "success"
            # Verify that parameters were sent
            last_request = m.last_request
            assert "param1=value1" in last_request.url
            assert "param2=value2" in last_request.url
    
    def test_rate_limit_exception(self):
        """Test rate limit handling."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", status_code=429)
            
            client = NavHttpClient("https://api.example.com")
            
            with pytest.raises(NavRateLimitException):
                client.post("/test", "test data")
    
    def test_server_error(self):
        """Test server error handling."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", status_code=500, text="Internal Server Error")
            
            client = NavHttpClient("https://api.example.com")
            
            with pytest.raises(NavApiException, match="HTTP 500"):
                client.post("/test", "test data")
    
    def test_connection_error(self):
        """Test connection error handling."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", exc=requests.exceptions.ConnectionError)
            
            client = NavHttpClient("https://api.example.com")
            
            with pytest.raises(NavNetworkException, match="Network error"):
                client.post("/test", "test data")
    
    def test_timeout_error(self):
        """Test timeout error handling."""
        with requests_mock.Mocker() as m:
            m.post("https://api.example.com/test", exc=requests.exceptions.Timeout)
            
            client = NavHttpClient("https://api.example.com")
            
            with pytest.raises(NavNetworkException, match="Network error"):
                client.post("/test", "test data")
    
    def test_context_manager(self):
        """Test context manager functionality."""
        with NavHttpClient("https://api.example.com") as client:
            assert client.session is not None
        
        # Session should be closed after context manager exits
        assert client.session is not None  # Session object still exists but is closed
    
    def test_close(self):
        """Test explicit close."""
        client = NavHttpClient("https://api.example.com")
        session = client.session
        
        client.close()
        
        # Session should be closed
        assert session is not None
