import logging
import pytest
from helpers.event_listener import MyListener
from helpers.define_executor import Executor
from helpers.general_settings import PATH_TO_LOGS
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from pages.admin_part import AdminLoginPage, AdminProductPage
from pages.client_part import ClientNoAuthorized
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Set log level for Selenium and urllib3 to Warning
LOGGER.setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# Configure general settings for logs
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s() - %(message)s',
    filemode='w',   # Rewrite logs
    filename=PATH_TO_LOGS + "logs.log"
)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        required=False,
        default="http://localhost/",
        help="Request URL"
    )
    parser.addoption(
        "--browser",
        required=False,
        default="chrome",
        choices=["chrome", "ie", "firefox"],
        help="Browser to test. Available browsers: Chrome, IE, Firefox"
    )
    parser.addoption(
        "--remote_type",
        required=False,
        default="local",
        choices=["local", "local_grid", "cloud"],
        help="Defines how to run tests: locally, using grid or cloud service. Available values: local, local_grid, cloud"
    )
    parser.addoption(
        "--executor-url",
        required=False,
        help="Defines URL where tests will be executed"
    )


@pytest.fixture(scope="module")
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def get_remote_type(request):
    return request.config.getoption("--remote_type")


@pytest.fixture(scope="module")
def get_executor_url(request):
    return request.config.getoption("--executor-url")


@pytest.fixture(scope="class")
def browser_in_use(request, get_browser, get_remote_type, get_executor_url):
    e = Executor(get_browser.lower(), get_remote_type.lower(), get_executor_url)
    wd = e.determine_webdriver()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture()
def title_to_check():
    page_title = "Your Store"
    return page_title


@pytest.fixture()
def admin_login_page(browser_in_use, get_url):
    return AdminLoginPage(browser_in_use, get_url)


@pytest.fixture()
def admin_product_page(browser_in_use, get_url):
    return AdminProductPage(browser_in_use, get_url)


@pytest.fixture(scope="class")
def client_not_authorized_zone(browser_in_use, get_url):
    return ClientNoAuthorized(browser_in_use, get_url)


@pytest.fixture()
def to_perform_action(browser_in_use):
    return ActionChains(browser_in_use)
