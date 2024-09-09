# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 4.py
# Time       ：2024/9/5 20:39
# Author     ：FeiFei
# version    ：python 3.12
# Description：
"""
import numpy as np

# 加法
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)

# 乘法
result = array1 * array2
print(result)

data = [1, 5, 6, 9]
# 平均值
mindle = np.mean(data)
print(mindle)

# 中位数
data1 = np.median(data)

"""
计算数组的标准差
numpy.std(arr, axis=None, dtype=None, out=None): 计算数组的标准差。参数axis、dtype和out的含义与numpy.mean()
相同。

计算数组的方差
numpy.var(arr, axis=None, dtype=None, out=None): 计算数组的方差。参数axis、dtype和out的含义与numpy.mean()
相同。

计算数组的最小值
numpy.min(arr, axis=None, out=None): 计算数组的最小值。参数axis和out的含义与numpy.mean()
相同。

计算数组的最大值
numpy.max(arr, axis=None, out=None): 计算数组的最大值。参数axis和out的含义与numpy.mean()
相同

计算数组的元素之和
numpy.sum(arr, axis=None, dtype=None, out=None): 计算数组的元素之和。参数axis、dtype和out的含义与numpy.mean()
相同。

计算数组的元素乘积
numpy.prod(arr, axis=None, dtype=None, out=None): 计算数组的元素乘积。参数axis、dtype和out的含义与numpy.mean()
相同

计算数组的累积和
numpy.cumsum(arr, axis=None, dtype=None, out=None): 计算数组的累积和。参数axis、dtype和out的含义与numpy.mean()
相同。
"""