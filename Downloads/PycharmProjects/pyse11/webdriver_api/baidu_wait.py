# coding=utf-8
# 设置元素等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import *
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print(ctime())
# driver.find_element(By.ID,value=None)
# driver.find_element(By.XPATH,'//*')
# 显示等待
# WebDriverWait(driver, 5, 1) 驱动，等待时长，步长
# presence_of_element_located 判断元素是否存在
try:
    element = WebDriverWait(driver, 5, 1).until(
        EC.presence_of_element_located((By.ID, "kw"))
    )
    element.send_keys('selenium')
except TimeoutException as e:
    print("element time out")

print(ctime())
# sleep(2)
driver.close()