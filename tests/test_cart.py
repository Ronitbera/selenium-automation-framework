from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


def test_add_product_to_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.get_cart_item_count() == 1
    assert "Sauce Labs Backpack" in cart_page.get_cart_item_names()


def test_remove_product_from_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.get_cart_item_count() == 1

    cart_page.remove_product("Sauce Labs Backpack")

    assert cart_page.get_cart_item_count() == 0
def test_add_multiple_products_to_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    product_names = cart_page.get_cart_item_names()

    assert cart_page.get_cart_item_count() == 2
    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names
