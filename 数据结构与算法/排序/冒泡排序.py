# -*- coding: utf-8 -*-
# @Time    : 2024/9/14 15:46
# @Author  : zfy
# @Site    : 
# @File    : 冒泡排序.py
# @Software: PyCharm 
# @Comment :

def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n-1):
        flag = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True

        if not flag:
            break
    return nums


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(bubble_sort(nums))
