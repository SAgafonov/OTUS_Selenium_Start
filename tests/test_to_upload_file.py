import pytest
from selenium import webdriver


@pytest.fixture()
def chrome_browser(request):
    options = webdriver.ChromeOptions()

    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_download(chrome_browser):
    path_to_file = "G:\\Study\\OTUS\\Git\\OTUS_Selenium_Start\\helpers\\images\\pic_1.png"
    url = 'https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file'
    chrome_browser.get(url)
    script = """
    document.querySelector("form[method='post'] div input").setAttribute("style", "opacity: 1")
    """
    chrome_browser.switch_to.frame(chrome_browser.find_element_by_id("frame_Examples"))
    chrome_browser.execute_script(script)
    elem = chrome_browser.find_element_by_id("image_uploads")
    elem.send_keys(path_to_file)
    chrome_browser.switch_to.default_content()
