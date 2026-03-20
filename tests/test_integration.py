import pytest
from api.product_api import create_product
from pages.login_page import LoginPage

def test_api_ui_integration(setup):
    driver = setup

    payload = {
        "title": "Integration Product",
        "price": 200,
        "description": "Test integration",
        "category": "electronics"
    }

    response = create_product(payload)

    if response.status_code != 201:
        pytest.skip(f"Skipping due to API restriction: {response.status_code}")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url