#!/usr/bin/env python
# -*- coding:utf-8 -*-


t1 = [100, 50, 20, 5, 1]

def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n  # 最后剩了n块钱

def change1(t, n):
    m = []
    for money in t:
        m.append(n // money)
        n = n % money
    return m, n      # 最后剩了n块钱


# print(change1(t1, 376))
print(change(t1, 281))