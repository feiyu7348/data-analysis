import selenium import webbrowser
import time

myDriver=webbrowser.Chrome()
time.sleep(3)

myDriver.get(r'http://weibo.com')
time.sleep(10)

myDriver.fine_element_by_xpath(r'/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/a[1]')
time.sleep(3)

myDriver.find._