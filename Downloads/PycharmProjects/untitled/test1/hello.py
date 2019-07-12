#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()

driver.get("http://shixin.court.gov.cn/index.html")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='pName']").clear()
driver.find_element_by_xpath("//*[@id='pName']").send_keys("0678")
'''
driver.find_element_by_css_selector("#dl > input.form1").clear()
driver.find_element_by_css_selector("#dl > input.form1").send_keys("95714")
driver.find_element_by_css_selector("#password").clear()
driver.find_element_by_css_selector("#password").send_keys("0678")
driver.find_element_by_css_selector("#pwd > input.button").click()



<input type="text" id="pName" name="pName" style="width:336px;border:0px;" onchange="refreshCaptcha();">
'''