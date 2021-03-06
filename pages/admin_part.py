import allure
import logging
import random
from helpers.db_connector import DBConnector
from helpers.admin_helper import CSS_SELECTORS_FOR_PRODUCTS, CSS_SELECTORS_GENERAL, CSS_SELECTORS_LEFT_NAV_MENU, \
    USERNAME, PASSWORD, ADMIN_SUB_URL
from .base import BasePage

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class AdminLoginPage(BasePage):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url + ADMIN_SUB_URL
        super().__init__(driver=driver, url=self.url)
        self.db = DBConnector()
        logger.debug("AdminLoginPage class is initialized")

    @allure.step("Enter username")
    def _set_username_(self):
        # To test logging console output
        self.driver.execute_script("console.log('TEEEEEEEEEEEEEEEEEEEEEEEEEEEEST')")

        logger.debug("Look for username field using '{}' selector".format(CSS_SELECTORS_GENERAL["login_selector"]))
        login_input = self.look_for_element(selector=CSS_SELECTORS_GENERAL["login_selector"])
        logger.debug("Username field is found")
        logger.info("Clear username field")
        login_input.clear()
        logger.info("Enter username")
        login_input.send_keys(USERNAME)

    @allure.step("Enter password")
    def _set_password_(self):
        logger.debug("Look for password field '{}' selector".format(CSS_SELECTORS_GENERAL["password_selector"]))
        password_input = self.look_for_element(selector=CSS_SELECTORS_GENERAL["password_selector"])
        logger.debug("Password field is found")
        logger.info("Clear password field")
        password_input.clear()
        logger.info("Enter password")
        password_input.send_keys(PASSWORD)

    @allure.step("Log in admin panel")
    def login(self):
        logger.info("Open login page")
        self.open_page()
        logger.debug("Call method to enter username")
        self._set_username_()
        logger.debug("Call method to enter password")
        self._set_password_()
        logger.info("Press button to authorize")
        self.look_for_element(selector=CSS_SELECTORS_GENERAL["login_btn_selector"]).click()

    @allure.step("Log out from admin panel")
    def logout(self):
        logger.info("Click 'Log out' button")
        self.look_for_element(selector=CSS_SELECTORS_GENERAL["logout_btn_selector"]).click()


