#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  time:2021/5/27

"""
组合模式：
    - 内容：将对象组合成树形结构，以表示“部分-整体”的层次结构，组合模式使得用户对单个对象和组合对象的使用具有一致性
    - 角色：
        - 抽象组件
        - 叶子组件
        - 复合组件
        - 客户端
    - 适用场景：
        - 表示对象的“部分-整体”层次结构（特别是结构是递归的）
        - 希望用户忽略组合对象和单个对象的不同，用户统一的使用组合结构中的所有对象
    - 优点：
        - 定义了包含基本对象和组合对象的类层次结构
        - 简化客户端代码，即客户端可以一致的使用组合对象和单个对象
        - 更容易增加新类型的组件
"""
from abc import ABCMeta, abstractmethod


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s %s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


# 叶子节点
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段(%s %s)" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 符合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("-----复合图形-----")
        for g in self.children:
            g.draw()
        print("-----复合图像-----")


l = Line(Point(1,1), Point(2,2))
print(l)

