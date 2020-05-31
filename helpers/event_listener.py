import logging
from datetime import datetime
from .general_settings import PATH_TO_SCREENSHOTS
from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class MyListener(AbstractEventListener):

    def after_find(self, by, value, driver):
        for item in driver.get_log("browser"):
            logger.debug(item)

    def before_quit(self, driver):
        logger.debug("Quit {driver}".format(driver=driver.name.capitalize()))

    def after_quit(self, driver):
        logger.debug(">>>>> {driver} is quit <<<<<".format(driver=driver.name.capitalize()))

    def on_exception(self, exception, driver):
        logger.error("Got an Exception: {exception}".format(exception=exception))
        driver.save_screenshot("{path}{screen_name}.png".format(path=PATH_TO_SCREENSHOTS,
                                                                screen_name=datetime.now().strftime("%H-%M-%S")))
