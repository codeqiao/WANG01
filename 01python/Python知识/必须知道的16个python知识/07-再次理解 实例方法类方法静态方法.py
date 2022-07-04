'''
encoding: utf-8
@Description:       
@Date:       2022/06/08 12:45:00
@Author:     Wang
'''

"""
    用到类属性就用类方法
    用到实例属性就用实例方法
    都没有就用静态方法

    静态方法和类方法都可以用类名直接调用

    类中的函数有self参数就表示可以通过实例对象进行操作
    类属性，所有的实例对象都共享
    类属性需要用类方法来调用

    实例属性：都用self调用
    类属性： 都用cls调用
"""

import time

from lib2to3.pytree import Node


class Tool(object):
    
    num = 0  # 类属性 可以通过类名来访问

    def __init__(self, name) -> None:
        # self是专门用来保存刚刚创建出来的那个对象的
        self.name = name
        Tool.num+=1

    #　实例方法
    # def print_num(self) -> None:
    #     print(Tool.num)

    # 类方法，需要用类的名字来调用
    @classmethod
    def print_num(cls) -> None:
        print(cls.num)

    @staticmethod
    def print_static() -> None:
        print("我是静态方法")

#　创建实例化对象
t = Tool("锄头") 
t2 = Tool("镰刀")
Tool.print_static()

class TimeTest(object):

    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def show_time() -> None:
        print(f'当前的时间是{time.strftime("%H:%M:%S", time.localtime())}')

t = TimeTest(22,33,44)
t.show_time()