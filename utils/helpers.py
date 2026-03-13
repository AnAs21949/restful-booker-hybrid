import json

def load_booking_payload():
    with open("data/booking_payload.json") as f:
        return json.load(f)