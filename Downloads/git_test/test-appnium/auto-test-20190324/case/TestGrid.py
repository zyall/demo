from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capability = DesiredCapabilities.CHROME
driver = webdriver.Remote(command_executor="http://192.168.7.40:4444/wd/hub",desired_capabilities=capability)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
