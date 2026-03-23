import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),        # valid
    ("locked_out_user", "secret_sauce"),      # locked user
    ("problem_user", "wrong_password"),       # wrong password
    ("invalid_user", "invalid_pass")          # invalid user
])
def test_login_data_driven(setup, username, password):
    driver = setup
    login = LoginPage(driver)

    login.login(username, password)

    current_url = driver.current_url

    if username == "standard_user" and password == "secret_sauce":
        assert "inventory" in current_url
    else:
        assert "inventory" not in current_url