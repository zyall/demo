from selenium import webdriver
import time
import os
os.system("taskkill /im chromedriver.exe /f")
driver= webdriver.Chrome()
driver.get("file:///E:/zl/20190324/share/20190602/a.html")

driver.get("file:///E:/zl/20190324/share/20190602/a.html")
time.sleep(2)
driver.find_element_by_xpath("//option[@value='saab']").click()
time.sleep(3)
driver.quit()
