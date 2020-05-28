import random
from admin_helper import CSS_SELECTORS_FOR_PRODUCTS, CSS_SELECTORS_GENERAL, CSS_SELECTORS_LEFT_NAV_MENU, USERNAME, PASSWORD
from selenium.webdriver.common.by import By
from .base import BasePage
from time import sleep


class AdminLoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def _set_username_(self):
        login_input = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["login_selector"])
        login_input.clear()
        login_input.send_keys(USERNAME)

    def _set_password_(self):
        password_input = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["password_selector"])
        password_input.clear()
        password_input.send_keys(PASSWORD)

    def login(self):
        self.open_page()
        self._set_username_()
        self._set_password_()
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["login_btn_selector"]).click()

    def logout(self):
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["logout_btn_selector"]).click()


class AdminProductPage(AdminLoginPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def check_if_authorized(self):
        if not self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["logout_btn_selector"]):
            self.login()

    def check_if_table_with_products_is_not_empty(self, num_of_companies_to_create=1):
        rows_of_products_table = self.look_for_element(By.CSS_SELECTOR, "tbody tr")
        if rows_of_products_table.text == "No results!":
            for i in range(num_of_companies_to_create):
                self.create_product()

    def admin_navigate_to_products(self):
        self.check_if_authorized()
        path_to_product = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_LEFT_NAV_MENU["catalog_element"])
        path_to_product.click()
        path_to_product = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_LEFT_NAV_MENU["product_element"])
        path_to_product.click()

    def create_product(self):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        text_fields_to_be_created = {
            "prod_name_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "meta_tag_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "model_in_edit": "Test_prod_model_in_edit_" + str(random.randint(1, 10000)),
            "price_in_edit": "1000.00",
            "quantity_in_edit": "100"
        }
        add_product_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["add_product_btn"])
        add_product_btn.click()
        for key in text_fields_to_be_created:
            self.driver.execute_script(
                f"$(\"{CSS_SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_created.get(key)}\";")

        save_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["save_btn"])
        save_btn.click()
        return text_fields_to_be_created

    def edit_product(self):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        text_fields_to_be_changed = {
            "prod_name_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "model_in_edit": "Test_prod_model_in_edit_" + str(random.randint(1, 10000)),
            "price_in_edit": "1000.00",
            "quantity_in_edit": "100"
        }

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        edit_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["edit_btn"])
        edit_btn.click()

        for key in text_fields_to_be_changed:
            self.driver.execute_script(
                f"$(\"{CSS_SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_changed.get(key)}\";")

        save_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["save_btn"])
        save_btn.click()
        return text_fields_to_be_changed

    def delete_product(self, name: str = None) -> str:
        """
        Delete either first product or product which name is passed as an argument
        :param name: name of a product which should be deleted
        :return: name of a deleted product
        """
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        rows_of_products_table = self.look_for_elements(By.CSS_SELECTOR, "tbody tr")
        if not name:
            name_of_deleted_product = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
            select_product_chck_box = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(1)")
        else:
            name_of_deleted_product = name
            for row in rows_of_products_table:
                if name_of_deleted_product == row.find_element_by_css_selector(
                        "td:nth-child(3)").text:
                    select_product_chck_box = row.find_element_by_css_selector("td:nth-child(1)")

        select_product_chck_box.click()
        del_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["delete_product_btn"])
        del_btn.click()
        self.alert_accept()
        return name_of_deleted_product

    def delete_all_products(self):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["checkbox_select_all"]).click()
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["delete_product_btn"]).click()
        self.alert_accept()

    def copy_product(self):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        rows_of_products_table = self.look_for_elements(By.CSS_SELECTOR, "tbody tr")
        name_of_copied_product = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
        select_product_chck_box = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(1)")
        select_product_chck_box.click()
        copy_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["copy_product_btn"])
        copy_btn.click()
        return name_of_copied_product

    def filter_product(self, field_to_filter_by):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        rows_of_products_table = self.look_for_elements(By.CSS_SELECTOR, "tbody tr")
        if field_to_filter_by == "name":
            text_to_filter_by = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
            input_field = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_name"])
        elif field_to_filter_by == "model":
            text_to_filter_by = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(4)").text
            input_field = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_model"])
        else:
            raise ValueError("Incorrect filter field. Must be 'name' or 'model'")

        input_field.clear()
        input_field.send_keys(text_to_filter_by)
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["filter_btn"]).click()
        return text_to_filter_by

    def remove_filtration(self, field_to_filter_by):
        if field_to_filter_by == "name":
            input_field = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_name"])
        elif field_to_filter_by == "model":
            input_field = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_model"])
        else:
            raise ValueError("Incorrect filter field. Must be 'name' or 'model'")

        input_field.clear()
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["filter_btn"]).click()

    def upload_image(self):
        path_to_images = "G:\\Study\\OTUS\\Git\\OTUS_Selenium_Start\\helpers\\images"
        print(path_to_images + "\\pic_1.png")
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty()
        edit_btn = self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["edit_btn"])
        edit_btn.click()
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["tab_image_in_edit"]).click()
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["image_in_edit"]).click()
        self.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_FOR_PRODUCTS["btn_to_add_image"]).click()
        script = "arguments[0].style.opacity=1;" \
                 "arguments[0].style['transform']='translate(0px, 0px) scale(1)';" \
                 "arguments[0].style['MozTransform']='translate(0px, 0px) scale(1)';" \
                 "arguments[0].style['WebkitTransform']='translate(0px, 0px) scale(1)';" \
                 "arguments[0].style['msTransform']='translate(0px, 0px) scale(1)';" \
                 "arguments[0].style['OTransform']='translate(0px, 0px) scale(1)';" \
                 "return true;"
        # el = self.driver.find_elements_by_css_selector(".note-image-input.form-control")[0],[1] - не падает
        # el = self.driver.find_element_by_css_selector("#form-upload input[type='file']")
        # self.driver.execute_script(script, el)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", self.driver.find_element_by_xpath("//input[@type='file']"), "0")
        self.driver.execute_script("arguments[0].setAttribute('class', arguments[1])", self.driver.find_element_by_xpath("//input[@type='file']/../../div[2]"), "a")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path_to_images + "\\pic_1.png")
        # btn_to_upload_img = self.driver.find_element_by_css_selector('#form-upload input[name=\'file[]\']')
        # el.send_keys(path_to_images + "\\pic_1.png")
        # print(path_to_images + "\\pic_1.png")
        sleep(5)
