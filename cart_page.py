from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_cart_item_names(self):
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def remove_product(self, product_name):
        product = self.wait.until(
            lambda driver: driver.find_element(
                By.XPATH,
                f"//div[contains(@class,'cart_item')]"
                f"[.//div[contains(@class,'inventory_item_name') "
                f"and normalize-space()='{product_name}']]"
            )
        )

        product.find_element(
            By.TAG_NAME, "button"
        ).click()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)