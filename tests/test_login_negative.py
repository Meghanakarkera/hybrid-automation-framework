import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.login("invalid_user", "wrong_pass")

    error_text = login.get_error_message()

    assert "Username and password do not match" in error_text