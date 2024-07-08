from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestLitemall:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get('https://www.luffycity.com/')
        self.driver.find_element(By.CSS_SELECTOR, ".signin").click()
        pop = self.driver.find_element(By.CSS_SELECTOR, ".popup-content")
        # WebDriverWait(self.driver).until(expected_conditions.presence_of_element_located(pop))
        self.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div[1]/div[1]/input').send_keys(
            "17722754206")
        self.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div[1]/div[2]/input').send_keys(
            "754206")
        self.driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.singin-popup > div > div > button").click()

        self.driver.find_element(By.XPATH,'//*[@id="__layout"]/div/header/div/div/nav/a[3]/li').click()
        # heijin = self.driver.find_element(By.XPATH,"//*[text()='黑金卡激活成功！']")
        # assert heijin.text == "黑金卡激活成功！"
