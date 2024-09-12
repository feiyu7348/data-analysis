#!/usr/bin/env python
# -*- coding:utf-8 -*-


import random


random.seed(1000)
arr = [random.randint(0,1000) for _ in range(100000)]  # 随机生成一万个0到1000之间的数

b = []  # 存放数据

while len(arr) > 0:
    a = arr.pop(0)  # 删除第一个变量赋给新列表a
    count = arr.count(a) + 1  # 计算总数
    for i in range(count - 1):  # 删除arr中的相同元素
        arr.remove(a)
    b.append([a, count])  # 存起来，a为数字，count为出现次数


# 输出数字和个数
# for i in range(len(b)):
#     print("{}有{}个".format(b[i][0], b[i][1]))
'''
# 快速排序
def partition(arr, left, right):
    # 归位操作，left，right 分别为数组左边和右边的位置索引
    tmp = arr[left]
    while left < right:
        while left < right and arr[right] >= tmp:  # 从右边找比 tmp 小的数，如果比 tmp 大，则移动指针
            right -= 1                             # 将指针左移一个位置
        arr[left] = arr[right]                     # 将右边的值写到左边的空位上
        while left < right and arr[left] <= tmp:   # 从左边找比 tmp 大的数，如果比 tmp 小，则移动指针
            left += 1                              # 将指针右移一个位置
        arr[right] = arr[left]                     # 将左边的值写到右边的空位上
    arr[left] = tmp                                # 把 tmp 归位
    return left                   # 返回 left，right 都可以，目的是便于后面的递归操作对左右两部分进行排序

def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        # print(arr)                         # 每次归位后打印一次
        quick_sort(arr, left, mid-1)       # 对左半部分进行归位操作
        quick_sort(arr, mid+1, right)      # 对右半部分进行归位操作
'''
# 获取b中数字的个数 后面进行排序
array = []
for i in range(len(b)):
    array.append(b[i][1])

array.sort(reverse=True)  # 内hi函数sort使用Timsort算法
# print(array)

# 打印
for n in list(reversed(list(set(array)))):  # 集合去重打印
    for i in range(len(b)):
        if b[i][1] == n:
            print("{}有{}个".format(b[i][0], n))



