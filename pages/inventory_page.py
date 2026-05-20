from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    menu_btn = (By.ID, "react-burger-menu-btn")
    logout_btn = (By.ID, "logout_sidebar_link")

    # Actions

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def get_cart_count(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.cart_badge)
        )
        return element.text

    def logout(self):
        self.driver.find_element(*self.menu_btn).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_btn)
        ).click()

    # New Locators
    remove_btn = (By.ID, "remove-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    # Checkout Locators
    checkout_btn = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")

    # New Actions

    def remove_product(self):
        self.driver.find_element(*self.remove_btn).click()

    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart = wait.until(EC.element_to_be_clickable(self.cart_icon))
        cart.click()

    def safe_type(self, locator, value):
        wait = WebDriverWait(self.driver, 10)

        for _ in range(3):
            field = wait.until(EC.element_to_be_clickable(locator))
            field.clear()
            field.send_keys(value)

            try:
                #  re-fetch element (VERY IMPORTANT)
                wait.until(lambda d: d.find_element(*locator).get_attribute("value").strip() == str(value).strip())
                return
            except:
                print(f"Retrying for {value}...")

        raise Exception(f"Unable to enter value: {value}")

    #  CHECKOUT FLOW
    def checkout(self, fname, lname, zip_code):
        wait = WebDriverWait(self.driver, 10)

        # Ensure cart page
        wait.until(EC.url_contains("cart"))

        # Click checkout
        checkout_btn = wait.until(
            EC.element_to_be_clickable(self.checkout_btn)
        )
        self.driver.execute_script("arguments[0].click();", checkout_btn)

        # Wait for step one page
        wait.until(EC.visibility_of_element_located(self.first_name))

        # Fill details (STABLE)
        self.safe_type(self.first_name, fname)
        self.safe_type(self.last_name, lname)
        self.safe_type(self.postal_code, zip_code)

        # Click Continue
        continue_btn = wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        )
        self.driver.execute_script("arguments[0].click();", continue_btn)

        # Check for errors AFTER clicking continue
        error = self.driver.find_elements(By.CLASS_NAME, "error-message-container")
        if error and error[0].text.strip():
            raise Exception(f"Checkout failed: {error[0].text}")

        # Wait for step two
        wait.until(EC.visibility_of_element_located(self.finish_btn))

        # Click Finish
        finish_btn = wait.until(
            EC.element_to_be_clickable(self.finish_btn)
        )
        self.driver.execute_script("arguments[0].click();", finish_btn)

    def get_success_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.success_msg)
        ).text