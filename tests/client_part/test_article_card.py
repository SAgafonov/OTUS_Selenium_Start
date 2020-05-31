import pytest
from selenium.webdriver.common.by import By


class TestArticleCard:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#logo h1 a")])
    def test_check_main_logo(self, client_not_authorized_zone, urls, locator, selector):
        client_not_authorized_zone.open_page()
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector).text == "Your Store"

    @pytest.mark.parametrize("locator, selector", [(By.NAME, "search")])
    def test_search_field(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator, selector)
        assert client_not_authorized_zone.look_for_element(locator,
                                                           selector,
                                                           attribute="placeholder") == "Search"

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@id='search']/span/button")])
    def test_search_btn(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)
        client_not_authorized_zone.look_for_element(locator=locator, selector=selector).click()
        assert client_not_authorized_zone.look_for_element(locator=By.CSS_SELECTOR, selector="div#content h1").text == "Search"

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "button[class='btn btn-inverse btn-block "
                                                                     "btn-lg dropdown-toggle']")])
    def test_cart_btn(self, client_not_authorized_zone, urls, locator, selector):
        client_not_authorized_zone.open_page(urls["article_card_url"])
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar"),
                                                   (By.XPATH, "//nav[@class='navbar']/"
                                                              "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                              "ul[@class='nav navbar-nav']")])
    def test_navigation_bar(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_check_add_to_wish_list_btn(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_check_compare_this_product_btn(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".col-sm-4 ul")])
    def test_description_label(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator=locator, selector=selector)[0]

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".col-sm-4 ul")])
    def test_price_label(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_elements(locator=locator, selector=selector)[1]

    @pytest.mark.parametrize("locator, selector", [(By.ID, "input-quantity")])
    def test_qty_text_field(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.ID, "button-cart")])
    def test_add_to_cart_btn(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "thumbnails")])
    def test_thumbnail_exists(self, client_not_authorized_zone, locator, selector):
        assert client_not_authorized_zone.look_for_element(locator=locator, selector=selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".thumbnails li")])
    def test_thumbnails_len(self, client_not_authorized_zone, locator, selector):
        assert len(client_not_authorized_zone.look_for_elements(locator=locator, selector=selector)) == 7
