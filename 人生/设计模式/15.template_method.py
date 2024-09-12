#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/5/28

"""
模板方法模式
    - 内容：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中，模板方法使得子类可以不改变
            一个算法的结构即可重定义该算法的某些特定步骤
    - 角色：
        - 抽象类：定义抽象的原子操作；实现一个模板方法作为算法的骨架
        - 具体类：实现原子操作
"""
from abc import ABCMeta, abstractmethod
from time import sleep


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):  # 原子操作/钩子操作
        pass

    def run(self):  # 模板方法
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口结束运行")

    def repaint(self):
        print(self.msg)


MyWindow("Hello...").run()