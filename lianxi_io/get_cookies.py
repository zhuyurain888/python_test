from selenium import webdriver
from time import sleep, time, ctime

driver =webdriver.Chrome()
driver.get("http://www.baidu.com")

# cookie=driver.get_cookies()
# print(cookie)
# driver.quit()