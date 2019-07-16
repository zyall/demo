from selenium import  webdriver
import time
import os

#driver = webdriver.Chrome("E:/zl/20190324/share/20190602/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

time.sleep(2)
driver.find_element_by_xpath("//*[@id='u1']/a[1]").click()
time.sleep(2)
driver.find_element_by_id("ww").send_keys("abcd")
driver.find_element_by_id("s_btn_wr").click()
time.sleep(2)
main_handle = driver.current_window_handle
elements = driver.find_elements_by_xpath("//div/h3/a")
for ele in elements:
    print(ele.text)
    ele.click()
    handles = driver.window_handles
    for h in handles:
        if h != main_handle:
            driver.switch_to.window(h)
            driver.close()
    driver.switch_to.window(main_handle)
os.system("taskkill /im chromedriver.exe /f")
driver.quit()