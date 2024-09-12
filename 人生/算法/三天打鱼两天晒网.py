#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/3 17:22


def days(year, month, day):
    li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a = 0
    for i in range(1990, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            a = a + 366
        else:
            a = a + 365
    for j in range(month - 1):
        a = a + li[j]
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month >= 3:
        a = a + 1
    a = a + day
    return a


list1 = ['晒网', '打鱼', '打鱼', '打鱼', '晒网']
y = 2021
m = 6
d = 3
n = days(y, m, d)

print(y, '年', m, '月', d, '日', list1[n % 5])
