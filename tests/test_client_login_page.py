
class TestClientLoginPage:

    def test_check_main_logo(self, urls, browser_in_use):
        browser_in_use.get(urls["client_login_page_url"])
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
        browser_in_use.get(urls["client_login_page_url"])
        assert browser_in_use.find_element_by_css_selector("button[class='btn btn-inverse btn-block "
                                                           "btn-lg dropdown-toggle']")

    def test_navigation_bar(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_class_name("navbar")
        assert browser_in_use.find_element_by_xpath("//nav[@class='navbar']/"
                                                    "div[@class='collapse navbar-collapse navbar-ex1-collapse']/"
                                                    "ul[@class='nav navbar-nav']")

    def test_new_customer_form(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector(".well")[0]
        assert browser_in_use.find_elements_by_css_selector(".well")[0].find_element_by_css_selector(
            "h2").text == "New Customer"

    def test_login_form(self, urls, browser_in_use):
        assert browser_in_use.find_elements_by_css_selector(".well")[1]
        assert browser_in_use.find_elements_by_css_selector(".well")[1].find_element_by_css_selector(
            "h2").text == "Returning Customer"

    def test_email_address_field(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("[name='email']")

    def test_password_field(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("[name='password']")

    def test_forgot_password_link(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_link_text("Forgotten Password")
        assert browser_in_use.find_element_by_link_text("Forgotten Password").get_attribute(
            "href") == "https://localhost/index.php?route=account/forgotten"

    def test_login_btn(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("input[class='btn btn-primary']")
