# -*- coding: utf-8 -*-
# @Time    : 2024/9/14 20:11
# @Author  : zfy
# @Site    : 
# @File    : 插入排序.py
# @Software: PyCharm 
# @Comment :

def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    insert_sort(nums)
    print(nums)
