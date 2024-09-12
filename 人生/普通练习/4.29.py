#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_count_max_ele(s):
    max_count = 0  # 记录最大的次数
    dct = {}  # 键为元素，值为次数
    for i in range(len(s)):
        if s[i] not in dct:  # 元素不在列表里，就加上，s[i]为键
            dct[s[i]] = 1  # 赋值为 1
        else:
            c = dct[s[i]] + 1  # 计数
            dct[s[i]] = c  # 更新次数
            if c > max_count:
                max_count = c
    return [k for k, v in dct.items() if v == max_count]  # 根据列表的值获取键


s = [1, 2, 3, 4, 1, 2, 3]
print(get_count_max_ele(s))

# def max_list(s):
#     tmp = 0
#     for i in s:
#         if s.count(i) > tmp:
#             max_ele = i
#             tmp = s.count(i)
#     return max_ele
#
#
# s = [1, 2, 3, 4, 1, 2, 3]
# print(max_list(s))

# from collections import Counter
# array = [0,1,2,2,3,4,4,4,5,6,2]
# print(Counter(array))
# print(Counter(array).most_common(1)[0][0])

# list = ['1', '2', '3', '6', '5', '6', '6', '2', '1', '2']
# result = max(set(list), key=list.count)
# print(result)
