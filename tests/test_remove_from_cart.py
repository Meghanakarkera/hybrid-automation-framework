import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
def test_remove_from_cart(setup):
    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_product_to_cart()
    inventory.remove_product()

    # Optional: verify cart badge disappears
    badge_disappeared = WebDriverWait(driver, timeout=5).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert badge_disappeared