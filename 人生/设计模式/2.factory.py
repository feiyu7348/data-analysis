#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
简单工厂模式
    - 内容：不直接向客户端暴露创建的实现细节，而是通过一个工厂类来复制创建产品类的实现
    - 角色：
        - 工厂角色
        - 抽象产品角色
        - 具体产品角色
    - 优点：
        - 隐藏了对象创建的实现细节
        - 客户端不需要修改代码
    - 缺点
        - 违反了单一职责原则，将创建逻辑集中到一个工厂类里
        - 当添加新厂品时，需要修改工厂类代码，违反了开闭原则
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print('花呗支付%d元.' % money)
        else:
            print("支付宝余额支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d元.' % money)


class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            return TypeError("No such payment named %s" % method)


# client
pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)












