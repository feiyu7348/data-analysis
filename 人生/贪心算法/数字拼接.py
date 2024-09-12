#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]

def xy_cmp(x, y):
    if x+y < y+x:  # 前面是小的数加大的数，比如128和1286得1281286，比1286128小
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(li):
    li = list(map(str, li))  # 把li列表中的数字转成字符串再变成一个新列表
    li.sort(key=cmp_to_key(xy_cmp))  # cmp_to_key函数返回的参数是xy_cmp函数,不会可以用冒泡排序
    return ''.join(li)  #join函数连接字符串

print(number_join(li))