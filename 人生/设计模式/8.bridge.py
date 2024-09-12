#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  time:2021/5/27

"""
桥模式：
    - 内容：将一个事物的两个维度分离，使其都可以独立的变化
    - 角色：
        - 抽象
        - 细化抽象
        - 实现者
        - 具体实现者
    - 应用场景：
        - 当两个事物有两个维度上的表现，两个维度都可能扩展时
    - 优点
        - 抽象和实现相分离
        - 优秀的扩展能力
"""

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)


shape = Rectangle(Red())
shape.draw()
