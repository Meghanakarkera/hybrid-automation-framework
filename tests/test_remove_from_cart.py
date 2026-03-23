import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_remove_from_cart(setup):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_product_to_cart()
    inventory.remove_product()

    # Optional: verify cart badge disappears
    elements = driver.find_elements("class name", "shopping_cart_badge")
    assert len(elements) == 0