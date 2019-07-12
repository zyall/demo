# coding:utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
time.sleep(1)
driver.get("http://shixin.court.gov.cn/index.html")
#driver.find_element_by_name('//*[@id="pName"]').clear()

