# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 2.py.py
# Time       ：2024/9/5 19:31
# Author     ：FeiFei
# version    ：python 3.12
# Description：
"""
import numpy as np

# 改变数组形状
data1 = [1, 2, 3, 4, 5]
data2 = [1, 2, 3, 4, 5]
data = np.array([data1, data2])
print(data.shape)
data = data.reshape(5, 2)
print(data.shape)

# 数组转置
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_array = np.array(data)
print(data_array)
print(data_array.T)
