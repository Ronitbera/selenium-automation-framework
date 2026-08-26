from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_inventory_page_displayed(self):
        return self.wait_for_element(
            self.INVENTORY_CONTAINER
        ).is_displayed()

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

def add_product_to_cart(self, product_name):
    product = self.wait.until(
        lambda driver: driver.find_element(
            By.XPATH,
            f"//div[contains(@class,'inventory_item')][.//div[contains(@class,'inventory_item_name') and normalize-space()='{product_name}']]"
        )
    )

    button = product.find_element(By.TAG_NAME, "button")
    button.click()

    self.wait.until(
        lambda driver: button.text == "Remove"
    )

    def open_cart(self):
        self.click(self.CART_LINK)
