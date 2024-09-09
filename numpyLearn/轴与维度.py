# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 轴与维度.py
# Time       ：2024/9/9 14:44
# Author     ：FeiFei
# version    ：python 3.12
# Description： 《Python气象应用编程》 3.3.2
"""
import numpy as np

vector = np.array([1, 2, 3])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('\n---向量---\n')
print(vector)  # 向量
print('\n---矩阵---\n')
print(matrix)  # 矩阵
print('\n---张量---\n')
print(tensor)  # 张量


print(matrix.ndim)
print(matrix.shape)
print(matrix.size)
