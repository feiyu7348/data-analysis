#!/usr/bin/env python
# -*- coding:utf-8 -*

class Solution:
    """最大和的连续子数组"""
    def maxSubArray(self , A ):
        # write code here
        res = []
        _index = []
        for i in range(len(A)):
            if A[i] > 0:
                res.append(A[i])
                _index.append(i)
                break
        for i in range(_index[-1], len(A)):
            if A[i] <= 0:
                continue
            else:
                if sum(A[_index[-1]+1: i+1]) > 0:
                    res.append(sum(A[_index[-1]+1: i+1]) + res[-1])
                    _index.append(i)
        return res[-1]


s = Solution()
A = [-2, 0, -3, 4, -2, 2, 2, -5, 4]
print(s.maxSubArray(A))
