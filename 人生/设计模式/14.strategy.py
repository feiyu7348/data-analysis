#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/5/28

"""
策略者模式
    - 内容：定义一系列的算法，把他们一个个封装起来，并且使他们可相互替换，本模式使得算法可独立于使用他的客户而变化
    - 角色：
        - 抽象策略
        - 具体策略
        - 上下文
"""

from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


class Context:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# client
data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()


