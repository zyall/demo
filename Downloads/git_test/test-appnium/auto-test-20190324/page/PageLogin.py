from base.PageBase import PageBase
from selenium.webdriver.common.by import By
from page.PagePannel import PagePannel


class PageLogin(PageBase):
    user_name = (By.ID,"user_login")
    password=(By.ID,"user_pass")
    btn = (By.ID,"wp-submit")
    error_msg = (By.XPATH,'//*[@id="login_error"]')

    def __init__(self,driver=None):
        PageBase.__init__(self, driver)

    def login(self,name,password):
        self.wait_element(*self.btn).click()


    def get_error_msg(self):
        return self.wait_element(*self.error_msg).text

if __name__== "__main__":
        pl = PageLogin()
        pl.login("admin","123456")
