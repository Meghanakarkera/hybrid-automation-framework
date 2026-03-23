from pages.login_page import LoginPage
import pytest

@pytest.mark.ui
def test_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
