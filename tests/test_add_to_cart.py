import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_add_to_cart(setup):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_product_to_cart()

    cart_count = inventory.get_cart_count()

    assert cart_count == "1"