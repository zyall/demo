# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestFirefox(unittest.TestCase):
    '''
    商城平台的订单流程
    '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://106.13.46.164:8080"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_firefox(self):
        driver = self.driver
        driver.get(self.base_url + "/iwebshop/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_name("login_info").clear()
        driver.find_element_by_name("login_info").send_keys("Allen")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("liu246855sg")
        driver.find_element_by_class_name('submit_login').click()
        time.sleep(10)
        loginresult = driver.find_element_by_class_name('loginfo')
        print(loginresult.text)
        self.assertEqual(u'Allen您好，欢迎您来到iwebshop购物！[安全退出]',loginresult.text)
        driver.find_element_by_link_text(u"特价商品").click()
        driver.find_element_by_id("buy_now").click()
        time.sleep(10)
        driver.find_element_by_class_name("submit_order").click()
        time.sleep(10)
        orderresult = driver.find_elements_by_class_name("f14")
        print(orderresult[0].text)
        self.assertEqual(u"订单已提交",orderresult[0].text)
        driver.find_element_by_class_name("submit_pay").click()
        time.sleep(10)
        # 切换窗口
        n = driver.window_handles
        driver.switch_to.window(n[1])
        payresult = driver.find_elements_by_class_name("f14")
        print(payresult[0].text)
        self.assertEqual(u"支付成功",payresult[0].text)



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
