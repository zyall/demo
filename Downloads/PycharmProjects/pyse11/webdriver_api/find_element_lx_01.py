#coding:utf-8
from selenium import webdriver
dr = webdriver.Chrome()
# dr.get("http://mail.126.com/")
dr.get("https://mail.qq.com/")
# 隐式等待5s
dr.implicitly_wait(10)
# 先定位iframe
# frame = dr.find_element_by_css_selector('div#loginDiv>ifame')
frame=dr.find_element_by_xpath('//*[@id="login_frame"]')
# 再通过frame_element切换iframe
dr.switch_to_frame(frame)
# 定位用户邮箱
dr.find_element_by_xpath('//*[@id="img_out_1554754887"]').click()
# 输入独立密码
dr.find_element_by_xpath('//*[@id="pp"]').send_keys('123900600all')
# 点击登录
dr.find_element_by_xpath('//*[@id="btlogin"]').click()
# 获取cookie
# cookie = dr.get_cookies()

# for cookie in dr.get_cookies():
#     print("%s:%s"%(cookie['name'],cookie['value']))

# dr.close()
