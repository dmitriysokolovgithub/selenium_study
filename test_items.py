import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


def test_shopping_cart_existence(browser):
    url = r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    button_element = browser.find_element(By.XPATH, r"//button[contains(@class,'btn-add-to-basket')]")
    try:
        button_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, r"//button[contains(@class,'btn-add-to-basket')]")))
        button_search_result = True
    except NoSuchElementException:
        button_search_result = False
    assert button_search_result
