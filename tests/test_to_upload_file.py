
def test_download(browser_in_use):
    path_to_file = "G:\\Study\\OTUS\\Git\\OTUS_Selenium_Start\\helpers\\images\\pic_1.png"
    url = 'https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file'
    browser_in_use.get(url)
    script = """
    document.querySelector("form[method='post'] div input").setAttribute("style", "opacity: 1")
    """
    browser_in_use.switch_to.frame(browser_in_use.find_element_by_id("frame_Examples"))
    browser_in_use.execute_script(script)
    elem = browser_in_use.find_element_by_id("image_uploads")
    elem.send_keys(path_to_file)
    browser_in_use.switch_to.default_content()
