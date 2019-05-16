from selenium import  webdriver
import time


# 实例化对象，引用Chrome浏览器
driver = webdriver.Chrome()

# 访问地址的方法
driver.get("https://www.baidu.com/")

# 定位百度首页的搜索输入框，然后在输入框里面输入关键字"泽林"
driver.find_element_by_id("kw").send_keys("泽林")

# 定位到百度一下的按钮，并实现点击操作
driver.find_element_by_id("su").click()

# 线程延迟时间
time.sleep(3)
# 线程等待时间
driver.implicitly_wait(3)

driver.close()

driver.quit()


