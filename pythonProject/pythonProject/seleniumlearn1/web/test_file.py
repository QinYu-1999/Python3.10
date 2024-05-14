
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from log.logging import logger


class TestFile:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_file_send(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, '.sc-icon.cu-icon').click()
        self.driver.find_element(By.CSS_SELECTOR, '.upload-btn_3JqrF').send_keys(
            "D:\pythonProject\pythonProject\pythonProject\seleniumlearn1\image\123.jpg")
        time.sleep(3)

    def test_alert(self):
        url = self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

        logger.debug('打开网页')
        self.driver.maximize_window()
        self.driver.switch_to.frame("iframeResult")

        start = self.driver.find_element(By.CSS_SELECTOR, '#draggable')
        ends = self.driver.find_element(By.CSS_SELECTOR, '#droppable')
        active = ActionChains(self.driver)
        active.drag_and_drop(start, ends).perform()
        time.sleep(2)
        # 点击alert弹框的确认按钮
        self.driver.switch_to.alert.accept()
        # 切换回主frame
        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.ID, 'submitBTN').click()
        self.driver.save_screenshot("file.png")
        logger.info('保存截图成功')
        time.sleep(4)