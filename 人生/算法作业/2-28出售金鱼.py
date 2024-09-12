#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = 11

while True:
    a = n - (n / 2 + 1 / 2)  # 卖出第一次剩余
    b = a - (a / 3 + 1 / 3)  # 卖出第二次剩余
    c = b - (b / 4 + 1 / 4)  # 卖出第三次剩余
    d = c - (c / 5 + 1 / 5)  # 卖出第四次剩余
    if d == 11:
        print(n)
        break
    else:
        n += 1
