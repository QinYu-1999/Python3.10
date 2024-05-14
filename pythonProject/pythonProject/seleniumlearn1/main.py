# This is a sample Python script.
import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from web import web_1, test_wait


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def start():
    driver = webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study/locate')
    # 1.ID定位
    # find_id = driver.find_element(By.ID, 'located_id')
    # print(find_id)
    # 2.name定位
    # find_name = driver.find_element(By.NAME, 'located_name')
    # print(find_name)
    # 3.css定位
    # find_xss = driver.find_element(By.CSS_SELECTOR,"#app > div > section > section > main > div > div.box > div:nth-child(3) > button > span")
    # print(find_xss)
    # 4.xpath定位
    # find_xpath = driver.find_element(By.XPATH,'//*[@id="locate_id"]/a/span')
    # print(find_xpath)
    # # 5.linktext定位
    # find_linktext = driver.find_element(By.LINK_TEXT,'元素定位')
    # print(find_linktext)
    driver.quit()


def start_element_interactions():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study/locate")
    # #输入文本“小狗”
    # driver.find_element(By.ID, 'kw').send_keys('小狗')
    # time.sleep(2)
    # #清空输入框
    # driver.find_element(By.ID, 'kw').clear()
    # time.sleep(2)
    # driver.find_element(By.ID, 'kw').send_keys('小狗')
    # #点击搜索按钮
    # driver.find_element(By.ID, 'su').click()
    # time.sleep(5)
    # 获取元素的属性
    # web_s = driver.find_element(By.ID,'kw1')
    # res = web_s.get_attribute('name')
    # 隐式等待
    # driver.implicitly_wait(3)
    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.ID, 'success_btn'))
    )
    driver.find_element(By.ID, 'success_btn').click()
    time.sleep(5)
    driver.quit()

def element_css():
    driver = webdriver.Chrome()
    driver.get("https://ceshiren.com/search?expanded=true")
    driver.find_element(By.CSS_SELECTOR,"[placeholder='搜索']").send_keys('appium')
    driver.find_element(By.CSS_SELECTOR,".search-cta").click()
    time.sleep(5)
# Press the green button in the gutter to run the script.
def test_xpath():
    driver = webdriver.Chrome()
    driver.get('https://yingshi.tv/vod/play/id/195/sid/1/nid/1.html')
    res = driver.find_element(By.XPATH,'//*[@class="ys_menuNavList ys_menuNavShowType"]//a[1]')
    driver.quit()

if __name__ == '__main__':
    test_wait.wait_unit()
    # start()
    # start_element_interactions()
    # element_css()
    # test_xpath()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
