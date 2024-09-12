#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/5/31 22:50


# 二、URL字串上大都相同则为相似，拟定为80%以上为相似
given_url = 'https://blog.csdn.net/weixin_51617086'
urls = ['https://blog.csdn.net/weixin_51617086/article/details/117405692?spm=1001.2014.3001.5501',
        'https://blog.csdn.net/weixin_51617086/article/details/117339353?spm=1001.2014.3001.5501',
        'https://blog.csdn.net/weixin_51617086/article/details/117299551?spm=1001.2014.3001.5501',
        'https://space.bilibili.com/146015656/favlist?fid=1239219656&ftype=create',
        'https://so.csdn.net/so/search',
        'https://blog.csd./251/nweixin_51617086']

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    arr = [[0 for _ in range(len2+1)] for _ in range(len1+1)]  # len1+1行，len2+1列
    b = [[0 for _ in range(len2+1)] for _ in range(len1+1)]  # 用于记录字符位置 1 左上方 2 上方 3 左方
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:  # i j位置上的字符匹配的时候，来自于左上方+1
                arr[i][j] = arr[i-1][j-1] + 1
                b[i][j] = 1
            elif arr[i-1][j] > arr[i][j-1]:  # 来自于上方
                arr[i][j] = arr[i-1][j]
                b[i][j] = 2
            else:
                arr[i][j] = arr[i][j-1]
                b[i][j] = 3
    return arr[-1][-1], b

def lcs_trackback(x, y):  # 回溯
    arr, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 来自于左上方 匹配
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自于上方 不匹配
            i -= 1
        else:
            j -= 1  # 来自于左方 不匹配
    return ''.join(reversed(res))


for url in urls:
    com = lcs_trackback(given_url, url)
    if len(com) / len(given_url) >= 0.5:
        print("公共子序列：{}，url:{}".format(com, url))