class AdminProductPage(AdminLoginPage):

    def check_if_authorized(self):
        logger.debug("Check if in authorized zone")
        if not self.look_for_element(selector=CSS_SELECTORS_GENERAL["logout_btn_selector"]):
            logger.info("User is not authorized")
            logger.info("Authorize")
            self.login()

    def check_if_table_with_products_is_not_empty(self, num_of_companies_to_create=1):
        logger.debug("Check if 'Product' table is not empty")
        rows_of_products_table = self.look_for_element(selector="tbody tr")
        if rows_of_products_table.text == "No results!":
            logger.info("'Product table is empty'")
            logger.info("Create {} product(-s)".format(num_of_companies_to_create))
            for i in range(num_of_companies_to_create):
                self.create_product()

    @allure.step("Go to 'Products' page")
    def admin_navigate_to_products(self):
        logger.debug("Check if in authorized zone")
        self.check_if_authorized()
        logger.debug("Look for 'Catalog' item using '{}' selector".format(CSS_SELECTORS_LEFT_NAV_MENU["catalog_element"]))
        path_to_product = self.look_for_element(selector=CSS_SELECTORS_LEFT_NAV_MENU["catalog_element"])
        logger.debug("'Catalog' item is found")
        path_to_product.click()
        logger.debug("Look for 'Product' item using '{}' selector".format(CSS_SELECTORS_LEFT_NAV_MENU["product_element"]))
        path_to_product = self.look_for_element(selector=CSS_SELECTORS_LEFT_NAV_MENU["product_element"])
        logger.debug("'Product' item is found")
        logger.info("Go to 'Products' page")
        path_to_product.click()

    @allure.step("Create a product")
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
        logger.debug("Look for 'Add product' button using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["add_product_btn"]))
        add_product_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["add_product_btn"])
        logger.debug("'Add product' button is found")
        logger.info("Click 'Add product' button")
        add_product_btn.click()
        logger.info("Fill in fields using JS")
        with allure.step("Key in values to required fields"):
            for key in text_fields_to_be_created:
                self.driver.execute_script(
                    f"$(\"{CSS_SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_created.get(key)}\";")

        logger.debug("Look for 'Save' button using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["save_btn"]))
        save_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["save_btn"])
        logger.debug("'Save' button is found")
        logger.info("Click 'Save' button")
        with allure.step("Save a product"):
            save_btn.click()
        return text_fields_to_be_created

    @allure.step("Edit a product")
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
        logger.debug("Get name of a first product")
        first_prod_name = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["prod_name"]).text
        logger.debug("Get ID of the product that will be edited")
        edited_prod_id = self.db.select_method("SELECT product_id FROM oc_product_description "
                                               "WHERE name='{name}';".format(name=first_prod_name))[0][0]
        logger.debug("Look for 'Edit product' button using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["edit_btn"]))
        edit_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["edit_btn"])
        logger.debug("'Edit product' button is found")
        logger.info("Click 'Edit product' button")
        edit_btn.click()

        logger.info("Fill in fields using JS")
        with allure.step("Key in values to required fields"):
            for key in text_fields_to_be_changed:
                self.driver.execute_script(
                    f"$(\"{CSS_SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_changed.get(key)}\";")

        logger.debug("Look for 'Save' button using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["save_btn"]))
        save_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["save_btn"])
        logger.debug("'Save' button is found")
        logger.info("Click 'Save' button")
        with allure.step("Save a changes"):
            save_btn.click()
        return text_fields_to_be_changed, edited_prod_id

    @allure.step("Delete a product")
    def delete_product(self, name: str = None) -> tuple:
        """
        Delete either first product or product which name is passed as an argument
        :param name: string: name of a product which should be deleted
        :return: tuple: name of a deleted product and ID of a deleted product
        """
        deleted_prod_id = None
        select_product_chck_box = None
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        self.driver.refresh()
        rows_of_products_table = self.look_for_elements(selector="tbody tr")
        if not name:
            logger.debug("Name of product to be deleted is NOT provided")
            logger.debug("Select first product to be deleted")
            name_of_deleted_product = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
            logger.debug("Get ID of the product that will be deleted")
            deleted_prod_id = self.db.select_method("SELECT product_id FROM oc_product_description "
                                                   "WHERE name='{name}';".format(name=name_of_deleted_product))[0][0]
            select_product_chck_box = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(1)")
        else:
            logger.debug("Name of product to be deleted is provided")
            logger.debug("Select the provided product to be deleted")
            name_of_deleted_product = name
            for row in rows_of_products_table:
                logger.debug("Look for a product")
                if name_of_deleted_product == row.find_element_by_css_selector(
                        "td:nth-child(3)").text:
                    logger.debug("Product '{}' is found".format(name_of_deleted_product))
                    logger.debug("Get ID of the product that will be deleted")
                    deleted_prod_id = self.db.select_method("SELECT product_id FROM oc_product_description "
                                                            "WHERE name='{name}';".format(name=name_of_deleted_product))[0][0]
                    select_product_chck_box = row.find_element_by_css_selector("td:nth-child(1)")
                    logger.debug("{}", select_product_chck_box)
                else:
                    logger.debug("Product '{}' is NOT found".format(name_of_deleted_product))

        logger.info("Select a check-box for the '{}' product".format(name_of_deleted_product))
        with allure.step("Select a product to be deleted"):
            select_product_chck_box.click()
        logger.debug("Look for 'Delete' button using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["delete_product_btn"]))
        del_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["delete_product_btn"])
        logger.debug("'Delete' button is found")
        logger.info("Click 'Delete' button")
        with allure.step("Delete a product"):
            del_btn.click()
        self.alert_accept()
        return name_of_deleted_product, deleted_prod_id

    @allure.step("Delete all products")
    def delete_all_products(self):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        logger.info("Select all products")
        with allure.step("Select all products"):
            self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["checkbox_select_all"]).click()
        logger.info("Click 'Delete' button")
        with allure.step("Delete all products"):
            self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["delete_product_btn"]).click()
        logger.info("Accept alert")
        self.alert_accept()

    @allure.step("Copy a product")
    def copy_product(self):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        logger.debug("Get rows from products table")
        rows_of_products_table = self.look_for_elements(selector="tbody tr")
        logger.debug("Get name of a company to be copied")
        name_of_copied_product = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
        logger.debug("Select a product to be copied")
        select_product_chck_box = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(1)")
        with allure.step("Select a product to copy"):
            select_product_chck_box.click()
        logger.debug("Look for 'Copy' button using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["copy_product_btn"]))
        copy_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["copy_product_btn"])
        logger.debug("'Copy' button is found")
        logger.info("Click 'Copy' button")
        with allure.step("Copy a product"):
            copy_btn.click()
        return name_of_copied_product

    @allure.step("Filter products")
    def filter_product(self, field_to_filter_by):
        if self.driver.title != "Products":
            self.check_if_authorized()
            self.admin_navigate_to_products()

        self.check_if_table_with_products_is_not_empty(num_of_companies_to_create=3)
        logger.debug("Get rows from products table")
        rows_of_products_table = self.look_for_elements(selector="tbody tr")
        if field_to_filter_by == "name":
            logger.debug("Get name of a product to filter by")
            text_to_filter_by = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
            logger.debug("Get input field to filter using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_name"]))
            input_field = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_name"])
        elif field_to_filter_by == "model":
            logger.debug("Get model of a product to filter by")
            text_to_filter_by = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(4)").text
            logger.debug("Get input field to filter using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_model"]))
            input_field = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_model"])
        else:
            logger.error("Incorrect field is provided - '{}'".format(field_to_filter_by))
            raise ValueError("Incorrect filter field. Must be 'name' or 'model'")

        logger.info("Clear filter field")
        with allure.step("Clear input field"):
            input_field.clear()
        logger.info("Fill in filter field")
        with allure.step("Enter text to filter by"):
            input_field.send_keys(text_to_filter_by)
        logger.info("Click 'Filter' button")
        with allure.step("Filtering"):
            self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["filter_btn"]).click()
        return text_to_filter_by

    @allure.step("Set default state of filtration")
    def remove_filtration(self, field_to_filter_by):
        if field_to_filter_by == "name":
            logger.debug("Get input field to filter using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_name"]))
            input_field = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_name"])
        elif field_to_filter_by == "model":
            logger.debug("Get input field to filter using '{}' selector".format(CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_model"]))
            input_field = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["filter_input_product_model"])
        else:
            logger.error("Incorrect field is provided - '{}'".format(field_to_filter_by))
            raise ValueError("Incorrect filter field. Must be 'name' or 'model'")

        logger.info("Clear filter field")
        input_field.clear()
        logger.info("Click 'Filter' button")
        self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["filter_btn"]).click()

    # def upload_image(self):
    #     path_to_images = "G:\\Study\\OTUS\\Git\\OTUS_Selenium_Start\\helpers\\images"
    #     print(path_to_images + "\\pic_1.png")
    #     if self.driver.title != "Products":
    #         self.check_if_authorized()
    #         self.admin_navigate_to_products()
    #
    #     self.check_if_table_with_products_is_not_empty()
    #     edit_btn = self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["edit_btn"])
    #     edit_btn.click()
    #     self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["tab_image_in_edit"]).click()
    #     self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["image_in_edit"]).click()
    #     self.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["btn_to_add_image"]).click()
    #     script = "arguments[0].style.opacity=1;" \
    #              "arguments[0].style['transform']='translate(0px, 0px) scale(1)';" \
    #              "arguments[0].style['MozTransform']='translate(0px, 0px) scale(1)';" \
    #              "arguments[0].style['WebkitTransform']='translate(0px, 0px) scale(1)';" \
    #              "arguments[0].style['msTransform']='translate(0px, 0px) scale(1)';" \
    #              "arguments[0].style['OTransform']='translate(0px, 0px) scale(1)';" \
    #              "return true;"
    #     # el = self.driver.find_elements_by_css_selector(".note-image-input.form-control")[0],[1] - не падает
    #     # el = self.driver.find_element_by_css_selector("#form-upload input[type='file']")
    #     # self.driver.execute_script(script, el)
    #     self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", self.driver.find_element_by_xpath("//input[@type='file']"), "0")
    #     self.driver.execute_script("arguments[0].setAttribute('class', arguments[1])", self.driver.find_element_by_xpath("//input[@type='file']/../../div[2]"), "a")
    #     self.driver.find_element_by_xpath("//input[@type='file']").send_keys(path_to_images + "\\pic_1.png")
    #     # btn_to_upload_img = self.driver.find_element_by_css_selector('#form-upload input[name=\'file[]\']')
    #     # el.send_keys(path_to_images + "\\pic_1.png")
    #     # print(path_to_images + "\\pic_1.png")
    #     sleep(5)
