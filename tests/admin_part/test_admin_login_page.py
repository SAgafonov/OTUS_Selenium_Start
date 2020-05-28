import pytest
from admin_helper import CSS_SELECTORS_GENERAL
from selenium.webdriver.common.by import By


class TestAdminLoginPage:

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar-brand")])
    def test_check_main_logo_presence(self, admin_login_page, locator, selector):
        admin_login_page.open_page()
        assert admin_login_page.look_for_element(locator, selector)

    def test_check_main_logo_attrs(self, admin_login_page):
        assert admin_login_page.look_for_element(By.CSS_SELECTOR,
                                                 CSS_SELECTORS_GENERAL["main_logo"],
                                                 attribute="src") == "http://localhost/admin/view/image/logo.png"
        assert admin_login_page.look_for_element(By.CSS_SELECTOR,
                                                 CSS_SELECTORS_GENERAL["main_logo"],
                                                 attribute="title") == "OpenCart"

    def test_login_form(self, admin_login_page):
        assert admin_login_page.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["login_form_selector"])

    def test_username_field(self, admin_login_page):
        assert admin_login_page.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["login_selector"])

    def test_password_field(self, admin_login_page):
        assert admin_login_page.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["password_selector"])

    def test_login_btn(self, admin_login_page):
        assert admin_login_page.look_for_element(By.CSS_SELECTOR, CSS_SELECTORS_GENERAL["login_btn_selector"])
        assert admin_login_page.look_for_element(By.CSS_SELECTOR,
                                                 CSS_SELECTORS_GENERAL["login_btn_selector"]).text == "Login"

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_btn(self, admin_login_page, locator, selector):
        assert admin_login_page.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_btn_attribute(self, admin_login_page, locator, selector):
        assert admin_login_page.look_for_element(locator,
                                                 selector,
                                                 attribute="href") == "https://localhost/admin/index.php?route=common/forgotten"
