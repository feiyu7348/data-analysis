# -*- coding: utf-8 -*-
# @Time    : 2024/9/14 20:17
# @Author  : zfy
# @Site    : 
# @File    : 快速排序.py
# @Software: PyCharm 
# @Comment :

def quick_sort(nums: list[int]):
    n = len(nums)
    if n <= 1:
        return nums

    pivot = nums[0]
    left = [nums[i] for i in range(1, n) if nums[i] < pivot]
    right = [nums[i] for i in range(1, n) if nums[i] >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(quick_sort(nums))
