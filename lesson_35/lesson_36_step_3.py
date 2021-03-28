import time
import math
import pytest
from selenium import webdriver


urlparams = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('urlp', urlparams)
def test_check_answer(browser, urlp):
    link = f"https://stepik.org/lesson/{urlp}/step/1"
    browser.get(link)
    time.sleep(2)

    answer = math.log(int(time.time()))
    answelem = browser.find_element_by_css_selector("textarea.string-quiz__textarea")
    answelem.send_keys(str(answer))

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    time.sleep(2)

    check_message = browser.find_element_by_css_selector("pre.smart-hints__hint").text

    assert check_message == "Correct!", check_message


