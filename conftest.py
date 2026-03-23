import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest_html
import os
from datetime import datetime

@pytest.fixture
def setup():
    options = Options()

    #options.add_argument("--headless=new")   # 🔥 updated
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
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("setup")

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            # Capture screenshot ONLY if failed
            if report.failed:
                driver.save_screenshot(file_path)

                # Attach to HTML report
                if "pytest_html" in item.config.pluginmanager.plugins:
                    extra = getattr(report, "extra", [])
                    extra.append(pytest_html.extras.image(file_path))
                    report.extra = extra

