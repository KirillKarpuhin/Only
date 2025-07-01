import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit() 

link = "https://only.digital/en"

def test_footer(browser):
    browser.get(link)
    # скроллим до футера
    footer = browser.find_element(By.TAG_NAME, "footer")
    browser.execute_script("arguments[0].scrollIntoView();", footer)
    # находим иконку соц.сетки
    social_links = browser.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[1]/a[1]")
    assert social_links.is_displayed()
    # доп. проверка на наличие копирайта
    copyright = browser.find_element(By.XPATH, "/html/body/main/footer/div[1]/p[2]")
    assert "©" in copyright.text