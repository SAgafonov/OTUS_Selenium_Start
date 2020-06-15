import allure
import logging
from helpers.general_settings import PATH_TO_LOGS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        logger.info("Open URL {}".format(self.url))
        self.driver.get(self.url)

    def look_for_element(self, selector, locator=By.CSS_SELECTOR, attribute=None, timeout=5):
        """
        Opens the necessary page;
        Waits until element appears and returns the element
        :param locator: webdriver.common.by: How to search the element
        :param selector: string: What search in HTML code
        :param attribute: string: attribute of elements that is looked for
        :param timeout: int: Seconds to wait for the element
        :return: element
        """
        print(locator)
        try:
            logger.debug("Look for element using '{}' locator and '{}' selector".format(locator, selector))
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator, selector)))
            if attribute:
                logger.debug("Return attributes of the element which has '{}' selector".format(selector))
                return self.driver.find_element(locator, selector).get_attribute(attribute)
            return self.driver.find_element(locator, selector)
        except TimeoutException:
            logger.exception("Element '{}' is not appeared in {} seconds".format(selector, timeout))
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            allure.attach.file(source=PATH_TO_LOGS + "chrome_logs.log",
                               attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Element '{}' is not appeared in {} seconds".format(selector, timeout))

    def look_for_elements(self, selector, locator=By.CSS_SELECTOR, timeout=5):
        """
        Opens the necessary page;
        Waits until elements appears and returns the list of elements
        :param locator: How to search the element
        :param selector: What search in HTML code
        :param timeout: int. Seconds to wait for the element
        :return: list of elements
        """
        try:
            logger.debug("Look for elements using '{}' locator and '{}' selector".format(locator, selector))
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator, selector)))
            return self.driver.find_elements(locator, selector)
        except TimeoutException:
            logger.exception("Element '{}' is not appeared in {} seconds".format(selector, timeout))
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            allure.attach.file(source=PATH_TO_LOGS + "chrome_logs.log",
                               attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Element '{}' is not appeared in {} seconds".format(selector, timeout))

    @allure.step("Accept browser alert")
    def alert_accept(self, timeout=3):
        try:
            logger.debug("Wait until alert is appeared")
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            logger.debug("Switch to alert")
            alert = self.driver.switch_to.alert
            logger.info("Accept alert")
            alert.accept()
        except TimeoutException:
            logger.exception("Element alert popup is not appeared in {} seconds".format(timeout))
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            allure.attach.file(source=PATH_TO_LOGS + "chrome_logs.log",
                               attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Element alert popup is not appeared in {} seconds".format(timeout))
