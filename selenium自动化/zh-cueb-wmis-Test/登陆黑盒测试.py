#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/3 10:47


from selenium import webdriver
from time import sleep
import unittest


class Testcases(unittest.TestCase):
    bro = webdriver.Chrome(executable_path='chromedriver.exe')
    bro.get('http://localhost:8080/#/')
    sleep(2)
    # 标签定位
    bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').clear()
    userName_tag = bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input')
    sleep(2)

    def setUp(self) ->None:
        print("每个用例的前置")

    def tearDown(self) ->None:
        print("每个用例的后置")

    def test01(self):
        # 标签交互
        # 等价分类法
        self.userName_tag.send_keys('ab')  # 两个字母
        sleep(2)
        self.bro.find_element_by_tag_name('button').click()
        sleep(2)

    def test02(self):
        # 标签交互
        # 等价分类法
        self.bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').clear()
        self.userName_tag.send_keys('abcdefghijk')  # 十一个字母
        sleep(2)
        self.bro.find_element_by_tag_name('button').click()
        sleep(2)

    def test03(self):
        # 标签交互
        # 边界值分析法
        self.bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').clear()
        self.userName_tag.send_keys('asd')  # 三个字母
        sleep(2)
        self.bro.find_element_by_tag_name('button').click()
        sleep(2)

    def test04(self):
        # 标签交互
        # 边界值分析法
        self.bro.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').clear()
        self.userName_tag.send_keys('abcdefghij')  # 十个字母
        sleep(2)
        self.bro.find_element_by_tag_name('button').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
