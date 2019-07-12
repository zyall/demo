# coding=utf-8

# 第一步导入webdriver模块
from selenium import webdriver
import time

# 第二步打开浏览器
driver=webdriver.Chrome()

# 第三步打开百度
driver.get("https://www.baidu.com")
time.sleep(3)
driver.get("http://www.runoob.com/python/python-100-examples.html")
# 设置休眠时间3秒，也可以是小数，单位是秒
time.sleep(3)
# 页面刷新
driver.refresh()
# 返回上一页
driver.back()
time.sleep(3)
# 切换到下一页
driver.forward()
# 设置窗口大小为540*960
driver.set_window_size(540,960)
time.sleep(2)
# 将浏览器窗口最大化
driver.maximize_window()
# 截屏
driver.get_screenshot_as_file("/Users/zq1/PycharmProjects/201801/f.jpg")
# 退出
driver.quit()


