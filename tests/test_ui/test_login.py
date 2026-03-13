import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_admin_login_successful(logged_in_driver):
    assert "admin/rooms" in logged_in_driver.current_url



@pytest.mark.negative
def test_invalid_login_shows_error(driver):
    driver.get("https://automationintesting.online/admin")
    login_page = LoginPage(driver)
    login_page.login("admin", "passwor")
    assert "Invalid credentials" in login_page.get_error_msg()
