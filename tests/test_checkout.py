import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_checkout_flow(setup):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Login
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory.add_product_to_cart()

    # Go to cart
    inventory.go_to_cart()

    # Checkout
    inventory.checkout("Meghana", "Karkera", "575001")

    # Validate success
    success_text = inventory.get_success_message()

    assert "THANK YOU" in success_text.upper()