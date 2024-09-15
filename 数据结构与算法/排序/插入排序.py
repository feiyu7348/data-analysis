# -*- coding: utf-8 -*-
# @Time    : 2024/9/14 20:11
# @Author  : zfy
# @Site    : 
# @File    : 插入排序.py
# @Software: PyCharm 
# @Comment :

def insert_sort(nums: list[int]):
    """插入排序"""
    # 外循环：已排序区间为 [0, i-1]
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        # 内循环：将 base 插入到已排序区间 [0, i-1] 中的正确位置
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]  # 将 nums[j] 向右移动一位
            j -= 1
        nums[j + 1] = base  # 将 base 赋值到正确位置


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    insert_sort(nums)
    print(nums)
