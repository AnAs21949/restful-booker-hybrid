import pytest
from pages.admin_panel_page import AdminPanelPage

@pytest.mark.smoke
def test_admin_panel_shows_bookings(logged_in_driver):
    admin_panel_page = AdminPanelPage(logged_in_driver)
    admin_panel_page.click_room(1)
    rows = admin_panel_page.get_booking_rows()
    assert len(rows) > 0
