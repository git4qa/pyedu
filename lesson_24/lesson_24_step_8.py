from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text

    answ_elem = browser.find_element_by_id("answer")
    answ_elem.send_keys(calc(x))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
