from selenium import webdriver
from time import sleep, time, ctime

driver =webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)#隐示等待
print(ctime())
#判断一个元素是否存在
for i in range(10):
    print ( i )
    try:
        ele=driver.find_element_by_id("1kw")
        print (i)
        if ele.is_displayed():
            driver.close()
            print(i)
            break
    except:
        pass
    sleep(1)
else:
    print("超时")
    driver.close ()
    print ( ctime () )
