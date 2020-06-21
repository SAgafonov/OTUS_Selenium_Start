from helpers.event_listener import MyListener
from helpers.general_settings import PATH_TO_LOGS
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Executor:
    """
        Define webdriver considering options, desired caps,
        the way how to execute tests either locally, using local grid or in cloud
    """

    def __init__(self, browser: str, remote_type: str, executor_url: str):
        self._browser = browser
        self._remote_type = remote_type
        self._options = None
        self._caps = None
        self._executor_url = executor_url

    def determine_options(self):
        if self._browser == "chrome":
            caps = DesiredCapabilities.CHROME
            caps["loggingPrefs"] = {"performance": "ALL", "browser": "ALL"}
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument(
                '--window-size=1200x600')  # Исправляет ошибку, когде не видны элементы фильтра продукта в headless режиме
            options.add_argument('--start-fullscreen')
            options.add_argument('--ignore-certificate-errors')
            options.add_experimental_option("w3c", False)
            self._options = options
            self._caps = caps
        elif self._browser == "firefox":
            options = FirefoxOptions()
            options.add_argument('-headless')
            options.add_argument('-kiosk')  # full-screen mode
            self._options = options
            self._caps = {}

    def determine_webdriver(self):
        wd = None
        self.determine_options()
        if self._remote_type == "local":
            if self._browser == "chrome":
                wd = EventFiringWebDriver(webdriver.Chrome(
                    options=self._options,
                    desired_capabilities=self._caps,
                    service_log_path=PATH_TO_LOGS + "chrome_logs.log"
                    ), MyListener()
                )
                return wd
            elif self._browser == "firefox":
                wd = webdriver.Firefox(options=self._options, service_log_path=PATH_TO_LOGS + "geckodriver.log")
                profile = webdriver.FirefoxProfile()
                profile.accept_untrusted_certs = True
                return wd
            elif self._browser == "ie":
                wd = webdriver.Ie()
                wd.fullscreen_window()
                return wd
        elif self._remote_type == "local_grid":
            if not self._executor_url:
                raise AttributeError("URL to remote resource is not provided!")
            wd = webdriver.Remote(command_executor=self._executor_url,
                                  desired_capabilities=self._caps,
                                  options=self._options)
        elif self._remote_type == "cloud":
            if not self._executor_url:
                raise AttributeError("URL to remote resource is not provided!")
            desired_cap = {
                'os': 'Windows',
                'os_version': '10',
                # 'browser': 'Chrome',
                # 'browser_version': '80',
                'name': "Upload_File_New"
            }
            self._caps = {**self._caps, **desired_cap}
            wd = webdriver.Remote(command_executor=self._executor_url,
                                  desired_capabilities=self._caps,
                                  options=self._options)
        elif self._remote_type == "selenoid":
            if not self._executor_url:
                self._executor_url = "http://localhost:4444/wd/hub"
            desired_cap = {
                'browserName': self._browser,
                # 'version': "65.0",
                # 'enableVnc': True,
                # 'enableVideo': True,
                # 'enableLog': True,
                'name': "Selenoid"
            }
            self._caps = {**self._caps, **desired_cap}
            wd = webdriver.Remote(command_executor=self._executor_url,
                                  desired_capabilities=self._caps,
                                  options=self._options)
        if not wd:
            raise ValueError("'webdriver' is not defined")
        return wd
