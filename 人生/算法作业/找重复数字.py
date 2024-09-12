#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/8 20:05

import random


random.seed(1000)
arr = [random.randint(0,1000) for _ in range(10000)]  # 随机生成一万个0到1000之间的数

b = []  # 存放数据

while len(arr) > 0:
    a = arr.pop(0)  # 删除第一个变量赋给新列表a
    count = arr.count(a) + 1  # 计算总数
    for i in range(count-1):
        arr.remove(a)

    b.append([a, count])  # 存起来，a为数字，count为出现次数


# 输出数字和个数
# for i in range(len(b)):
#     print("{}有{}个".format(b[i][0], b[i][1]))


# 获取b中数字的个数 后面进行排序
array = []
for i in range(len(b)):
    array.append(b[i][1])

array.sort(reverse=True)
# print(array)

# 打印
for n in list(reversed(list(set(array)))):  # 集合去重打印
    for i in range(len(b)):
        if b[i][1] == n:
            print("{}有{}个".format(b[i][0], n))
