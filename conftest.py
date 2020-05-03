import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, IeOptions, FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        required=True,
        help="Request URL"
    )
    parser.addoption(
        "--browser",
        required=True,
        help="Browser to test. Available browsers: Chrome, IE, Firefox"
    )


@pytest.fixture()
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def browser_in_use(request, get_browser):
    if get_browser.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument('headless')
        options.add_argument('start-fullscreen')
        wd = webdriver.Chrome(options=options)
        request.addfinalizer(wd.quit)
        return wd
    elif get_browser.lower() == "ie":
        wd = webdriver.Ie()
        wd.fullscreen_window()
        request.addfinalizer(wd.quit)
        return wd
    elif get_browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument('-kiosk')          # full-screen mode
        wd = webdriver.Firefox(options=options)
        request.addfinalizer(wd.quit)
        return wd
    else:
        raise ValueError("Incorrect browser")
