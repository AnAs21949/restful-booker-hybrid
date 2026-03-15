import pytest
from pages.booking_page import BookingPage
from pages.admin_panel_page import AdminPanelPage

@pytest.mark.hybrid
@pytest.mark.regression
def test_booking_created_via_api_retrievable_by_id(api_client, booking_cleanup):
    response = api_client.create_booking({
  "firstname": "bookingAnas",
  "lastname": "ABID",
  "totalprice": 200,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2025-06-01",
    "checkout": "2025-06-05"
  },
  "additionalneeds": "Breakfast"
})
    booking_id = response["bookingid"]
    my_booking =  api_client.get_booking(response["bookingid"])
    assert my_booking["firstname"] == "bookingAnas", "firstname hasn't been detected"
    assert my_booking["lastname"] == "ABID", "lastname hasn't been detected"
    assert my_booking["totalprice"] == 200, "totalprice doesn't match"
    booking_cleanup.append(booking_id)


