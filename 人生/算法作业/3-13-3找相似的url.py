#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 认为前面的目录相同则为相似
import re

given_url = 'https://blog.csdn.net/weixin_51617086'
urls = ['https://blog.csdn.net/weixin_51617086/article/details/117405692?spm=1001.2014.3001.5501',
        'https://blog.csdn.net/weixin_51617086/article/details/117339353?spm=1001.2014.3001.5501',
        'https://blog.csdn.net/weixin_51617086/article/details/117299551?spm=1001.2014.3001.5501',
        'https://space.bilibili.com/146015656/favlist?fid=1239219656&ftype=create',
        'https://so.csdn.net/so/search',
        'https://blog.csd./251/nweixin_51617086']

for url in urls:
    rs = re.match(r'https://blog.csdn.net/weixin_51617086.*', url)
    if rs is not None:
        print("相似url:{}".format(rs.group()))







