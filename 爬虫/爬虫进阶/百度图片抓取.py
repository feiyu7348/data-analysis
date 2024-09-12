#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import os


# 进行数据爬取
def getPage(kw, num):
    pass


# 下载图片到本地
def downloadImage(datalist, dir):
    # 检查文件是否存在
    if not os.path.exists(dir):
        os.mkdir(dir)
    # 下载图片到本地
    x = 0
    for data in datalist:
        for i in data:
            if i.get('thumbURL') is not None:
                print(f"下载图片{i.get('thumbURL')}")
                imgres = requests.get(i.get('thumbURL'))
                open(f'{dir}/{x}.jpg', 'wb').write(imgres.content)
                x += 1


# 获取用户输入信息
ketword = input("请输入搜索图片的关键字：")
# 调用函数，进行数据的爬取，可以指定关键字和下载页数
datalist = getPage(ketword, 2)
# 调用函数，保存数据，可以指定要保存的图片路劲
downloadImage(datalist, './baidu')
