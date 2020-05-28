import pytest
from selenium.webdriver.common.by import By


class TestCatalogPage:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#logo h1 a")])
    def test_check_main_logo(self, client_not_authorized_zone, urls, locator, selector):
        client_not_authorized_zone.open_page(urls["catalog_url"])
        assert client_not_authorized_zone.look_for_element(locator, selector)
        assert client_not_authorized_zone.look_for_element(locator, selector).text == "Your Store"

    @pytest.mark.parametrize("locator, selector", [(By.NAME, "search")])
    def test_search_field(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator, selector)
        assert client_not_authorized_zone.look_for_element(locator,
                                                           selector,
                                                           attribute="placeholder") == "Search"

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@id='search']/span/button")])
    def test_search_btn(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator, selector)
        client_not_authorized_zone.look_for_element(locator, selector).click()
        assert client_not_authorized_zone.look_for_element(locator=By.CSS_SELECTOR,
                                                           selector="div#content h1").text == "Search"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "button[class='btn btn-inverse btn-block "
                                                                     "btn-lg dropdown-toggle']")])
    def test_cart_btn(self, client_not_authorized_zone, urls, locator, selector):
        client_not_authorized_zone.open_page(urls["catalog_url"])
        assert client_not_authorized_zone.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar"),
                                                   (By.XPATH, "//nav[@class='navbar']/"
                                                              "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                              "ul[@class='nav navbar-nav']")])
    def test_navigation_bar(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "#column-left .list-group")])
    def test_left_list_group(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@class='product-thumb']")])
    def test_product_cards_exist(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@class='product-thumb']")])
    def test_product_cards_quantity(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_add_to_wish_list_btns(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_add_to_wish_list_btns_quantity(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "price")])
    def test_price_label(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "price")])
    def test_price_lables_quantity(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_compare_btns(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_compare_btns_quantity(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div[class='button-group'] "
                                                                     "i[class='fa fa-shopping-cart']")])
    def test_add_to_cart_btns(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div[class='button-group'] "
                                                                     "i[class='fa fa-shopping-cart']")])
    def test_add_to_cart_btns_quantity(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "image")])
    def test_main_picture(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "image")])
    def test_main_pictures_quantity(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator, selector)) == 12

    # ===> так ищет class='hidden-xs hidden-sm hidden-md' <===
    #
    # def test_add_to_cart_btnstu(self, urls, browser_in_use):
    #     assert browser_in_use.find_elements_by_css_selector("div[class='button-group'] "
    #                                                         "span[class='hidden-xs hidden-sm hidden-md']")
    # ===> а если делать как в строчках 77 - 83, то не находит. почему? <===
