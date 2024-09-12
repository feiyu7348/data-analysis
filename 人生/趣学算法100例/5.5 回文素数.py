# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/7/5 18:59

import math


# 判断素数
def prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:  # 不是素数返回0
            return 0
    return 1  # 是素数返回1


def palindrome_prime():
    for i in range(0, 10):  # 穷举第一位
        for j in range(0, 10):  # 穷举第二位
            for k in range(0, 10):  # 穷举第三位
                n = i * 100 + j * 10 + k  # 组成的整数
                m = i + j * 10 + k * 100  # 对应的反序数
                if i == 0 and j == 0:  # 处理整数前两位为0的情况
                    m = m // 100
                elif i == 0:  # 处理整数第一位为0的情况
                    m = m // 10
                if n > 10 and n == m and prime(n):  # 若大于十且为回文数并且是素数
                    print(n, end=" ")


palindrome_prime()
