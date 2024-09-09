# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.py
# Time       ：2024/9/5 20:53
# Author     ：FeiFei
# version    ：python 3.12
# Description：
"""
import numpy as np
import pandas as pd

data1 = np.random.randint(1, 10, size=5)
print("ndarray数组是:")
print(data1)
data2 = pd.Series(data1)
print("Series数组是:")
print(data2)
