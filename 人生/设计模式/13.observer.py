#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/5/27

"""
观察者模式
    - 内容：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知
            并被自动更新，观察者模式又称“发布-订阅”模式
    - 角色：
        - 抽象主题
        - 具体主题
        - 抽象观察者
        - 具体观察者
"""

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):  # 抽象订阅者
    @abstractmethod
    def update(self, notice):  # notice是一个Notice类的对象
        pass


class Notice:  # 抽象发布者
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.reverse(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice):  # 具体发布者
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()  # 推送


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# client
notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司。。。号"
print(s1.company_info)
print(s2.company_info)






















