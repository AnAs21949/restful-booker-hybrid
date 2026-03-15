import pytest
from api.client import BookingAPIClient
from utils.helpers import load_booking_payload as myData
import time
unique_name = f"Anas{int(time.time())}"
delete_name = f"Delete{int(time.time())}"
multi_name = f"Multi{int(time.time())}"


@pytest.mark.hybrid
@pytest.mark.regression
def test_create_booking_visible_via_search(api_client, booking_cleanup):
    res = api_client.create_booking({
  "firstname": unique_name,
  "lastname": "Hassan",
  "totalprice": 200,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2025-06-01",
    "checkout": "2025-06-05"
  },
  "additionalneeds": "Breakfast"
})
    booking_cleanup.append(res["bookingid"])
    response = api_client.get_all_bookings(firstname=unique_name)
    assert len(response) > 0

    booking_id = response[0]["bookingid"]
    api_client.delete_booking(booking_id)
    assert len(api_client.get_all_bookings(firstname=unique_name)) == 0



@pytest.mark.regression
@pytest.mark.hybrid
def test_delete_via_api_booking_gone_from_search(api_client, booking_cleanup):
    res = api_client.create_booking({
  "firstname": delete_name,
  "lastname": "Hassan",
  "totalprice": 200,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2025-06-01",
    "checkout": "2025-06-05"
  },
  "additionalneeds": "Breakfast"
})
    booking_cleanup.append(res["bookingid"])
    response = api_client.get_all_bookings(firstname=delete_name)
    booking_id = response[0]["bookingid"]
    api_client.delete_booking(booking_id)
    assert len(api_client.get_all_bookings(firstname=delete_name)) == 0


@pytest.mark.regression
@pytest.mark.hybrid
def test_create_multiple_bookings_all_searchable(api_client, booking_cleanup):
    res1 = api_client.create_booking({
  "firstname": multi_name,
  "lastname": "Hassan",
  "totalprice": 200,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2025-06-01",
    "checkout": "2025-06-05"
  },
  "additionalneeds": "Breakfast"
})
    booking_cleanup.append(res1["bookingid"])

    res2 = api_client.create_booking({
  "firstname": multi_name,
  "lastname": "Hassan",
  "totalprice": 200,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2025-06-01",
    "checkout": "2025-06-05"
  },
  "additionalneeds": "Breakfast"
})
    booking_cleanup.append(res2["bookingid"])

    res3 = api_client.create_booking({
  "firstname": multi_name,
  "lastname": "Hassan",
  "totalprice": 200,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2025-06-01",
    "checkout": "2025-06-05"
  },
  "additionalneeds": "Breakfast"
})
    booking_cleanup.append(res3["bookingid"])

    assert len(api_client.get_all_bookings(firstname = multi_name)) >= 3