import pytest
from selenium.webdriver.common.by import By


class TestClientLoginPage:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#logo h1 a")])
    def test_check_main_logo(self, initial_search, urls, locator, selector):
        initial_search.open_page(urls["client_login_page_url"])
        assert initial_search.look_for_element(locator, selector)
        assert initial_search.look_for_element(locator, selector).text == "Your Store"

    @pytest.mark.parametrize("locator, selector", [(By.NAME, "search")])
    def test_search_field(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)
        assert initial_search.look_for_element(locator,
                                               selector,
                                               attribute="placeholder") == "Search"

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@id='search']/span/button")])
    def test_search_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)
        initial_search.look_for_element(locator, selector).click()
        assert initial_search.look_for_element(locator=By.CSS_SELECTOR, selector="div#content h1").text == "Search"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "button[class='btn btn-inverse btn-block "
                                                                     "btn-lg dropdown-toggle']")])
    def test_cart_btn(self, initial_search, urls, locator, selector):
        initial_search.open_page(urls["client_login_page_url"])
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar"),
                                                   (By.XPATH, "//nav[@class='navbar']/"
                                                              "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                              "ul[@class='nav navbar-nav']")])
    def test_navigation_bar(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".well")])
    def test_new_customer_form(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)[0]
        assert initial_search.look_for_elements(locator, selector)[0].find_element_by_css_selector(
            "h2").text == "New Customer"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".well")])
    def test_login_form(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)[1]
        assert initial_search.look_for_elements(locator, selector)[1].find_element_by_css_selector(
            "h2").text == "Returning Customer"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[name='email']")])
    def test_email_address_field(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[name='password']")])
    def test_password_field(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.LINK_TEXT, "Forgotten Password")])
    def test_forgot_password_link(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)
        assert initial_search.look_for_element(locator, selector, attribute="href") == "https://localhost/index.php?route=account/forgotten"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "input[class='btn btn-primary']")])
    def test_login_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)
