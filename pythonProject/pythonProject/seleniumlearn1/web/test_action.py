import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestResult:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_key_down_up(self):
        # 键盘操作，需要借助Keys
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element(By.ID, "search-button").click()
        ele = self.driver.find_element(By.ID, 'search-term')
        ActionChains(self.driver).key_down(Keys.SHIFT, ele). \
            send_keys('appium').perform()
        time.sleep(4)

    def test_mouse_double(self):
        # 双击
        self.driver.get('https://vip.ceshiren.com/#/ui_study/action_chains')
        ele = self.driver.find_element(By.ID, 'primary_btn')
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(2)

    def test_mouse_action1(self):
        # 滑块
        self.driver.get('https://vip.ceshiren.com/#/ui_study/action_chains')
        start_ele = self.driver.find_element(By.ID, 'item1')
        end_ele = self.driver.find_element(By.ID, 'item3')
        ActionChains(self.driver).drag_and_drop(start_ele, end_ele).perform()
        time.sleep(2)

    def test_mouse_action2(self):
        # 鼠标固定选项
        self.driver.get('https://vip.ceshiren.com/#/ui_study/action_chains2')
        start_ele = self.driver.find_element(By.CSS_SELECTOR, '.menu')
        ActionChains(self.driver).move_to_element(start_ele).perform()
        self.driver.find_element(By.XPATH, "//*[text()=' 管理班 ']").click()
        time.sleep(2)

    def test_scroll_to_element(self):
        # 鼠标滚动
        self.driver.get('https://ceshiren.com/')
        start_ele = self.driver.find_element(By.XPATH, '//*[text()="MinIO怎么测试"]')
        ActionChains(self.driver).scroll_to_element(start_ele).perform()
        time.sleep(10)
