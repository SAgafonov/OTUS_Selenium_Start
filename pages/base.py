from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)

    def look_for_element(self, locator, selector, attribute=None, timeout=5):
        """
        Opens the necessary page;
        Waits until element appears and returns the element
        :param locator: How to search the element
        :param selector: What search in HTML code
        :param attribute: attribute of elements that is looked for
        :param timeout: int. Seconds to wait for the element
        :return: element
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator, selector)))
            if attribute:
                return self.driver.find_element(locator, selector).get_attribute(attribute)
            return self.driver.find_element(locator, selector)
        except TimeoutException:
            raise AssertionError("Element '{}' is not appeared in {} seconds".format(selector, timeout))

    def look_for_elements(self, locator, selector, timeout=5):
        """
        Opens the necessary page;
        Waits until elements appears and returns the list of elements
        :param locator: How to search the element
        :param selector: What search in HTML code
        :param timeout: int. Seconds to wait for the element
        :return: list of elements
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator, selector)))
            return self.driver.find_elements(locator, selector)
        except TimeoutException:
            raise AssertionError("Element '{}' is not appeared in {} seconds".format(selector, timeout))

    def alert_accept(self, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            raise AssertionError("Element alert popup is not appeared in {} seconds".format(timeout))
