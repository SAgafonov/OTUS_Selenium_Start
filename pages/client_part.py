import inspect
import logging
from helpers.client_helper import CLIENT_CATALOG_SUB_URL, CLIENT_ARTICLE_CARD_SUB_URL, CLIENT_LOGIN_PAGE_SUB_URL
from .base import BasePage

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class ClientNoAuthorized(BasePage):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        super().__init__(driver=driver, url=self.url)

    def open_page(self):
        # Получаем имя модуля, откуда вызывается функция
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        if mod.__name__ == "tests.client_part.test_article_card":
            sub_url = CLIENT_ARTICLE_CARD_SUB_URL
        elif mod.__name__ == "tests.client_part.test_catalog_page":
            sub_url = CLIENT_CATALOG_SUB_URL
        elif mod.__name__ == "tests.client_part.test_client_login_page":
            sub_url = CLIENT_LOGIN_PAGE_SUB_URL
        else:
            sub_url = "/"
        logger.info("Open URL {}".format(self.url + sub_url))
        self.driver.get(self.url + sub_url)
