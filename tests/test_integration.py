from api.product_api import create_product
from pages.login_page import LoginPage

def test_api_ui_integration(setup):
    driver = setup

    # Step 1: API call (create product)
    payload = {
        "title": "Integration Product",
        "price": 200,
        "description": "Test integration",
        "category": "electronics"
    }

    response = create_product(payload)
    assert response.status_code == 201

    data = response.json()
    product_title = data["title"]

    print("API Product Created:", product_title)

    # Step 2: UI login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Step 3: Validate UI page
    assert "inventory" in driver.current_url

    print("UI Login Successful ✅")