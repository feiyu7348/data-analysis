# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/4 10:05


class Solution:
    def generateMatrix(self, n: int) :
        left, right, up, down = 0, n-1, 0, n-1
        matrix = [ [0]*n for _ in range(n)]
        num = 1
        while left<=right and up<=down:
            # 填充左到右
            for i in range(left, right+1):
                matrix[up][i] = num
                num += 1
            print(matrix)
            up += 1
            # 填充上到下
            for i in range(up, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            # 填充右到左
            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            # 填充下到上
            for i in range(down, up-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix


class Solution1:
    def generateMatrix(self, n: int):
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat


s = Solution()
print(s.generateMatrix(3))
