#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/3 10:59

from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('http://localhost:8080/#/')
sleep(2)


a_tag = bro.find_element_by_tag_name('button')
a_tag.click()
sleep(2)

ruku_tag = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[1]/div').click()
sleep(1)
rukugaidan_tag = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/ul/li[1]/ul/li[1]/span').click()
sleep(1)
shengchengrukudan = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/button/span').click()
sleep(1)
lingxingruku = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/button[1]/span').click()
sleep(1)
# 添加物品
# 品名
name = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[1]/div/div/input')
name.send_keys("苹果")
sleep(1)
# 规格
spec = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[2]/div/div/input')
spec.send_keys("10个/箱")
sleep(1)
# 单位
unit = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[3]/div/div/input')
unit.send_keys("箱")
sleep(1)
# 数量
unit = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[4]/div/div/input')
unit.send_keys("30")
sleep(1)
# 单价
price = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[5]/div/div/input')
price.send_keys("5")
sleep(1)
# 生产日期
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[6]/div/div[1]/div/span[1]/i').click()
sleep(1)
product = bro.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[5]').click()
# /html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[5]
sleep(1)
# 保质期
life = bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[7]/div/div/input')
life.send_keys("12")
sleep(1)
# 库房
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[8]/div/div/div/input').click()
sleep(1)
house = bro.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
sleep(1)
# 货架
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[9]/div/div/div[1]/input').click()
sleep(1)
huojia = bro.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
sleep(1)
# 提交
bro.find_element_by_xpath('//*[@id="app"]/div/section/section/main/div/div[2]/div/form/div[10]/div/button[1]').click()
sleep(1)
