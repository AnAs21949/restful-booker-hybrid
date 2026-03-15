import pytest
from selenium import webdriver
from api.client import BookingAPIClient
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import os
import datetime





@pytest.fixture(scope='session')
def api_client():
    client = BookingAPIClient()
    client.authenticate("admin", "password123")
    yield client



@pytest.fixture(scope='function')
def driver():
    options = Options()
    if os.getenv('CI'):
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report  = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver is None:
            return  # test API-only, pas de screenshot
        screenshots_dir = os.path.join("screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"{item.name}__{ts}.png"
        path = os.path.join(screenshots_dir, name)
        driver.save_screenshot(path)
        print(f"\n[SCREENSHOT] {path}")
