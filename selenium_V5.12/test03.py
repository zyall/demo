from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
time.sleep(3)
# 获取当前的页面的title属性
title = driver.title
time.sleep(3)
# 获取当前页面的url
current_url = driver.current_url
print(current_url)

page_source = driver.page_source
print(page_source)

if title == '百度一下，你就知道':
    print("Excute Success")
else:
    print("Excute Failed")

driver.close()
driver.quit()
