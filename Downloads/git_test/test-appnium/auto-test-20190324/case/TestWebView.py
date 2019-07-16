from appium import webdriver
import unittest
import time

class TestWebView(unittest.TestCase):
    def test_web_view(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.youdao.note'
        #desired_caps['automationName'] = 'UiAutomator2'
        #desired_caps["unicodeKeyboard"] = True
        #desired_caps["resetKeyboard"] = True
        desired_caps['appActivity'] = 'com.youdao.note.activity2.SplashActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # driver.find_element_by_id("com.youdao.note:id/tab_name").click()
        # driver.find_element_by_id("com.youdao.note:id/mytask").click()
        # driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.ImageView[1]").click()
        driver.find_element_by_xpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[3]").click()
        webview = driver.contexts
        print(webview)
        driver.switch_to.context(webview[2])
        resource = driver.page_source
        driver.find_element_by_xpath("").send_keys()





if __name__ == "__main__":
        unittest.main()