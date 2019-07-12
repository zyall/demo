from  selenium import webdriver


dr = webdriver.Chrome()


dr.get("http://www.baidu.com")


# dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')

# dr.find_element_by_id("su").click()
dr.find_element_by_css_selector('#su')

dr.quit()



