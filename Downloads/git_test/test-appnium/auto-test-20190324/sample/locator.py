from selenium import webdriver
import os
import time

driver = webdriver.Chrome();
driver.get("http://www.baidu.com")
wholep= driver.find_elements_by_xpath("/html")
wholep2= driver.find_element_by_css_selector("html")
