import json
import time

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from log.logging import logger


class TestLitemall:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://litemall.hogwarts.ceshiren.com/#/login?redirect=%2Fdashboard")
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys('manage')
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME, 'password').send_keys('manage123')
        logger.debug('\nusername/pw输入成功')
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("cookies.yaml", "w") as f:
            yaml.safe_dump(cookies, f)
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary').click()
        frist_page = self.driver.find_element(By.XPATH, '//*[text()="首页"]')

        assert frist_page.text == '首页'
        logger.info("登陆成功")

    def test_add(self):
        self.test_login()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/div/span').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li/span').click()

        self.driver.find_element(By.XPATH, '//*[text()="添加"]').click()
        logger.debug('进入添加页面')
        context = 'sel-text'
        context2 = 'nihao'

        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div[1]/input') \
            .send_keys(
            context)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/div[1]/input').send_keys(
            context2)
        logger.debug('输入成功')
        action = ActionChains(self.driver)
        scroll_1 = self.driver.find_element(By.XPATH, '//*[text() = "上架"]')
        action.scroll_to_element(scroll_1).perform()
        scroll_1.click()
        mes = self.driver.find_element(By.CSS_SELECTOR, '.el-message-box__message')
        # aler = self.driver.switch_to.alert
        if mes:
            logger.debug(mes.text)
        else:
            aler = self.driver.find_element(By.CSS_SELECTOR, '.el-notification__title')
            logger.debug(aler.text)
            assert aler.text == '成功'

    def test_delete(self):
        # self.test_login()
        self.test_add()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[text()="nihao"]')))
        dele = self.driver.find_elements(By.CSS_SELECTOR, '.el-button--danger')
        logger.debug(dele[0])
        dele[0].click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.el-notification__title')))
        aler = self.driver.find_element(By.CSS_SELECTOR, '.el-notification__title')
        logger.debug(aler.text)

    def test_add_cookies(self):
        self.driver.get(
            "https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua/a.754894437.1.5af92a89UmXdBF&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
        time.sleep(10)
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # with open("cookies.yaml", "w") as f:
        #     yaml.safe_dump(cookies, f)
        with open("cookies.yaml",'r') as f:
            c = yaml.safe_load(f)
        for i in c:
            self.driver.add_cookie(i)
        self.driver.get(
            "https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua/a.754894437.1.5af92a89UmXdBF&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
        time.sleep(5)