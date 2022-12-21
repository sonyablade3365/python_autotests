"""
Hawaii 2022
"""
from selenium.webdriver.common.by import By

def test_smoke(browser):
    """
    SMK-1. Smoke-test
    """
    
    browser.get("https://postcard.qa.studio/")

    button = browser.find_element(By.ID, value="send")
    
    assert button.text == "Отправить", "Unexpected text on button"


