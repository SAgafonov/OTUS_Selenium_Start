import pytest
from selenium.webdriver.common.by import By


class TestAuthorization:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR,
                                                    {"login_selector": "[name='username']",
                                                     "password_selector": "[name='password']",
                                                     "user_menu_selector": ".dropdown > .dropdown-toggle",
                                                     "logout_btn_selector": "ul.nav.navbar-nav.navbar-right > li:nth-child(2)"})])
    def test_login(self, initial_search, urls, creds_for_admin, to_perform_action, locator, selector):
        username, password = creds_for_admin
        initial_search.open_page(urls["admin_login_page_url"])
        login_input = initial_search.look_for_element(locator, selector["login_selector"])
        password_input = initial_search.look_for_element(locator, selector["password_selector"])
        login_input.send_keys(username)
        password_input.send_keys(password)
        password_input.submit()
        assert initial_search.look_for_element(locator, selector["user_menu_selector"]).text == "John Doe"
        assert initial_search.look_for_element(locator, selector["logout_btn_selector"])

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR,
                                                    {"catalog_element": "#menu > #menu-catalog",
                                                     "product_element": "li#menu-catalog > ul#collapse1 li:nth-child(2)",
                                                     "table_of_products_title": "div.col-md-9.col-md-pull-3.col-sm-12 h3",
                                                     "table_of_products": "div.col-md-9.col-md-pull-3.col-sm-12 div.table-responsive table"})])
    def test_go_to_products(self, initial_search, to_perform_action, locator, selector):
        path_to_product = initial_search.look_for_element(locator, selector["catalog_element"])
        path_to_product.click()
        path_to_product = initial_search.look_for_element(locator, selector["product_element"])
        path_to_product.click()
        assert initial_search.look_for_element(locator, selector["table_of_products_title"]).text == "Product List"
        assert initial_search.look_for_element(locator, selector["table_of_products"])

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR,
                                                    {"logout_btn_selector": "ul.nav.navbar-nav.navbar-right > li:nth-child(2)",
                                                     "login_form_selector": "div.panel-body form",
                                                     "username_field_selector": "[name='username']"})])
    def test_logout(self, initial_search, to_perform_action, locator, selector):
        logout_btn = initial_search.look_for_element(locator, selector["logout_btn_selector"])
        logout_btn.click()
        assert initial_search.look_for_element(locator, selector["login_form_selector"])
        assert initial_search.look_for_element(locator, selector["username_field_selector"])
