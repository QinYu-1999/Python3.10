from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
option.debugger_address = "localhost:9222"
drive = webdriver.Chrome(options=option)
drive.get("https://github.com/")
