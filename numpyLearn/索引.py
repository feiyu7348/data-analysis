# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 索引.py
# Time       ：2024/9/9 14:54
# Author     ：FeiFei
# version    ：python 3.12
# Description：
"""
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a[a > 4])
print(a[(a > 4) & (a < 8)])

# 两种返回值不一样
t1 = np.array([[10.5, 13, 16.3],
               [12, 12.5, 15.5]])
print(t1 > 12)
