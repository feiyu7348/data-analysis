#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 方法一
def permutation(array, start):  # start代表子字符串的首位置索引
    if array is None:
        return
    if start == len(array)-1:  # 完成全排列后输出当前排列的字符串
        print(''.join(array))
    else:
        i = start
        while i < len(array):
            array[start], array[i] = array[i], array[start]  # 交换start与i所在位置的字符
            permutation(array, start + 1)  # 固定第一个字符，对剩余的字符进行全排列
            array[start], array[i] = array[i], array[start]  # 还原start与i所在位置的字符
            i += 1


arr = ['a', 'b', 'c']
permutation(arr, 0)


# 方法二
# def string_permutation(s):
#     # 迭代终止条件
#     if len(s) <= 1:
#         return [s]
#     else:
#         temp_list = []
#         for i in range(len(s)):  # 遍历字符串 s 中的每个字符
#             for j in string_permutation(s[0:i] + s[i+1:]):  # 把除了s[i]字符以外的字符组成字符串然后让它迭代
#                 temp_list.append(s[i]+j)
#         return temp_list
#
# print(string_permutation('abc'))

"""
过程1：    
s = ‘abc’
s的长度为3
i 可以取 0，1，2
当 i = 0时，string_permutation([‘bc’])迭代，进入过程2(去看过程2)。
处理完过程2后返回到这里：
此时 j 只能取 ‘bc’，‘cb’，所以temp_list = [‘abc’，‘acb’]

当 i =1时，string_permutation([‘ac’])迭代，这里和 i = 0 的情况一模一样

过程2：
s = ‘bc’
s的长度为2
i 可以取 0，1
当 i = 0时，string_permutation(‘c’)迭代，进入过程3(去看过程3)。
处理完进程3后返回到这里：
此时 j 只能取 ‘c’，所以temp_list = [s[0]+j] = [‘bc’]。

当i = 1时，string_permutation(‘b’)迭代，进入过程4(去看过程4)。
处理完过程4后返回到这里：
此时 j 只能取‘b’，所以temp_list = [‘bc’，‘cb’]，因为是append()哈。
所以过程2最终返回的temp_list是 [‘bc’，‘cb’]。

过程3：
s = ‘c’
s的长度为 1
满足迭代终止条件，所以string_permutation(‘c’)返回 [‘c’]

过程4：
s = ‘b’
s的长度为 1
满足迭代终止条件，所以string_permutation(‘b’)返回 [‘b’]
"""
