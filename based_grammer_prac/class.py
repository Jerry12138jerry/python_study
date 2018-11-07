#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 17:32
# @Author  : Jerry
# @Site    : 
# @File    : class.py
# @Software: PyCharm

# 继承
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

class Child(Person):
    def __init__(self, name, sex, mother, father):
       Person.__init__(self, name, sex)
       self.mother = mother
       self.father = father

May = Child("May", "female", "April", "June")
print(May.mother, May.father)

# 多态
class Screen(object):
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, valuer):
        if not isinstance(valuer, int):
            raise ValueError()
        if valuer < 0:
            raise ValueError()
        self.width = valuer

    @property
    def height(self):
        return self.height

    @width.setter
    def height(self, valuer):
        if not isinstance(valuer, int):
            raise ValueError()
        if valuer < 0:
            raise ValueError()
        self.height = valuer

s = Screen
s.width = 3
s.height = 400
print(s.width,s.height)