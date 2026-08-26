import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome, edge, or firefox"
    )
