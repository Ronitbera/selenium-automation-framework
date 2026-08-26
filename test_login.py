import pytest

from pages.login_page import LoginPage
from config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD
)


def test_valid_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    assert "/inventory.html" in driver.current_url


@pytest.mark.parametrize(
    "username, password",
    [
        (VALID_USERNAME, "wrong_password"),
        ("wrong_user", VALID_PASSWORD),
        ("wrong_user", "wrong_password"),
    ]
)
def test_invalid_login(driver, username, password):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    actual_message = login_page.get_error_message_text()

    assert "Username and password do not match" in actual_message