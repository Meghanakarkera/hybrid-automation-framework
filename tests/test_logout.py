import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_logout(setup):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.logout()

    assert "saucedemo.com" in driver.current_url