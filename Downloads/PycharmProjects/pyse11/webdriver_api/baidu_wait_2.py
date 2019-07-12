# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import *
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print(ctime())
for i in range(5):
    # is_displayed()：判断元素是否显示
    el = driver.find_element_by_id("kw").is_displayed()
    # 判断el是否True
    if el:
        break
    sleep(5)
else:
    print("elment time out")

print(ctime())
driver.find_element_by_id("kw").send_keys("selenium")
driver.close()

