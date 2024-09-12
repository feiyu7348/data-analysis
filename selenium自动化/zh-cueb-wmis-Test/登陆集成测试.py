#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/2 11:10


from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('http://localhost:8080/#/')
sleep(2)
# 标签定位
search_input = bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').clear()
userName_tag = bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input')
sleep(2)
userName_tag.clear()
sleep(2)
# 标签交互
# 测试正确的用户名
userName_tag.send_keys('guojiale')
sleep(5)


a_tag = bro.find_element_by_tag_name('button')
a_tag.click()



