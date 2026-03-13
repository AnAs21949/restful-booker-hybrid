import pytest
from selenium import webdriver
from api.client import BookingAPIClient
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage



@pytest.fixture(scope='session')
def api_client():
    client = BookingAPIClient()
    client.authenticate("admin", "password123")
    yield client

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def booking_cleanup(api_client):
    IDs = []
    yield IDs
    for id in IDs:
        api_client.delete_booking(id)

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    driver.get("https://automationintesting.online/admin")
    login_page.login("admin", "password")
    login_page.wait_for_url("admin/rooms")
    yield driver

