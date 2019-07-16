from appium import webdriver
import os
from utils.logger import logger
import time
from appium.webdriver.common.touch_action import TouchAction

logger = logger(logger="PageBaseAndroid").getlog()
class PageBaseAndroid(object):
    def __init__(self, driver=None):
        if driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'ios'
            desired_caps['platformVersion'] = '12.1'
            desired_caps['deviceName'] = '127.0.0.1:62001'
            desired_caps['appPackage'] = 'com.youdao.note'
            desired_caps['automationName'] = 'UiAutomator2'
            desired_caps["unicodeKeyboard"] = True
            desired_caps["resetKeyboard"] = True
            desired_caps['appActivity'] = 'com.youdao.note.activity2.SplashActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver = driver

    def get_element(self, *locator):
        logger.info("查找元素 %s" % str(locator))
        return self.driver.find_element(*locator)

    #获取元素，智能等待
    def wait_element(self, *locator):
        ele = None
        count = 0
        while ele is None:
            count = count + 1
            try:
                ele = self.driver.find_element(*locator)
            except:
                pass
            flag = ele is not None
            logger.info("查找元素第%d次 %s %s " % (count, flag, str(locator)))
            time.sleep(0.1)
            if count > 30:
                logger.info("没有找到元素 %s" % str(locator))
                break
        return ele


    def wait_elements(self, *locator):
        eles = None
        count = 0
        while eles is None:
            count = count + 1
            try:
                eles = self.driver.find_element(*locator)
            except:
                pass
            flag = eles is not None
            logger.info("查找元素第%d次 %s %s " % (count, flag, str(locator)))
            time.sleep(0.1)
            if count > 30:
                logger.info("没有找到元素 %s" % str(locator))
                break
        return eles


    def long_touch(self,element):
        ta = TouchAction(self.driver)
        ta.long_press(element,duration=1000).perform()

