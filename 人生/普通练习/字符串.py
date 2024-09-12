# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/3 19:09


str1 = "k1:1|k2:2|k3:3|k4:4"


def str2dict(str1):
    dit = {}
    for i in str1.split('|'):
        print(i.split(':'))
        k, v = i.split(':')
        dit[k] = v

    return dit


# print(str2dict(str1))

a, b = [1, 2]
print(a, b)
