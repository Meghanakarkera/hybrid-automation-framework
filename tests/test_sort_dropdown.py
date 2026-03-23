import pytest
from selenium.webdriver.support.ui import Select
import time

@pytest.mark.ui
def test_sort_dropdown(setup):
    driver = setup

    # Login
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Dropdown
    dropdown = Select(driver.find_element("class name", "product_sort_container"))
    dropdown.select_by_visible_text("Price (low to high)")

    time.sleep(3)