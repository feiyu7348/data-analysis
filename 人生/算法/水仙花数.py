#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# for i in range(100, 1000):
#     bai = i // 100
#     shi = (i // 10) % 10
#     ge = i % 10
#     if bai ** 3 + shi **3 +ge ** 3 == i:
#         print(i)

def shuixianhua(m, n):
    for i in range(m, n):
        bai = i // 100
        shi = (i // 10) % 10
        ge = i % 10
        if bai**3 + shi**3 + ge**3 == i:
            print(i)
    if not i:
        print('no')

shuixianhua(100, 120)