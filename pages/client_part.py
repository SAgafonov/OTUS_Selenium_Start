from .base import BasePage


class ClientNoAuthorized(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
