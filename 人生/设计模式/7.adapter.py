#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  time:2021/5/27

"""
适配器模式
    - 内容:将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作
    - 两种实现方式：
        - 类适配器：使得多继承
        - 对象适配器：使用组合
    - 角色：
        - 目标接口
        - 待适配的类
        - 适配器
    - 适用场景
        - 想使用一个已存在的类，而它的接口不符合你的要求
        - （对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口，对象适配器可以适配它的父类接口
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


class BankPay:
    def cost(self, money):
        print("银联支付%d元。" % money)


class ApplePay:
    def cost(self, money):
        print("苹果支付%d元。" % money)

# # 类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)


# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(ApplePay())
p.pay(100)







