
def test_opencart_page_is_opened(get_url, browser_in_use):
    browser_in_use.get(get_url)
    assert browser_in_use.title == "Your Store"
    assert browser_in_use.find_element_by_xpath("//a[@href='http://www.opencart.com']").text == "OpenCart"
