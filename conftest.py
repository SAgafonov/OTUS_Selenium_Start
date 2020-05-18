import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from look_for_elements import FindElements
from preconditions import Precondition
from selenium.webdriver.common.action_chains import ActionChains


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


@pytest.fixture(scope="module")
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def browser_in_use(request, get_browser):
    if get_browser.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--start-fullscreen')
        options.add_argument('--ignore-certificate-errors')
        wd = webdriver.Chrome(options=options)
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
        wd = webdriver.Firefox(options=options)
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        # wd.implicitly_wait(5)
        request.addfinalizer(wd.quit)
        return wd
    else:
        raise ValueError("Incorrect browser")


@pytest.fixture(scope="class")
def urls(get_url):
    return {"main_page_url": get_url,
            "catalog_url": get_url + "index.php?route=product/category&path=20",
            "article_card_url": get_url + "index.php?route=product/product&path=57&product_id=49",
            "client_login_page_url": get_url + "index.php?route=account/login",
            "admin_login_page_url": get_url + "admin/"}


@pytest.fixture()
def title_to_check():
    page_title = "Your Store"
    return page_title


@pytest.fixture(scope="class")
def initial_search(browser_in_use):
    return FindElements(browser_in_use)


@pytest.fixture()
def precondition(browser_in_use):
    return Precondition(browser_in_use)


@pytest.fixture()
def to_perform_action(browser_in_use):
    return ActionChains(browser_in_use)
