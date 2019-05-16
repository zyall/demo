from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("http://106.13.46.164:8080/iwebshop/")
time.sleep(3)
driver.find_element_by_link_text("登录").click()
time.sleep(2)
driver.find_element_by_name('login_info').send_keys('Allen')
driver.find_element_by_name('password').send_keys('liu246855sg')

# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/table/tbody/tr[5]/td[2]/input').click()


driver.find_element_by_class_name('submit_login').click()

driver.close()

driver.quit()
