#!/usr/bin/env python
# -*- coding:utf-8 -*-

#分数背包
goods = [(60, 10), (100, 20), (120, 30)]  # 每个商品元祖表示（价格，重量）
goods.sort(key=lambda x: x[0] / x[1], reverse=True)  # 对goods单位价值从大到小排序

def fractional_backpack(goods, w):  # w为能装的最大重量
    m = [0 for _ in range(len(goods))]  # 建立一个和goods一样长的列表
    total_v = 0  # 初始化总价值
    for i,(price, weight) in enumerate(goods):  # 枚举函数，一个一个取，i为索引值
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight
        else:  # 取的下一个物品重量大于背包剩余容量
            m[i] = w / weight  # w为背包剩余容量，此时m[i]为一个分数
            total_v += m[i] * price
            w = 0  # 最后背包剩余容量为0，这句代码不写也好像能行，写上便于理解
            break  # 跳出循环
    return total_v, m

print(fractional_backpack(goods,50))