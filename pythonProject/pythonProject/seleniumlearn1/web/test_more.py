import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

class TestMore:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
    def teardown_class(self):
        self.driver.quit()
    def test_more_chuangkou(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.set_window_size()
        self.driver.maximize_window()
        # time.sleep(10)
        # ActionChains(self.driver).move_to_element(By.CSS_SELECTOR,"#u1 #s-top-loginbtn").perform()
        self.driver.find_element(By.CSS_SELECTOR,"#u1 #s-top-loginbtn").click()
        # print(self.driver.current_window_handle)
        self.driver.find_element(By.CSS_SELECTOR,'.tang-pass-footerBar #TANGRAM__PSP_11__regLink').click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        self.driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_4__userName']").send_keys("username")
        time.sleep(3)
        self.driver.switch_to.window(window[0])
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__changeSmsCodeItem').click()
        # self.driver.find_element(By.XPATH,"//*[@id='s-user-name-menu']//*[text()='切换账号']").click()
    def test_frame(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        logging.debug('打开网页')
        # print(self.driver.find_element(By.ID, "frame_btn"))
        self.driver.switch_to.frame("frame1")
        print(self.driver.find_element(By.ID, "frame_btn").text)
        #切换回父frame
        # self.driver.switch_to.parent_frame()
        #切换回默认frame
        # self.driver.switch_to.default_content()
        # print(self.driver.find_element(By.ID, "success_btn").text)
        self.driver.switch_to.frame("frame2")
        self.driver.find_element(By.XPATH,".el-table__row")