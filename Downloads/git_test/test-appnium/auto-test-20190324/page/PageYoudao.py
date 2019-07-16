from selenium.webdriver.common.by import By
from base.PageBaseAndroid import PageBaseAndroid

class PageYoudao(PageBaseAndroid):

    def __init__(self,driver=None):
        PageBaseAndroid.__init__(self, driver)


    ele_add_note = (By.ID,"com.youdao.note:id/add_note")
    ele_add_icon = (By.ID,"com.youdao.note:id/add_icon")
    ele_note_title = (By.ID,"com.youdao.note:id/note_title")
    ele_note_content = (By.XPATH,"//android.widget.LinearLayout[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText[1]")
    ele_actionbar_complete_text = (By.ID,"com.youdao.note:id/actionbar_complete_text")
    ele_save_toast = (By.XPATH,"//*[contains(@text,'成功')]")

    ele_note_first=(By.XPATH,"//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]")
    ele_delete = (By.XPATH,"//android.widget.TextView[@text='删除']")
    ele_confirm = (By.ID,"com.youdao.note:id/btn_ok")
    ele_note_tile_first =(By.XPATH,"//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")


    def add_note(self,title,content):
        self.wait_element(*self.ele_add_note).click()
        self.wait_element(*self.ele_add_icon).click()
        self.wait_element(*self.ele_note_title).send_keys(title)
        self.wait_element(*self.ele_note_content).send_keys(content)
        self.wait_element(*self.ele_actionbar_complete_text).click()

    def get_save_toast(self):
        return self.wait_element(*self.ele_save_toast).text

    def del_note(self):
        ele = self.wait_element(*self.ele_note_first)
        self.long_touch(ele)
        self.wait_element(*self.ele_delete).click()
        self.wait_element(*self.ele_confirm).click()

    def get_note_fist_title_text(self):
        return self.wait_element(*self.ele_note_tile_first).text

    def get_note_fist_title_text_by_id(self):
        eles = self.wait_element((By.ID,"com.youdao.note:id/title"))
        return eles.text


        # ele = driver.find_element_by_xpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]")
        # from appium.webdriver.common.touch_action import TouchAction
        # ta = TouchAction(driver)
        # ta.long_press(ele,duration=1000).perform()
        # driver.find_element_by_xpath("//android.widget.TextView[@text='删除']").click()
        # driver.find_element_by_id("com.youdao.note:id/btn_ok").click()






if __name__=="__main__":
       p = PageYoudao()
       #p.add_note("frame title 中文","frame content ")
       p.del_note()
