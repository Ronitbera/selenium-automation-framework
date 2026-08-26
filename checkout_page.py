from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.enter_text(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self):
        return self.wait_for_element(
            self.COMPLETE_HEADER
        ).is_displayed()

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)