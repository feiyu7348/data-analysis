#!/usr/bin/env python
# -*- coding:utf-8 -*-


def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    arr = [[0 for _ in range(len2+1)] for _ in range(len1+1)]  # len1+1行，len2+1列
    b = [[0 for _ in range(len2+1)] for _ in range(len1+1)]  # 用于记录字符位置 1 左上方 2 上方 3 左方
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:  # i j位置上的字符匹配的时候，来自于左上方+1
                arr[i][j] = arr[i-1][j-1] + 1
                b[i][j] = 1
            elif arr[i-1][j] > arr[i][j-1]:  # 来自于上方
                arr[i][j] = arr[i-1][j]
                b[i][j] = 2
            else:  # 来自左方
                arr[i][j] = arr[i][j-1]
                b[i][j] = 3
    return arr[-1][-1], b

def lcs_traceback(x, y):  # 回溯
    arr, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 来自于左上方 匹配
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自于上方 不匹配
            i -= 1
        else:
            j -= 1  # 来自于左方 不匹配
    return ''.join(reversed(res))


if __name__ == '__main__':
    str1 = 'BDCABA'
    str2 = 'ABCBDAB'
    print(lcs_traceback(str1, str2))
