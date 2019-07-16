import unittest
from utils.logger import logger
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logger = logger(logger="test_add_note").getlog()


class test_add_note(unittest.TestCase):
    def get_toast_text(self, driver,text):
        try:
            toast_loc = (By.XPATH, "//*[contains(@text,'" + text + "')]")
            logger.info(toast_loc)
            ele = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
            return ele.text
        except:
            return None

    def test_my_add(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.youdao.note'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps['appActivity'] = 'com.youdao.note.activity2.SplashActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        time.sleep(10)

        eles = driver.find_element_by_id("com.youdao.note:id/title")
        print(eles[0].text)


        driver.find_element_by_id("com.youdao.note:id/add_note").click()
        time.sleep(2)
        driver.find_element_by_id("com.youdao.note:id/add_icon").click()
        time.sleep(2)
        driver.find_element_by_id("com.youdao.note:id/note_title").send_keys("title中文")
        driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText[1]").send_keys("content中文")
        driver.find_element_by_id("com.youdao.note:id/actionbar_complete_text").click()

        toast_location=(By.XPATH,"//*[contains(@text,'成功')]")
        #ele = WebDriverWait(driver=driver,timeout=10,poll_frequency=0.1,ignored_exceptions=None).until(EC.presence_of_element_located(*toast_location))
        #ele =WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_location))
        ele = self.get_toast_text(driver,"成功")
        print(ele)


#删除
        # ele = driver.find_element_by_xpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]")
        # from appium.webdriver.common.touch_action import TouchAction
        # ta = TouchAction(driver)
        # ta.long_press(ele,duration=1000).perform()
        # driver.find_element_by_xpath("//android.widget.TextView[@text='删除']").click()
        # driver.find_element_by_id("com.youdao.note:id/btn_ok").click()

        # from appium.webdriver.common.touch_action import TouchAction
        # ta = TouchAction(driver)
        # webelement =
        # ta.long_press(webelement).perform()


if __name__ == "__main__":
    unittest.main()