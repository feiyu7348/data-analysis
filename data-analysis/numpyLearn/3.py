# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 3.py
# Time       ：2024/9/5 20:34
# Author     ：FeiFei
# version    ：python 3.12
# Description：
"""
import numpy as np

# 数组维度
data = np.array([1, 2, 3])
print(data.ndim)
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.ndim)

# 数组形状
print(data.shape)

# 数组中元素个数
print(data.size)

# 数组的数据类型
print(data.dtype)

