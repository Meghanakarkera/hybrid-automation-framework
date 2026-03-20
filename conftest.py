import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    options = Options()

    options.add_argument("--headless=new")   # 🔥 updated
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")   # 🔥 important
    options.add_argument("--window-size=1920,1080")  # 🔥 important

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            driver.save_screenshot("screenshots/failure.png")