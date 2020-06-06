import logging
import pytest
from helpers.event_listener import MyListener
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
        help="Browser to test. Available browsers: Chrome, IE, Firefox"
    )


@pytest.fixture(scope="module")
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def browser_in_use(request, get_browser):
    if get_browser.lower() == "chrome":
        caps = DesiredCapabilities.CHROME
        caps["loggingPrefs"] = {"performance": "ALL", "browser": "ALL"}
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1200x600')  # Исправляет ошибку, когде не видны элементы фильтра продукта в headless режиме
        options.add_argument('--start-fullscreen')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("w3c", False)
        wd = EventFiringWebDriver(webdriver.Chrome(
            options=options,
            desired_capabilities=caps,
            service_log_path=PATH_TO_LOGS + "chrome_logs.log"
            ), MyListener()
        )
        # wd.implicitly_wait(5)
        request.addfinalizer(wd.quit)
        return wd

    elif get_browser.lower() == "ie":
        wd = webdriver.Ie()
        wd.fullscreen_window()
        # wd.implicitly_wait(5)
        request.addfinalizer(wd.quit)
        return wd
    elif get_browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument('-kiosk')  # full-screen mode
        wd = webdriver.Firefox(options=options, service_log_path=PATH_TO_LOGS + "geckodriver.log")
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        # wd.implicitly_wait(5)
        request.addfinalizer(wd.quit)
        return wd
    else:
        raise ValueError("Incorrect browser")


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
