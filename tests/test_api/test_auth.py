import pytest
from api.client import BookingAPIClient

@pytest.mark.smoke
def test_authenticate_returns_token():
    client = BookingAPIClient()
    client.authenticate("admin", "password123")
    assert client.token != ""



@pytest.mark.negative
def test_invalid_credentials_returns_error():
    client = BookingAPIClient()
    response =  client.authenticate("admin", "password12")
    assert response["reason"] == "Bad credentials"