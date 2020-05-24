import pytest
import random
from admin_helper import SELECTORS_FOR_PRODUCTS, SELECTORS_GENERAL, SELECTORS_LEFT_NAV_MENU, USERNAME, PASSWORD
from selenium.webdriver.common.by import By


class TestAuthorization:

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_login(self, admin_login_page, locator):
        admin_login_page.login()
        assert admin_login_page.look_for_element(locator, SELECTORS_GENERAL["user_menu_selector"]).text == "John Doe"
        assert admin_login_page.look_for_element(locator, SELECTORS_GENERAL["logout_btn_selector"])

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_go_to_products(self, admin_product_page, locator):
        if not admin_product_page.look_for_element(locator, SELECTORS_GENERAL["logout_btn_selector"]):
            admin_product_page.login()
        admin_product_page.admin_navigate_to_products()
        assert admin_product_page.look_for_element(locator, SELECTORS_FOR_PRODUCTS["table_of_products_title"]).text == "Product List"
        assert admin_product_page.look_for_element(locator, SELECTORS_FOR_PRODUCTS["table_of_products"])

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_edit_product(self, admin_product_page, locator):
        changed_fields = admin_product_page.edit_product()
        price_to_compare = "$" + "{:,.2f}".format(float(changed_fields["price_in_edit"]))
        rows_of_products_table = admin_product_page.look_for_elements(locator, "tbody tr")

        for row in rows_of_products_table:
            if changed_fields["prod_name_in_edit"] == row.find_element_by_css_selector("td:nth-child(3)").text:
                assert row.find_element_by_css_selector("td:nth-child(4)").text == changed_fields["model_in_edit"]
                assert row.find_element_by_css_selector("td:nth-child(5)").text == price_to_compare
                assert row.find_element_by_css_selector("td:nth-child(6)").text == changed_fields["quantity_in_edit"]
                return

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_delete_product(self, admin_product_page, locator):
        name_of_deleted_product = admin_product_page.delete_product()
        rows_of_products_table = admin_product_page.look_for_elements(locator, "tbody tr")
        for row in rows_of_products_table:
            assert name_of_deleted_product not in row.text

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_add_product(self, admin_product_page, locator):
        created_fields = admin_product_page.create_product()
        price_to_compare = "$" + "{:,.2f}".format(float(created_fields["price_in_edit"]))
        rows_of_products_table = admin_product_page.look_for_elements(locator, "tbody tr")

        for row in rows_of_products_table:
            if created_fields["prod_name_in_edit"] == row.find_element_by_css_selector(
                    "td:nth-child(3)").text:
                assert row.find_element_by_css_selector("td:nth-child(4)").text == created_fields["model_in_edit"]
                assert row.find_element_by_css_selector("td:nth-child(5)").text == price_to_compare
                assert row.find_element_by_css_selector("td:nth-child(6)").text == created_fields["quantity_in_edit"]
                return

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_copy_product(self, admin_product_page, locator):
        name_of_copied_product = admin_product_page.copy_product()
        rows_of_products_table = admin_product_page.look_for_elements(locator, "tbody tr")
        temp = 0
        for row in rows_of_products_table:
            if row.find_element_by_css_selector("td:nth-child(3)").text == name_of_copied_product:
                temp += 1
        admin_product_page.delete_product(name_of_copied_product)
        assert temp == 2

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_filter_form_exists(self, admin_product_page, locator):
        assert admin_product_page.look_for_element(locator, SELECTORS_FOR_PRODUCTS["table_for_filtering"])

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_filter_by_name(self, admin_product_page, locator):
        filtered_name = admin_product_page.filter_product("name")
        rows_of_products_table = admin_product_page.look_for_elements(locator, "tbody tr")
        assert len(rows_of_products_table) == 1
        assert rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text == filtered_name
        admin_product_page.remove_filtration("name")

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_filter_by_model(self, admin_product_page, locator):
        filtered_name = admin_product_page.filter_product("model")
        rows_of_products_table = admin_product_page.look_for_elements(locator, "tbody tr")
        assert len(rows_of_products_table) == 1
        assert rows_of_products_table[0].find_element_by_css_selector("td:nth-child(4)").text == filtered_name
        admin_product_page.remove_filtration("model")

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_delete_all(self, admin_product_page, locator):
        admin_product_page.delete_all_products()
        assert admin_product_page.look_for_element(locator, "tbody tr").text == "No results!"

    @pytest.mark.parametrize("locator", [By.CSS_SELECTOR])
    def test_logout(self, admin_login_page, locator):
        admin_login_page.logout()
        assert admin_login_page.look_for_element(locator, SELECTORS_GENERAL["login_form_selector"])
        assert admin_login_page.look_for_element(locator, SELECTORS_GENERAL["login_selector"])
