# -*- coding: utf-8 -*-
# @Time    : 2024/9/14 14:10
# @Author  : zfy
# @Site    : 
# @File    : 二分查找.py
# @Software: PyCharm 
# @Comment :

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(s.search(nums, target))
