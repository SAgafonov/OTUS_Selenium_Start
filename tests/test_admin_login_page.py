
class TestAdminLoginPage:

    def test_check_main_logo(self, urls, browser_in_use):
        browser_in_use.get(urls["admin_login_page_url"])
        assert browser_in_use.find_element_by_class_name("navbar-brand")
        assert browser_in_use.find_element_by_css_selector(".navbar-brand img").get_attribute("src") == "http://localhost/admin/view/image/logo.png"
        assert browser_in_use.find_element_by_css_selector(".navbar-brand img").get_attribute("title") == "OpenCart"

    def test_login_form(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("div.panel-heading h1.panel-title")
        assert browser_in_use.find_element_by_css_selector("div.panel-heading h1.panel-title").text == "Please enter your login details."
        assert browser_in_use.find_element_by_css_selector("div.panel-body form")

    def test_username_field(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("[name='username']")

    def test_password_field(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("[name='password']")

    def test_login_btn(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_css_selector("button[class='btn btn-primary']")
        assert browser_in_use.find_element_by_css_selector("button[class='btn btn-primary']").text == "Login"

    def test_forgot_password_btn(self, urls, browser_in_use):
        assert browser_in_use.find_element_by_link_text("Forgotten Password")
        assert browser_in_use.find_element_by_link_text("Forgotten Password").get_attribute(
            "href") == "https://localhost/admin/index.php?route=common/forgotten"
