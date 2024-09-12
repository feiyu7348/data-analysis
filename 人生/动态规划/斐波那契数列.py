#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 递归 运行效率低，因为子问题的重复计算
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

# 非递归 可以理解为动态规划(DP)思想 = 最优子结构（递推式）+ 重复子问题（存起来，不需要重复计算）
def fibnacci_no_recurision(n):
    f = [0,1,1]  # 使下标一致，第一项是1
    if n >2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]

print(fibnacci(5))
print(fibnacci_no_recurision(5))