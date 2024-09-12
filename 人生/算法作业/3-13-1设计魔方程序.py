#!/usr/bin/env python
# -*- coding:utf-8 -*
# author:Zfy  date:2021/5/30 20:05


import numpy as np

# 构造魔方
s0 = np.zeros(9, dtype=np.int32).reshape(3,3)  # 第0面 正面
s1 = np.ones(9, dtype=np.int32).reshape(3,3)  # 第1面 右面
s2 = np.array([2 for _ in range(9)], dtype=np.int32).reshape(3,3)  # 第2面 后面
s3 = np.array([3 for _ in range(9)], dtype=np.int32).reshape(3,3)  # 第3面 左面
s4 = np.array([4 for _ in range(9)], dtype=np.int32).reshape(3,3)  # 第4面 上面
s5 = np.array([5 for _ in range(9)], dtype=np.int32).reshape(3,3)  # 第5面 下面

# 输出魔方
def print_cube():
    print("正面:{}".format(s0))
    print("右面:{}".format(s1))
    print("后面:{}".format(s2))
    print("左面:{}".format(s3))
    print("上面:{}".format(s4))
    print("下面:{}".format(s5))

# 1、面对正面（s0），左面（s3）逆时针2旋转
def left_rotate2():
    tmp = np.arange(3).reshape(3, 1)  # 临时数组
    for i in range(3):  # s0第一列存起来
        tmp[i][0] = s0[i][0]

    for i in range(3):
        s0[i][0] = s5[i][0]

    for i in range(3):
        s5[i][0] = s2[2-i][2]  # 注意2-i

    for i in range(3):
        s2[2-i][2] = s4[i][0]

    for i in range(3):
        s4[i][0] = tmp[i][0]

"""
实现全部旋转：
    - 魔方位置不变
    - 需要对六个面分别进行顺时针和逆时针旋转，总共需要十二个旋转函数
"""

# 2、面对正面（s0），左面（s3）顺时针1旋转
def left_rotate1():
    tmp = np.arange(3).reshape(3, 1)  # 临时数组
    for i in range(3):  # s0第一列存起来
        tmp[i][0] = s0[i][2]

    for i in range(3):
        s0[i][0] = s4[i][0]

    for i in range(3):
        s4[i][0] = s2[2-i][2]  # 注意2-i

    for i in range(3):
        s2[2-i][2] = s5[i][0]

    for i in range(3):
        s5[i][0] = tmp[i][0]

# 3、面对正面（s0），右面（s1）顺时针1旋转
def right_rotate1():
    tmp = np.arange(3).reshape(3, 1)  # 临时数组
    for i in range(3):  # s0第一列存起来
        tmp[i][0] = s0[i][2]

    for i in range(3):
        s0[i][2] = s5[i][2]

    for i in range(3):
        s5[i][2] = s2[2-i][0]  # 注意2-i

    for i in range(3):
        s2[2-i][0] = s4[i][2]

    for i in range(3):
        s4[i][2] = tmp[i][0]

# 4、面对正面（s0），右面（s1）逆时针2旋转
def right_rotate2():
    tmp = np.arange(3).reshape(3, 1)  # 临时数组
    for i in range(3):  # s0第一列存起来
        tmp[i][0] = s0[i][2]

    for i in range(3):
        s0[i][2] = s4[i][2]

    for i in range(3):
        s4[i][2] = s2[2-i][0]  # 注意2-i

    for i in range(3):
        s2[2-i][0] = s5[i][2]

    for i in range(3):
        s5[i][2] = tmp[i][0]

# 5、面对正面（s0），正面（s0）顺时针1旋转
def front_rotate1():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s4第三行存起来
        tmp[i] = s4[2][i]

    for i in range(3):
        s4[2][i] = s3[2-i][2]

    for i in range(3):
        s3[2-i][2] = s5[0][2-i]

    for i in range(3):
        s5[0][2-i] = s1[i][0]

    for i in range(3):
        s1[i][0] = tmp[i]

# 6、面对正面（s0），正面（s0）逆时针2旋转
def front_rotate2():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s4第三行存起来
        tmp[i] = s4[2][i]

    for i in range(3):
        s4[2][i] = s1[i][0]

    for i in range(3):
        s1[i][0] = s5[0][2-i]

    for i in range(3):
        s5[0][2-i] = s3[2-i][2]

    for i in range(3):
        s3[2-i][2] = tmp[i]

# 7、面对正面（s0），后面（s2）顺时针1旋转
def rear_rotate1():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s4第三行存起来
        tmp[i] = s4[0][i]

    for i in range(3):
        s4[0][i] = s1[i][2]

    for i in range(3):
        s1[i][2] = s5[2][2-i]

    for i in range(3):
        s5[2][2-i] = s3[2-i][0]

    for i in range(3):
        s3[2-i][0] = tmp[i]

# 8、面对正面（s0），后面（s2）逆时针2旋转
def rear_rotate2():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s4第三行存起来
        tmp[i] = s4[0][i]

    for i in range(3):
        s4[0][i] = s3[2-i][0]

    for i in range(3):
        s3[2-i][0] = s5[2][2-i]

    for i in range(3):
        s5[2][2-i] = s1[i][2]

    for i in range(3):
        s1[i][2] = tmp[i]

# 9、面对正面（s0），上面（s4）顺时针1旋转
def up_rotate1():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s0第一行存起来
        tmp[i] = s0[0][i]

    for i in range(3):
        s0[0][i] = s1[0][i]

    for i in range(3):
        s1[0][i] = s2[0][i]

    for i in range(3):
        s2[0][i] = s3[0][i-2]

    for i in range(3):
        s3[0][i-2] = tmp[i]

# 10、面对正面（s0），上面（s4）逆时针2旋转
def up_rotate2():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s0第一行存起来
        tmp[i] = s0[0][i]

    for i in range(3):
        s0[0][i] = s3[0][i-2]

    for i in range(3):
        s3[0][i-2] = s2[0][i]

    for i in range(3):
        s2[0][i] = s1[0][i]

    for i in range(3):
        s1[0][i] = tmp[i]

# 11、面对正面（s0），下面（s5）顺时针1旋转
def down_rotate1():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s0第三行存起来
        tmp[i] = s0[2][i]

    for i in range(3):
        s0[2][i] = s3[2][i - 2]

    for i in range(3):
        s3[2][i-2] = s2[2][i]

    for i in range(3):
        s2[2][i] = s1[2][i]

    for i in range(3):
        s1[2][i] = tmp[i]

# 12、面对正面（s0），下面（s5）逆时针2旋转
def down_rotate2():
    tmp = np.arange(3)  # 临时数组
    for i in range(3):  # s0第三行存起来
        tmp[i] = s0[2][i]

    for i in range(3):
        s0[2][i] = s1[2][i]

    for i in range(3):
        s1[2][i] = s2[2][i]

    for i in range(3):
        s2[2][i] = s3[2][i-2]

    for i in range(3):
        s3[2][i-2] = tmp[i]



if __name__ == '__main__':
    print_cube()  # 魔方初始值
    print("-----分割线-----")
    # left_rotate1()
    left_rotate2()
    # print_cube()
    print("-----分割线-----")
    # right_rotate2()
    # right_rotate1()
    # front_rotate1()
    # front_rotate2()
    # rear_rotate1()
    # rear_rotate2()
    # up_rotate1()
    # up_rotate2()
    down_rotate1()
    # down_rotate2()
    # print_cube()
    # left_rotate2()
    print_cube()








