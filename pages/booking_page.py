from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BookingPage(BasePage):
    booking_button = (By.CSS_SELECTOR, "a[href*='/reservation/3']")
    reserve_room = (By.ID, "doReservation")
    first_name = (By.CSS_SELECTOR, "input[placeholder='Firstname']")
    last_name = (By.CSS_SELECTOR, "input[placeholder='Lastname']")
    email = (By.CSS_SELECTOR, "input[placeholder='Email']")
    phone = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    reserve_now_button = (By.CSS_SELECTOR, "button[class='btn btn-primary w-100 mb-3']")
    return_home_button = (By.CSS_SELECTOR, "a[type='button']")




    

    def choose_a_room(self):
        self.scroll_and_click(self.booking_button)

    def click_reserve_button(self):
        self.scroll_and_click(self.reserve_room)

    def credentials_registration(self, firstName, lastName, Email, Phone):
        self.type(self.first_name, firstName)
        self.type(self.last_name, lastName)
        self.type(self.email, Email)
        self.type(self.phone, Phone)
        self.scroll_and_click(self.reserve_now_button)
        self.wait_element(self.return_home_button)
        self.scroll_and_click(self.return_home_button)
    

        
    
