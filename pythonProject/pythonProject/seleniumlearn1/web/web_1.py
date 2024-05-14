from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.var = {}

    def teardown_method(self):
        self.driver.quit()

    def test_sougou(self):
        self.driver.get("https://www.sogou.com/")
        self.driver.set_window_size(1235, 693)
        # 输入搜索信息

        self.driver.find_element(By.ID, "query").click()
        self.driver.find_element(By.ID, "query").send_keys("缅甸")
        # 点击搜索
        self.driver.find_element(By.ID, 'stb').click()
        element = self.driver.find_element(By.ID, 'stb')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        res_data = self.driver.find_element(By.CSS_SELECTOR, "#sogou_vr_70193901_title_0 > h3 > span")
        assert (res_data.text == '缅甸')


class Test_2():
    def set_driver(self):
        self.driver = webdriver.Chrome()

    def quit_b(self):
        self.driver.quit()

    def start_b(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study')
        find_id = self.driver.find_element(By.ID, 'located_id')
        print(find_id)
