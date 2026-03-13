from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "doLogin")
    error_message = (By.CSS_SELECTOR, ".alert.alert-danger")

    def login(self, user_name, user_password):
        self.type(self.username, user_name)
        self.type(self.password, user_password)
        self.click(self.login_button)

    def get_error_msg(self):
        return self.text(self.error_message)
