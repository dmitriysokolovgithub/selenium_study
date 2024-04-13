import pytest
from selenium.webdriver.common.by import By
import time


def test_shopping_cart_existence(browser):
    url = r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(5)
    button_element = browser.find_element(By.XPATH, r"//button[contains(@class,'btn-add-to-basket')]")
    assert True
