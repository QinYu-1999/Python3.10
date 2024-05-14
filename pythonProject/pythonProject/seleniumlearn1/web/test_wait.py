import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_wait_unit():
    driver = webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study/locate')
    web1 = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn'))
    )
    print(web1)
    time.sleep(2)
    driver.quit()


def element_to_be_clickable(target_element, next_element):
    def _predicate(driver):
        driver.find_element(*target_element).click()
        return driver.find_element(*next_element)

    return _predicate


def test_by():
    #封装超时函数
    driver = webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study/iframe')
    web1 = WebDriverWait(driver, 10).until(
        element_to_be_clickable(
            (By.ID,'primary_btn'),
            (By.XPATH,"//*[text() = '该弹框点击两次后才会弹出']"))
    )
    time.sleep(4)
    driver.quit()