import pytest
import random
from admin_helper import SELECTORS_FOR_PRODUCTS, SELECTORS_GENERAL, SELECTORS_LEFT_NAV_MENU, USERNAME, PASSWORD
from selenium.webdriver.common.by import By


class TestAuthorization:

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_login(self, initial_search, urls, precondition, locator):
        precondition.login(urls["admin_login_page_url"])
        assert initial_search.look_for_element(locator, SELECTORS_GENERAL["user_menu_selector"]).text == "John Doe"
        assert initial_search.look_for_element(locator, SELECTORS_GENERAL["logout_btn_selector"])

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_go_to_products(self, initial_search, urls, precondition, locator):
        if not initial_search.look_for_element(locator, SELECTORS_GENERAL["logout_btn_selector"]):
            precondition.login(url=urls["admin_login_page_url"])
        precondition.admin_navigate_to_products()
        assert initial_search.look_for_element(locator, SELECTORS_FOR_PRODUCTS["table_of_products_title"]).text == "Product List"
        assert initial_search.look_for_element(locator, SELECTORS_FOR_PRODUCTS["table_of_products"])

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_edit_product(self, initial_search, browser_in_use, urls, precondition, locator):
        text_fields_to_be_changed = {
            "prod_name_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "model_in_edit": "Test_prod_model_in_edit_",
            "price_in_edit": "1000.00",
            "quantity_in_edit": "100"
        }
        price_to_compare = "$" + "{:,.2f}".format(float(text_fields_to_be_changed["price_in_edit"]))

        if browser_in_use.title != "Products":
            precondition.login(url=urls["admin_login_page_url"])
            precondition.admin_navigate_to_products()

        rows_of_products_table = initial_search.look_for_element(locator, "tbody tr")

        if rows_of_products_table.text == "No results!":
            precondition.create_product()

        edit_btn = initial_search.look_for_element(locator, SELECTORS_FOR_PRODUCTS["edit_btn"])
        edit_btn.click()

        for key in text_fields_to_be_changed:
            browser_in_use.execute_script(f"$(\"{SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_changed.get(key)}\";")

        save_btn = initial_search.look_for_element(locator, SELECTORS_FOR_PRODUCTS["save_btn"])
        save_btn.click()

        rows_of_products_table = initial_search.look_for_elements(locator, "tbody tr")

        for row in rows_of_products_table:
            if text_fields_to_be_changed["prod_name_in_edit"] == row.find_element_by_css_selector("td:nth-child(3)").text:
                assert row.find_element_by_css_selector("td:nth-child(4)").text == text_fields_to_be_changed["model_in_edit"]
                assert row.find_element_by_css_selector("td:nth-child(5)").text == price_to_compare
                assert row.find_element_by_css_selector("td:nth-child(6)").text == text_fields_to_be_changed["quantity_in_edit"]
                return

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_delete_product(self, initial_search, browser_in_use, urls, precondition, locator):
        if browser_in_use.title != "Products":
            precondition.login(url=urls["admin_login_page_url"])
            precondition.admin_navigate_to_products()

        rows_of_products_table = initial_search.look_for_element(locator, "tbody tr")

        if rows_of_products_table.text == "No results!":
            precondition.create_product()

        rows_of_products_table = initial_search.look_for_elements(locator, "tbody tr")
        name_of_deleted_product = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text
        select_product_chck_box = rows_of_products_table[0].find_element_by_css_selector("td:nth-child(1)")
        select_product_chck_box.click()

        del_btn = initial_search.look_for_element(locator, SELECTORS_FOR_PRODUCTS["delete_product_btn"])
        del_btn.click()

        initial_search.alert_accept()

        rows_of_products_table = initial_search.look_for_elements(locator, "tbody tr")
        for row in rows_of_products_table:
            assert name_of_deleted_product not in row.text

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_add_product(self, initial_search, browser_in_use, urls, precondition, locator):
        if browser_in_use.title != "Products":
            precondition.login(url=urls["admin_login_page_url"])
            precondition.admin_navigate_to_products()

        text_fields_to_be_changed = {
            "prod_name_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "meta_tag_in_edit": "Test_prod_name_in_edit_" + str(random.randint(1, 10000)),
            "model_in_edit": "Test_prod_model_in_edit_" + str(random.randint(1, 10000)),
            "price_in_edit": "1000.00",
            "quantity_in_edit": "100"
        }
        price_to_compare = "$" + "{:,.2f}".format(float(text_fields_to_be_changed["price_in_edit"]))

        add_product_btn = initial_search.look_for_element(By.CSS_SELECTOR, SELECTORS_FOR_PRODUCTS["add_product_btn"])
        add_product_btn.click()

        for key in text_fields_to_be_changed:
            browser_in_use.execute_script(
                f"$(\"{SELECTORS_FOR_PRODUCTS[key]}\")[0].value = \"{text_fields_to_be_changed.get(key)}\";")

        save_btn = initial_search.look_for_element(By.CSS_SELECTOR, SELECTORS_FOR_PRODUCTS["save_btn"])
        save_btn.click()

        rows_of_products_table = initial_search.look_for_elements(locator, "tbody tr")

        for row in rows_of_products_table:
            if text_fields_to_be_changed["prod_name_in_edit"] == row.find_element_by_css_selector(
                    "td:nth-child(3)").text:
                assert row.find_element_by_css_selector("td:nth-child(4)").text == text_fields_to_be_changed["model_in_edit"]
                assert row.find_element_by_css_selector("td:nth-child(5)").text == price_to_compare
                assert row.find_element_by_css_selector("td:nth-child(6)").text == text_fields_to_be_changed["quantity_in_edit"]
                return

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_logout(self, initial_search, precondition, locator):
        logout_btn = initial_search.look_for_element(locator, SELECTORS_GENERAL["logout_btn_selector"])
        logout_btn.click()
        assert initial_search.look_for_element(locator, SELECTORS_GENERAL["login_form_selector"])
        assert initial_search.look_for_element(locator, SELECTORS_GENERAL["login_selector"])
