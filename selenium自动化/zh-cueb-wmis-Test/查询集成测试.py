#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/3 22:05


from selenium import webdriver
from time import sleep


bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('http://localhost:8080/#/')
sleep(2)
# 标签定位
bro.find_element_by_tag_name('button').click()
sleep(2)

# 点击查询管理
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/div').click()
sleep(2)
# 点击货架仓库
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[1]').click()
sleep(3)
# 点击查询空货架或空库存
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[2]').click()
sleep(3)
# 点击查询库存为空的物品
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[3]').click()
sleep(3)
# 点击查看出库单
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[4]').click()
sleep(3)
# 点击根据名称查询出库单
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[5]').click()
sleep(3)
# 查询物品
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/div[1]/div/div/input').send_keys("啊")
sleep(2)
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/div[2]/button[1]/span').click()
sleep(3)
# 点击查看入库概单和入库详单
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[2]/ul/li[6]').click()
sleep(3)
# 查看详情
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[6]/div/button').click()
sleep(5)
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[3]/div/div[1]/button/i').click()
sleep(10)

bro.quit()