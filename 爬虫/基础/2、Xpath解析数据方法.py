#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree

# 解析html文件
html = etree.parse('./text.html', etree.HTMLParser())
# 提取数据
r = html.xpath('/html/body/ul/li/a/text()')
print(r)

# 提取全部数据 两个斜杠
r = html.xpath('//li/a/text()')
print(r)

# 获取指定标签里面的li标签
t = html.xpath('//div[@class="teacher"]//li/a/text()')
print(t)
h = html.xpath('//div[@class="teacher"]//li/a/@href')
print(h)
# 文本和链接放到一起
res = list(zip(t, h))
print(res)


'''
    /  当前元素的直接子结点
    //  当前元素的子孙结点 
    
    text()   获取文本
    @attr   获取属性对应的值
'''