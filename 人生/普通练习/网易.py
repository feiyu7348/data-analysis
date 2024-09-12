# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/18 19:02

def func(n, a, b, g):
    dp = [[a for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if g[i][0] == '.':
            dp[i][0] = 0
        elif g[i][0] == '#':
            break
        if g[0][i] == '.':
            dp[0][i] = 0
        elif g[0][i] == '#':
            break

    for i in range(0, n, -1):
        for j in range(0, n, -1):
            if g[i][j] == '*':
                dp[i][j] = b
                break
        break

    for i in range(1, n):
        for j in range(1, n):
            if g[i][j] == '#':
                dp[i][j] = a + min(dp[i - 1][j], dp[i][j - 1])
            if g[i][j] == '.':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
            if dp[i][j] == b:
                dp[i][j] = b
    print(dp)
    return dp[-1][-1]


n, a, b = map(int, input().split())
g = []
for i in range(n):
    g.append([i for i in input()])

print(func(n, a, b, g))
