#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

def compettion(n, mymat):
    if n == 2:
        mymat[0, 0] = 1
        mymat[0, 1] = 2
        mymat[1, 0] = 2
        mymat[1, 1] = 1
        return  # 分治迭代至只有2名运动员
    # if n%2==1:n+=1#奇数
    # t=int(n/2)
    if n % 2 == 1:
        t = int((n + 1) / 2)
        n += 1
    else:
        t = int(n / 2)
    compettion(t, mymat)  # 分治迭代
    # 在原先的基础上，扩展矩阵
    if n % 4 == 0:  # 除以2为偶数个运动员
        for i in range(int(n / 2)):
            for j in range(int(n / 2)):
                thevalue = mymat[i][j]
                mymat[i + t][j] = thevalue + t
                mymat[i][j + t] = thevalue + t
                mymat[i + t][j + t] = thevalue
    else:  # 除以2为奇数个运动员
        for i in range(int(n / 2)):  # 截取部分子问题的解
            for j in range(int(n / 2) + 1):
                thevalue = mymat[i][j]
                if thevalue > t:  # 子问题中假设出的选手
                    ##用以下两行解决奇数个运动员时矩阵的左半部分
                    mymat[i + t][j] = i + 1  ##########################下左假设部分恰好为i+1
                    mymat[i][j] = i + t + 1  # 新假设出的选手处正好为i+t+1
                    ##需要处理矩阵k列开始的右半部分
                    c = i + t + 2  # 第一个是5
                    k = int(n / 2) + 1  # 第一个是4
                    while k < n:
                        if c > n:
                            c -= t
                        # if(c==i+t)  c++;
                        mymat[i][k] = c  # 右
                        mymat[c - 1][k] = i + 1  # 右下
                        c += 1
                        k += 1
                else:
                    mymat[i + t][j] = thevalue + t  # 向下延拓
    return mymat


#################################################################
def main():
    a = int(input("输入需要进行循环赛的人数:"))
    if a % 2 == 0:  # 运动员人数为偶数
        b = np.zeros([a, a])
        compettion(a, b)
    else:  # 运动员人数为奇数
        b = np.zeros([a + 1, a + 1])
        compettion(a + 1, b)
        for i in range(a + 1):
            for j in range(a + 1):
                if b[i][j] > a:
                    b[i][j] = 0
                if i == a: b[i][j] = 0
    print(b)


if __name__ == '__main__':
    main()