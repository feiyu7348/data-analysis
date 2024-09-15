# -*- coding: utf-8 -*-
# @Time    : 2024/9/14 19:51
# @Author  : zfy
# @Site    : 
# @File    : 选择排序.py
# @Software: PyCharm 
# @Comment :

def select_sort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums


def select_sort1(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(select_sort1(nums))
