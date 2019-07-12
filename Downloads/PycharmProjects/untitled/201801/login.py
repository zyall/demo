#coding:utf-8
from selenium import webdriver
import unittest
import time
class Blog(unittest.TestCase):
    u'''登录博客'''
    def setUp(self):
        self.driver=webdriver.Chrome()
        url="https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(20)  #设置等待超时
    def login(self,username,psw):
        u'''这里写了一个登录的方法，账号和密码参数化'''
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input1").send_keys(psw)
        self.driver.find_element_by_id()
        time.sleep(3)
    def tear_01(self):
        u'''登录案例参考：账号，密码自己设置'''
        self.login(u"上海-悠悠"，u"XXX")
        # 获取登录后的账号名称
        text=self.driver.find_element_by_id()
