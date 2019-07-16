from selenium import webdriver
import os

os.system("taskkill /im chromedriver.exe /f")
driver= webdriver.Chrome()
driver.get("file:///E:/zl/20190324/share/20190602/a.html")
driver.find_element_by_id("alert").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element_by_id("confirm").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element_by_id("prompt").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Mike")
driver.switch_to.alert.accept()

