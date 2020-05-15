import pytest
from selenium.webdriver.common.by import By


class TestArticleCard:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#logo h1 a")])
    def test_check_main_logo(self, initial_search, urls, locator, selector):
        initial_search.open_page(urls["article_card_url"])
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
        initial_search.open_page(urls["article_card_url"])
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar"),
                                                   (By.XPATH, "//nav[@class='navbar']/"
                                                              "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                              "ul[@class='nav navbar-nav']")])
    def test_navigation_bar(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_check_add_to_wish_list_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_check_compare_this_product_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".col-sm-4 ul")])
    def test_description_label(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)[0]

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".col-sm-4 ul")])
    def test_price_label(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)[1]

    @pytest.mark.parametrize("locator, selector", [(By.ID, "input-quantity")])
    def test_qty_text_field(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.ID, "button-cart")])
    def test_add_to_cart_btn(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "thumbnails")])
    def test_thumbnail_exists(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, ".thumbnails li")])
    def test_thumbnails_len(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 7
