# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/1 22:03


class Solution:
    def unique_paths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


a = Solution()
print(a.unique_paths(3, 7))
