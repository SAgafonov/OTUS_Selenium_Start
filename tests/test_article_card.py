
class TestArticleCard:

    def test_check_main_logo(self, urls, browser_in_use):
        browser_in_use.get(urls["article_card_url"])

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
        browser_in_use.get(urls["article_card_url"])
        assert browser_in_use.find_element_by_css_selector("button[class='btn btn-inverse btn-block "
                                                           "btn-lg dropdown-toggle']")

    def test_navigation_bar(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_class_name("navbar")
        assert browser_in_use.find_element_by_xpath("//nav[@class='navbar']/"
                                                    "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                    "ul[@class='nav navbar-nav']")

    def test_check_add_to_wish_list_btn(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("[data-original-title='Add to Wish List']")

    def test_check_compare_this_product_btn(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector("[data-original-title='Compare this Product']")

    def test_description_label(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector(".col-sm-4 ul")[0]

    def test_price_label(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector(".col-sm-4 ul")[1]

    def test_qty_text_field(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_id("input-quantity")

    def test_add_to_cart_btn(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_id("button-cart")

    def test_thumbnails(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_class_name("thumbnails")
        assert len(browser_in_use.find_elements_by_css_selector(".thumbnails li")) == 7
