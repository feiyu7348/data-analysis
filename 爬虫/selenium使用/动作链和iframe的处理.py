#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('http://')
# 如果定位的标签是存在于iframe标签中的
bro.switch_to_frame('iframeResult')  # 切换浏览器标签定位的作用域

# 动作链  实例化对象
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17, 0).perform()  # perform立即执行动作链操作
    time.sleep(0.3)

# 释放动作链
action.release()

bro.quit()
