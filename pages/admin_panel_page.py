from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPanelPage(BasePage):
    booking_row = (By.CSS_SELECTOR, "[class*='detail booking-']")

    def click_room(self,room_number):
        self.click((By.ID, f"room{room_number}"))

    def get_booking_rows(self):
        self.wait_element(self.booking_row)
        return self.driver.find_elements(*self.booking_row)
    
    def is_booking_visible(self, firstname):
        for row in self.get_booking_rows():
            name = row.find_element(By.CSS_SELECTOR, ".col-sm-2 p").text
            if name == firstname:
                return True
        return False
    