#!/usr/bin/env python
# coding: utf-8

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import requests
import json  #传递对象的语法
import re #z正则
import xlrd #读取Excel的扩展工具
import csv

import matplotlib.pyplot as plt #画图用的
#魔法函数
%matplotlib  inline

result = {} #建立空列表
# 记录次数，格式为{nums:[name,自问自答次数，评论次数，签到次数]}

with open('名单.csv', 'r', encoding='utf-8-sig') as f:  #encoding='utf-8-sig'编码
    reader = csv.reader(f)
    for row in reader:
        result[row[0]]=[row[1],0,0,0]

result

browser = webdriver.Chrome() #selenium的定义
browser.get("https://www.icourse163.org/")
browser.get('https://www.icourse163.org/learn/CUEB-1450000234?tid=1461631472#/learn/content')
time.sleep(2) #暂停俩秒
# 先把第一章的菜单合上
browser.find_element_by_xpath(r'//*[@class="titleBox j-titleBox f-cb"]').click()

def re(str_of_re:str):
    str_of_re = str_of_re.lower()
    nums = re.compile(r"(?<=\+)\d{11}")
    num = nums.findall(str_of_re)
    return num
def cal_zwzd(nums):
    if nums in result:
        result[nums][1]+=1
def cal_pl(nums):
    if nums in result:
        result[nums][2]+=1
def cal_qd(nums):
    if nums in result:
        result[nums][3]+=1

def start_pa (i):
    browser.get('https://www.icourse163.org/learn/CUEB-1450000234?tid=1461631472#/learn/content')
    time.sleep(1)
    chapter = browser.find_elements_by_xpath(r'//*[@class="titleBox j-titleBox f-cb"]')
    chapter = chapter[:-1]
#     第一个菜单合上
    suc = 1#安全作用
    while(suc):
       try:
            browser.find_element_by_xpath(r'//*[@class="titleBox j-titleBox f-cb"]').click()
            suc = 0
       except:
            pass
#     点开第i个菜单
    chapter[i].click()
#     点开在里面找本章收获
    time.sleep(1)
    try:
        questions = browser.find_elements_by_xpath(r'//*[@class="j-name name f-fl f-thide"]')
        for one_question in questions:
            if "本章收获与问题是什么" in one_question.text:
                one_question.click()
                break
    except:
        print(f"第{i}个菜单有问题")
    ye = 1
    # 看看有多少页
    time.sleep(1)
    a = browser.find_elements_by_xpath(r'//*[@id="courseLearn-inner-box"]/div/div/div[3]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[2]//a')
    ye_num = 1
    try:
        ye_num = int(a[-2].text)
    except:
        print("只有一页")
    while(ye <= ye_num):
        try:
    #       找所有自问自答
            print(f"正在爬第{ye}页")
            answer = browser.find_elements_by_xpath(r'//div[contains(@class,"m-detailInfoItem")]/div[2]/p')
            for one_answer in answer:
                if "刘经纬" in one_answer.text:
                    continue
                elif '++' in one_answer.text and '--'in one_answer.text and '=='in one_answer.text:
                    nums= reg(one_answer.text)
                    time.sleep(1)
                    for one_num in range(len(nums)):
                        cal_zwzd(nums[one_num])
    #         找所有评论和签到
    #         如果评论数很大就是签到，很小就是评论
            comment = browser.find_elements_by_xpath(r'//div[contains(@class,"m-comment-pool")]')
            qd_list =[]
            for comment_num in range(len(comment)):
                c = reg(comment[comment_num].text)
                if len(c)>10:
    #                 就是签到
                    for qd_num in range(len(c)):
                        cal_qd(c[qd_num])
                    if len(c)==20:
#                         如果有评论数是20的就记下来，可能需要点下一页。
                        qd_list.append(comment_num)                     
                if len(c)<=5:
    #                 就是评论
                    for m in range(len(c)):
                        cal_pl(c[m])   
    #         读完了之后把每一个下一页都点开
            next_button = browser.find_elements_by_xpath(r'//a[contains(@class,"zbtn znxt")]')
        except:
            pass
        if len(qd_list)>0:
            try:
                for nxt in qd_list:
                    next_button[nxt].click()
                time.sleep(1)
                comment = browser.find_elements_by_xpath(r'//div[contains(@class,"m-comment-pool")]')
                qd_list_again = []
                for nxt in qd_list:
                    c = reg(comment[nxt].text)
                    if len(c)==20:
                        qd_list_again.append(comment_num)
                    for qd_num in range(len(c)):
                        cal_qd(c[qd_num])
                if len(qd_list_again)>0:
                    for nxt in qd_list_again:
                        next_button[nxt].click()
                    time.sleep(1)
                    comment = browser.find_elements_by_xpath(r'//div[contains(@class,"m-comment-pool")]')
                    for nxt in qd_list_again:
                        c = reg(comment[nxt].text)
                        for qd_num in range(len(c)):
                            cal_qd(c[qd_num])
            except:
                pass
        
        ye+=1
        try:
            next_page = browser.find_elements_by_xpath(r'//a[contains(@class,"zbtn znxt")]')
            next_page[-1].click()
            time.sleep(1)
        except:
            pass
        print("当前结果是：")
        print(result)

for i in range(9):
    print(i)
    start_pa(i)

result

df = pd.DataFrame.from_dict(result,orient='index',columns=['姓名','自问自答次数','评论次数','签到次数'])

df
df.to_csv('ljw_result.csv',encoding="utf-8-sig")

df = pd.read_csv('ljw_result.csv',encoding='utf-8-sig')
df.set_index(["Unnamed: 0"], inplace=True)
df.index.name=''
df.head(30)

df = df.drop(df[df['自问自答次数']==0].index)
name = df['姓名']
df = df.drop(['姓名'], axis=1)

df.describe()

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

train_X,test_X= train_test_split(df,test_size=0.7,random_state=5)
train_X

train_label = [89,90,87,86,84,92,98,96,91,80,99,89,88,88,89,92,95,97,83,85,82,86,93,87,93,90,94,81,90,91]
test_X

C = 0.1
clf = SVC(kernel = "linear", C = C)

clf.fit(train_X,train_label)
test_pred = clf.predict(df)

test_pred

df['label']=test_pred
df['姓名']=name

df

df.to_csv('final_result.csv',encoding="utf-8-sig")

