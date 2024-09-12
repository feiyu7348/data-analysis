# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/1 22:22


class Solution:
    def unique_paths_with_obstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0

        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


a = Solution()
b = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(a.unique_paths_with_obstacles(b))
