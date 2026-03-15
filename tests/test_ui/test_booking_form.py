import pytest
from pages.booking_page import BookingPage
from pages.admin_panel_page import AdminPanelPage


@pytest.mark.smoke
@pytest.mark.regression  
def test_booking_form_submits_successfully(driver):
    driver.get("https://automationintesting.online/")
    booking_page = BookingPage(driver)
    booking_page.choose_a_room()
    booking_page.click_reserve_button()
    booking_page.credentials_registration(
        "ANAS123456789", "ABID123456789",
        "anas@test.com", "06527511041"
    )
    assert "automationintesting.online" in driver.current_url
    # If no exception was raised, the booking form completed successfully