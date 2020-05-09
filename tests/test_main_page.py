
class TestMainPage:

    def test_check_main_logo(self, urls, browser_in_use):
        browser_in_use.get(urls["main_page_url"])
        assert browser_in_use.find_element_by_css_selector("div#logo h1 a")
        assert browser_in_use.find_element_by_css_selector("div#logo h1 a").text == "Your Store"

    def test_search_field(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_name("search")
        assert browser_in_use.find_element_by_name("search").get_attribute("placeholder") == "Search"

    def test_search_btn(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_xpath("//div[@id='search']/span/button")
        browser_in_use.find_element_by_xpath("//div[@id='search']/span/button").click()
        assert browser_in_use.find_element_by_css_selector("div#content h1").text == "Search"

    def test_cart_btn(self, urls, browser_in_use):
        browser_in_use.get(urls["main_page_url"])
        assert browser_in_use.find_element_by_css_selector("button[class='btn btn-inverse btn-block "
                                                           "btn-lg dropdown-toggle']")

    def test_navigation_bar(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_class_name("navbar")
        assert browser_in_use.find_element_by_xpath("//nav[@class='navbar']/"
                                                    "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                    "ul[@class='nav navbar-nav']")

    def test_main_slider(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("div#slideshow0")

    def test_swiper_btns_prev(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("div.swiper-button-prev")
        assert len(browser_in_use.find_elements_by_css_selector("div.swiper-button-prev")) == 2

    def test_swiper_btns_next(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("div.swiper-button-next")
        assert len(browser_in_use.find_elements_by_css_selector("div.swiper-button-next")) == 2

    def test_featured_block_exists(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("div#content .row")

    def test_product_cards_exist(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_xpath("//div[@class='product-thumb transition']")
        assert len(browser_in_use.find_elements_by_xpath("//div[@class='product-thumb transition']")) == 4

    def test_add_to_wish_list_btns(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("[data-original-title='Add to Wish List']")
        assert len(browser_in_use.find_elements_by_css_selector("[data-original-title='Add to Wish List']")) == 4

    def test_price_label(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_class_name("price")
        assert len(browser_in_use.find_elements_by_class_name("price")) == 4

    def test_compare_btns(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("[data-original-title='Compare this Product']")
        assert len(browser_in_use.find_elements_by_css_selector("[data-original-title='Compare this Product']")) == 4

    def test_add_to_cart_btns(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("div[class='button-group'] "
                                                            "span[class='hidden-xs hidden-sm hidden-md']")
        assert len(browser_in_use.find_elements_by_css_selector("div[class='button-group'] "
                                                                "span[class='hidden-xs hidden-sm hidden-md']")) == 4

    def test_lower_slider(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_id("carousel0")
