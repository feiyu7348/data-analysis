#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
SOLID原则：
    - 开放封闭原则
    - 里氏替换原则
    - 依赖倒置原则
    - 接口隔离原则
    - 单一职责原则
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Aipay(Payment):
    def pay(self, money):
        print('支付宝支付%d元.' % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d元.' % money)


p = Aipay()
p.pay(100)
