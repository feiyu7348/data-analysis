#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
建造者模式
    - 内容：将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示
    - 角色：
        - 抽象创建者
        - 具体创建者
        - 指挥者
        - 产品
    - 建造者模式和抽象工厂模式相似，也用来创建复杂对象，主要区别是建造者模式注重一步一步构建一个
        复杂对象，而抽象工厂模式注重多个系列的产品对象
"""
from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s %s %s %s" % (self.face, self.body, self.arm, self.leg)


class PlayBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "脸蛋"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = "胳膊"

    def build_leg(self):
        self.player.leg = "大长腿"


class Monster(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "怪兽胳膊"

    def build_leg(self):
        self.player.leg = "怪兽腿"


class PlayerDirector:  # 控制组装顺序
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client
builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)


print(p)

























