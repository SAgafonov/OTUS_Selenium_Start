import logging
import pytest
from helpers.admin_helper import CSS_SELECTORS_GENERAL
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
logger.setLevel('INFO')


class TestAdminLoginPage:

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar-brand")])
    def test_check_main_logo_presence(self, admin_login_page, locator, selector):
        logger.info("<======== Run checking main logo test ========>")
        admin_login_page.open_page()
        assert admin_login_page.look_for_element(locator=locator, selector=selector)
        logger.info("========> End checking main logo test <========\n")

    def test_check_main_logo_attribute(self, admin_login_page):
        logger.info("<======== Run checking main logo attribute test ========>")
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["main_logo"],
                                                 attribute="src") == "http://localhost/admin/view/image/logo.png"
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["main_logo"],
                                                 attribute="title") == "OpenCart"
        logger.info("========> End checking main logo attribute test <========\n")

    def test_login_form(self, admin_login_page):
        logger.info("<======== Run checking presence of login form test ========>")
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["login_form_selector"])
        logger.info("========> End checking presence of login form test <========\n")

    def test_username_field(self, admin_login_page):
        logger.info("<======== Run checking presence of username field test ========>")
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["login_selector"])
        logger.info("========> End checking presence of username form test <========\n")

    def test_password_field(self, admin_login_page):
        logger.info("<======== Run checking presence of password field test ========>")
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["password_selector"])
        logger.info("========> End checking presence of password field test <========\n")

    def test_login_btn(self, admin_login_page):
        logger.info("<======== Run checking presence of submit button test ========>")
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["login_btn_selector"])
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["login_btn_selector"]).text == "Login"
        logger.info("========> End checking presence of submit button test <========\n")

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_btn(self, admin_login_page, locator, selector):
        logger.info("<======== Run checking presence of forgot passwd button test ========>")
        assert admin_login_page.look_for_element(locator=locator, selector=selector)
        logger.info("========> End checking presence of forgot passwd button test <========\n")

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_btn_attribute(self, admin_login_page, locator, selector):
        logger.info("<======== Run checking forgot passwd button attribute test ========>")
        assert admin_login_page.look_for_element(locator=locator,
                                                 selector=selector,
                                                 attribute="href") == "https://localhost/admin/index.php?route=common/forgotten"
        logger.info("========> End checking forgot passwd button attribute test <========\n")
