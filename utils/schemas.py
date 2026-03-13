
CREATE_BOOKING_SCHEMA = {
    "type": "object",
    "required": ["bookingid", "booking"],
    "properties": {
        "bookingid": {"type": "integer"},
        "booking": {
            "type": "object",
            "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"],
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "additionalneeds": {"type": "string"},
                "bookingdates":{
                    "type": "object",
                    "required": ["checkin", "checkout"],
                    "properties": {
                    "checkin": {"type": "string"},
                    "checkout": {"type": "string"},
                }
            },
            }
        }
    }
}


GET_BOOKING_SCHEMA = {
    "type": "object",
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"],
    "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "additionalneeds": {"type": "string"},
                "bookingdates":{
                    "type": "object",
                    "required": ["checkin", "checkout"],
                    "properties": {
                    "checkin": {"type": "string"},
                    "checkout": {"type": "string"}
                    }
                }
            },

}

