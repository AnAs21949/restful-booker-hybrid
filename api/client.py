import requests
from .endpoints import BASE_URL, BOOKING_URL

class BookingAPIClient():
    def __init__(self):
        self.token = ""
    
    def authenticate(self, username, password):
        response = requests.post(f"{BASE_URL}/auth", json={"username": username, "password": password})
        self.token = response.json().get("token", "")
        return response.json()
    
    def create_booking(self, payload):
        return requests.post(BOOKING_URL, json=payload).json()


    def get_booking(self, booking_id):
        return requests.get(f"{BOOKING_URL}/{booking_id}").json()

    def get_all_bookings(self, **params):
        return requests.get(BOOKING_URL, params=params).json()
    
    def update_booking(self, booking_id, payload):
        headers = {"Cookie": f"token={self.token}"}
        return requests.put(f"{BOOKING_URL}/{booking_id}", json=payload, headers=headers).json()
    
    
    def delete_booking(self, booking_id):
        headers = {"Cookie": f"token={self.token}"}
        url = f"{BOOKING_URL}/{booking_id}"
        response = requests.delete(url, headers=headers)
        return response.status_code