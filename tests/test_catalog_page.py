
class TestCatalogPage:

    def test_check_main_logo(self, urls, browser_in_use):
        browser_in_use.get(urls["catalog_url"])
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
        browser_in_use.get(urls["catalog_url"])
        assert browser_in_use.find_element_by_css_selector("button[class='btn btn-inverse btn-block "
                                                           "btn-lg dropdown-toggle']")

    def test_navigation_bar(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_class_name("navbar")
        assert browser_in_use.find_element_by_xpath("//nav[@class='navbar']/"
                                                    "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                    "ul[@class='nav navbar-nav']")

    def test_left_list_group(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("#column-left .list-group")

    def test_product_cards_exist(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_xpath("//div[@class='product-thumb']")
        assert len(browser_in_use.find_elements_by_xpath("//div[@class='product-thumb']")) == 12

    def test_add_to_wish_list_btns(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("[data-original-title='Add to Wish List']")
        assert len(browser_in_use.find_elements_by_css_selector("[data-original-title='Add to Wish List']")) == 12

    def test_price_label(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_class_name("price")
        assert len(browser_in_use.find_elements_by_class_name("price")) == 12

    def test_compare_btns(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("[data-original-title='Compare this Product']")
        assert len(browser_in_use.find_elements_by_css_selector("[data-original-title='Compare this Product']")) == 12

    def test_add_to_cart_btns(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("div[class='button-group'] "
                                                            "span[class='hidden-xs hidden-sm hidden-md']")
        assert len(browser_in_use.find_elements_by_css_selector("div[class='button-group'] "
                                                                "span[class='hidden-xs hidden-sm hidden-md']")) == 12

    def test_main_picture(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_class_name("image")
        assert len(browser_in_use.find_elements_by_class_name("image")) == 12
