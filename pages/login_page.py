from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    # Add popup locator (adjust if needed)
    popup_ok_btn = (By.XPATH, "//button[contains(text(),'OK')]")

    error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    # Actions
    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

        self.close_popup_if_present()


    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text

    def close_popup_if_present(self):
        try:
            popup = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.popup_ok_btn)
            )
            popup.click()
            print("Popup closed")
        except:
            print("No popup")

