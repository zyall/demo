from base.PageBase import PageBase
from selenium.webdriver.common.by import By


class PagePannel(PageBase):
    write_article = (By.XPATH,'//*[@id="menu-posts"]/a/div[3]')
    user_name = (By.XPATH,'//*[@id="wp-admin-bar-my-account"]/a/span')
    def __init__(self,driver=None):
        PageBase.__init__(self, driver)

    def click_wirte_article(self):
        self.wait_element(*self.write_article).click()

    def get_account_name(self):
        return self.wait_element(*self.user_name).text


