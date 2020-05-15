import pytest
from selenium.webdriver.common.by import By


class TestAdminLoginPage:

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar-brand")])
    def test_check_main_logo_presence(self, initial_search, urls, locator, selector):
        initial_search.open_page(urls["admin_login_page_url"])
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".navbar-brand img")])
    def test_check_main_logo_attrs(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator,
                                               selector,
                                               attribute="src") == "http://localhost/admin/view/image/logo.png"
        assert initial_search.look_for_element(locator,
                                               selector,
                                               attribute="title") == "OpenCart"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div.panel-body form")])
    def test_login_form(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div.panel-heading h1.panel-title")])
    def test_login_form_name(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector).text == "Please enter your login details."

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[name='username']")])
    def test_username_field(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[name='password']")])
    def test_password_field(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "button[class='btn btn-primary']")])
    def test_login_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)
        assert initial_search.look_for_element(locator, selector).text == "Login"

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_btn_attribute(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator,
                                               selector,
                                               attribute="href") == "https://localhost/admin/index.php?route=common/forgotten"
