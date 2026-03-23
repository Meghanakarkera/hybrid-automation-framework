from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        return self.driver.find_element(*self.cart_badge).text

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
        self.driver.find_element(*self.cart_icon).click()

    def checkout(self, fname, lname, zip_code):

        # Click checkout
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_btn)
        ).click()

        # Fill form
        first = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        )
        first.clear()
        first.send_keys(fname)

        last = self.driver.find_element(*self.last_name)
        last.clear()
        last.send_keys(lname)

        zipc = self.driver.find_element(*self.postal_code)
        zipc.clear()
        zipc.send_keys(zip_code)

        # Wait until all values are entered
        WebDriverWait(self.driver, 10).until(
            lambda d: first.get_attribute("value") and
                      last.get_attribute("value") and
                      zipc.get_attribute("value")
        )

        # Continue button with RETRY logic
        for i in range(3):
            try:
                continue_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.continue_btn)
                )
                self.driver.execute_script("arguments[0].click();", continue_btn)

                # Wait for next page
                WebDriverWait(self.driver, 5).until(
                    EC.url_contains("checkout-step-two")
                )
                print("Moved to step-two")
                break
            except:
                print(f"Retrying Continue click... attempt {i + 1}")

        # Final check (fail early if still not moved)
        assert "checkout-step-two" in self.driver.current_url, "Did not reach checkout step two"

        # Finish button
        finish_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.finish_btn)
        )
        self.driver.execute_script("arguments[0].click();", finish_btn)

    def get_success_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.success_msg)
        ).text