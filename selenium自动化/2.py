#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/5/30 17:17

from selenium import webdriver

wd = webdriver.Chrome()
# 设置最大等待时长为 10秒
wd.implicitly_wait(10)

wd.get('https://www.baidu.com')

element = wd.find_element_by_id('kw')

element.send_keys('黑羽魔巫宗\n')

element = wd.find_element_by_id('1')

print(element.text)
