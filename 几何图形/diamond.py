#!/usr/bin/env python
# -*- coding:utf-8 -*-

import turtle as pic  # 导入turtle库

pic.bgcolor('black')  # 设置背景为黑色
pic.speed(1)  # 画笔速度
pic.pensize(2)  # 指定画笔宽度

for i in range(1, 5):
    pic.pencolor('white')  # 指定画笔颜色为白色
    pic.circle(46, steps = 3)  # 画圆 46为半径
    pic.circle(40, steps = 7)  # steps参数是7条边的内切正多边形
    pic.circle(30, steps = 6)
    pic.circle(26, steps = 5)
    pic.circle(20, steps = 4)
    pic.circle(20, steps = 3)
    pic.forward(20)  # 画笔前移

pic.backward(96)  # 画笔后退
pic.forward(48)  # 画笔前移
pic.right(180)  # 画笔顺时针旋转180°
pic.circle(72)  #画半径为72像素的圆
pic.penup()  # 抬笔函数
pic.goto(32, 24)  # 移动画笔
pic.pendown()  # 落笔函数
pic.circle(84)  #画半径为84像素的圆

pic.penup()  # 抬笔
pic.goto(-40, -230)  # 移动画笔
pic.pendown()  # 落笔
# write为写字函数，第一个参数为内容，第二个参数为字体
# 字体名称为黑体，字体大小为14像素，字体类型为normal
pic.write('首都经济贸易大学', font=('黑体',14,'normal'))
pic.hideturtle()  # 隐藏画笔的图形
pic.done()  # 关闭turtle库






