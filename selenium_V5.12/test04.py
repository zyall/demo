from selenium import  webdriver
import time


driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
time.sleep(3)
driver.get("https://taobao.com")
time.sleep(3)

# 网页后退方法
driver.back()
time.sleep(3)
# 网页前进方法
driver.forward()
time.sleep(3)

driver.close()

driver.quit()
