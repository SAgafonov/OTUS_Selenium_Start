import pytest
from selenium.webdriver.common.by import By


class TestMainPage:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#logo h1 a")])
    def test_check_main_logo(self, initial_search, urls, locator, selector):
        initial_search.open_page(urls["main_page_url"])
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
        initial_search.open_page(urls["main_page_url"])
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar"),
                                                   (By.XPATH, "//nav[@class='navbar']/"
                                                              "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                              "ul[@class='nav navbar-nav']")])
    def test_navigation_bar(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#slideshow0")])
    def test_main_slider(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR,
                                                    {"btn_selector": "div.swiper-button-prev",
                                                     "slider_selector": ".swiper-viewport > #slideshow0"}
                                                    )])
    def test_swiper_btn_prev_in_main_slider(self, initial_search, to_perform_action, locator, selector):
        el_to_hover = initial_search.look_for_element(locator, selector["slider_selector"])
        hover = to_perform_action.move_to_element(el_to_hover)
        hover.perform()
        assert initial_search.look_for_element(locator, selector["btn_selector"], timeout=5)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR,
                                                    {"btn_selector": "div.swiper-button-next",
                                                     "slider_selector": ".swiper-viewport > #slideshow0"}
                                                    )])
    def test_swiper_btns_next_in_main_slider(self, initial_search, to_perform_action, locator, selector):
        el_to_hover = initial_search.look_for_element(locator, selector["slider_selector"])
        hover = to_perform_action.move_to_element(el_to_hover)
        hover.perform()
        assert initial_search.look_for_element(locator, selector["btn_selector"], timeout=5)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#content .row")])
    def test_featured_block_exists(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@class='product-thumb transition']")])
    def test_product_cards_exist(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@class='product-thumb transition']")])
    def test_product_cards_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 4

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_add_to_wish_list_btns(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_add_to_wish_list_btns_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 4

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "price")])
    def test_price_label(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "price")])
    def test_price_lables_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 4

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_compare_btns(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_compare_btns_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 4

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div[class='button-group'] "
                                                                     "i[class='fa fa-shopping-cart']")])
    def test_add_to_cart_btns(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div[class='button-group'] "
                                                                     "i[class='fa fa-shopping-cart']")])
    def test_add_to_cart_btns_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 4

    @pytest.mark.parametrize("locator, selector", [(By.ID, "carousel0")])
    def test_lower_slider(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)
