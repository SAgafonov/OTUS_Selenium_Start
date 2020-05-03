import pytest

@pytest.mark.parametrize("url, text", [("http://www.opencart.com", "OpenCart")])
def test_opencart_page_is_opened(get_url, browser_in_use, title_to_check, url, text):
    browser_in_use.get(get_url)
    assert browser_in_use.title == title_to_check
    assert browser_in_use.find_element_by_xpath(f"//a[@href='{url}']").text == text
