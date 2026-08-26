from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_element(self, locator):
        self.logger.info(f"Waiting for element: {locator}")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        self.logger.info(f"Entering text into: {locator}")
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Getting text from: {locator}")
        return self.wait_for_element(locator).text
