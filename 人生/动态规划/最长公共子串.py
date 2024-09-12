#!/usr/bin/env python
# -*- coding:utf-8 -*-


def getMaxSubStr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    sb = ''  # 存放公共子串
    maxs = 0  # 记录最长公共子串的长度
    maxI = 0  # 记录最长公共子串最后一个字符的位置
    # 申请新的空间来记录公共子串长度信息 二维数组
    arr = [[0 for i in range(len1+1)] for j in range(len2+1)]
    # 利用递推公式填写新建的二维数组（公共子串的长度信息）
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                if arr[i][j] > maxs:
                    maxs = arr[i][j]
                    maxI = i
            else:
                arr[i][j] = 0
    # 找出公共子串
    i = maxI - maxs
    while i < maxI:
        sb = sb + str1[i]
        i += 1
    return sb


if __name__ == '__main__':
    str1 = 'abccade'
    str2 = 'dgcadde'
    print(getMaxSubStr(str1, str2))
