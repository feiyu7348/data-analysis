#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from lxml import etree
import time


bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('http://www.taobao.com/')

# 标签定位
search_input = bro.find_element_by_id('q')
# 标签交互
search_input.send_keys('iphone')
# 执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)
# 点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

bro.get('http://www.baidu.com')
time.sleep(3)
# 回退
bro.back()
time.sleep(3)
# 前进
bro.forward()

time.sleep(5)
bro.quit()

