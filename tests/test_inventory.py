from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


def test_inventory_page_after_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_inventory_page_displayed()
    assert inventory_page.get_page_title() == "Products"
    assert inventory_page.get_product_count() == 6
