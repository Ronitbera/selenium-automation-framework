from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


def test_complete_checkout(driver):
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

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.enter_first_name("Ronit")
    checkout_page.enter_last_name("Bera")
    checkout_page.enter_postal_code("700001")

    checkout_page.click_continue()
    checkout_page.click_finish()

    assert checkout_page.is_order_complete()
    assert checkout_page.get_success_message() == "Thank you for your order!"
def test_checkout_without_first_name(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.enter_last_name("Bera")
    checkout_page.enter_postal_code("700001")

    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert "First Name is required" in error_message
