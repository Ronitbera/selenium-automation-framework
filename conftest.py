import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    driver.maximize_window()

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome, edge, or firefox"
    )