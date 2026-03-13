import pytest
from api.client import BookingAPIClient
from utils.helpers import load_booking_payload

@pytest.mark.smoke
def test_create_booking_returns_correct_data(api_client, booking_cleanup):
    client = api_client
    response= client.create_booking(load_booking_payload())
    
    assert response["bookingid"] > 0
    assert response["booking"]["firstname"] == "Ali"

    booking_cleanup.append(response["bookingid"])

@pytest.mark.smoke
@pytest.mark.regression
def test_get_booking_returns_correct_data(api_client, booking_cleanup):
    client = api_client
    response= client.create_booking(load_booking_payload())
    id_booking= response["bookingid"]
    assert client.get_booking(id_booking)["firstname"] == "Ali"

    booking_cleanup.append(id_booking)

@pytest.mark.regression
def test_delete_booking_returns_201(api_client):
    client = api_client
    response= client.create_booking(load_booking_payload())
    id_booking= response["bookingid"]
    
    assert client.delete_booking(id_booking) == 201

@pytest.mark.negative
def test_delete_without_token_returns_403(booking_cleanup):
    client = BookingAPIClient()
    response= client.create_booking(load_booking_payload())
    id_booking= response["bookingid"]
    assert client.delete_booking(id_booking) == 403
    booking_cleanup.append(id_booking)

