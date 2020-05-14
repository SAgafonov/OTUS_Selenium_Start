import pytest
from selenium.webdriver.common.by import By


class TestCatalogPage:

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div#logo h1 a")])
    def test_check_main_logo(self, initial_search, urls, locator, selector):
        initial_search.open_page(urls["catalog_url"])
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
        initial_search.open_page(urls["catalog_url"])
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "navbar"),
                                                   (By.XPATH, "//nav[@class='navbar']/"
                                                              "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                              "ul[@class='nav navbar-nav']")])
    def test_navigation_bar(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "#column-left .list-group")])
    def test_left_list_group(self, initial_search, locator, selector):
        assert initial_search.look_for_element(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@class='product-thumb']")])
    def test_product_cards_exist(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.XPATH, "//div[@class='product-thumb']")])
    def test_product_cards_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_add_to_wish_list_btns(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")])
    def test_add_to_wish_list_btns_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "price")])
    def test_price_label(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "price")])
    def test_price_lables_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_compare_btns(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "[data-original-title='Compare this Product']")])
    def test_compare_btns_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div[class='button-group'] "
                                                                     "i[class='fa fa-shopping-cart']")])
    def test_add_to_cart_btns(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CSS_SELECTOR, "div[class='button-group'] "
                                                                     "i[class='fa fa-shopping-cart']")])
    def test_add_to_cart_btns_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 12

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "image")])
    def test_main_picture(self, initial_search, locator, selector):
        assert initial_search.look_for_elements(locator, selector)

    @pytest.mark.parametrize("locator, selector", [(By.CLASS_NAME, "image")])
    def test_main_pictures_quantity(self, initial_search, locator, selector):
        assert len(initial_search.look_for_elements(locator, selector)) == 12

    # ===> так ищет class='hidden-xs hidden-sm hidden-md' <===
    #
    # def test_add_to_cart_btnstu(self, urls, browser_in_use):
    #     assert browser_in_use.find_elements_by_css_selector("div[class='button-group'] "
    #                                                         "span[class='hidden-xs hidden-sm hidden-md']")
    # ===> а если делать как в строчках 77 - 83, то не находит. почему? <===
