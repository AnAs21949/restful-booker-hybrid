import pytest
from jsonschema import validate
from utils.schemas import CREATE_BOOKING_SCHEMA, GET_BOOKING_SCHEMA
from utils.helpers import load_booking_payload

@pytest.mark.regression
def test_create_booking_response_matches_schema(api_client,booking_cleanup):
    response =  api_client.create_booking(load_booking_payload())
    validate(instance=response, schema=CREATE_BOOKING_SCHEMA)
    booking_cleanup.append(response["bookingid"])


@pytest.mark.regression
def test_get_booking_response_matches_schema(api_client,booking_cleanup):
    client = api_client
    book_response =  api_client.create_booking(load_booking_payload())
    id_booking = book_response["bookingid"]
    response =  client.get_booking(id_booking)
    validate(instance=response, schema=GET_BOOKING_SCHEMA)
    booking_cleanup.append(id_booking)

