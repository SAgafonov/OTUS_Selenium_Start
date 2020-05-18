import random
from look_for_elements import FindElements
from admin_helper import SELECTORS_FOR_PRODUCTS, SELECTORS_GENERAL, SELECTORS_LEFT_NAV_MENU, USERNAME, PASSWORD
from selenium.webdriver.common.by import By


class Precondition:

    def __init__(self, driver):
        self.driver = driver
        self.find_element = FindElements(self.driver)

    def login(self, url):
        self.find_element.open_page(url)
        login_input = self.find_element.look_for_element(By.CSS_SELECTOR, SELECTORS_GENERAL["login_selector"])
        password_input = self.find_element.look_for_element(By.CSS_SELECTOR, SELECTORS_GENERAL["password_selector"])

        login_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        password_input.submit()

    def admin_navigate_to_products(self):
        path_to_product = self.find_element.look_for_element(By.CSS_SELECTOR, SELECTORS_LEFT_NAV_MENU["catalog_element"])
        path_to_product.click()
        path_to_product = self.find_element.look_for_element(By.CSS_SELECTOR, SELECTORS_LEFT_NAV_MENU["product_element"])
        path_to_product.click()

    def create_product(self):
        text_fields_to_be_changed = {
            "prod_name_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "meta_tag_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "model_in_edit": "Test_prod_model_in_edit_",
            "price_in_edit": "1000.00",
            "quantity_in_edit": "100"
        }
        add_product_btn = self.find_element.look_for_element(By.CSS_SELECTOR, SELECTORS_FOR_PRODUCTS["add_product_btn"])
        add_product_btn.click()

        for key in text_fields_to_be_changed:
            self.driver.execute_script(f"$(\"{SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_changed.get(key)}\";")

        save_btn = self.find_element.look_for_element(By.CSS_SELECTOR, SELECTORS_FOR_PRODUCTS["save_btn"])
        save_btn.click()

