# Restful Booker Hybrid Test Framework

A hybrid API + UI automation framework built with Python, pytest, and Selenium.
The framework targets restful-booker.herokuapp.com (API) and
automationintesting.online (UI). Investigation confirmed these are independent
backends, a real-world finding documented here as a constraint of the test environment.

## Tech Stack

- Python 3.13
- pytest + pytest-html
- Selenium + webdriver-manager
- requests
- jsonschema
- GitHub Actions CI

## Project Structure

```
restful-booker-hybrid/
    api/                  # API client layer (BookingAPIClient)
    pages/                # Selenium page objects (POM)
    tests/
        test_api/         # 11 API tests
        test_ui/          # 4 UI tests
        test_hybrid/      # 4 hybrid cross-layer tests
    utils/                # schemas, helpers, config
    data/                 # test data JSON files
    conftest.py           # fixtures: api_client, driver, booking_cleanup
    pytest.ini            # markers: smoke, regression, negative, hybrid
```

## Setup

```bash
git clone https://github.com/AnAs21949/restful-booker-hybrid
cd restful-booker-hybrid
pip install -r requirements.txt
```

## Running Tests

```bash
# Full suite
pytest tests/ -v

# By layer
pytest tests/test_api/ -v
pytest tests/test_ui/ -v
pytest tests/test_hybrid/ -v

# By marker
pytest -m smoke -v
pytest -m regression -v
pytest -m negative -v
pytest -m hybrid -v

# With HTML report
pytest tests/ --html=report.html --self-contained-html
```

## Key Concepts Demonstrated

- **BookingAPIClient** — API equivalent of the Page Object Model. Tests never
  call `requests` directly, just as they never call `driver.find_element()` directly.
- **Schema validation** — responses validated with `jsonschema`, not just status codes.
- **Test data lifecycle** — `booking_cleanup` fixture deletes created data in
  teardown, even on test failure.
- **Hybrid tests** — cross-layer tests with the `hybrid` marker that verify data
  created in one layer appears correctly in the other.

## CI

GitHub Actions pipeline runs on every push to main — API tests first, then UI,
then hybrid. Pipeline badge reflects current status.
