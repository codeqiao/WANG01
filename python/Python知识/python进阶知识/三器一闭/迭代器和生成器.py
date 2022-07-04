'''
Author: CodeQi 2063520993@qq.com
Date: 2021-11-03 13:36:41
LastEditors: CodeQi 2063520993@qq.com
LastEditTime: 2022-06-13 21:43:01
FilePath: \python\python进阶知识\三器一闭\迭代器和生成器.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from enum import IntEnum
import time
import sys
#迭代器的要有__next__()方法 可迭代对象要有 __iter__()方法

class Shape:
    pass

class ShapeManager:
    def __init__(self):
        self.__shape_list = []
    def append(self,shape:Shape):
        "在末尾添加图形"
        self.__shape_list.append(shape)

    def generate(self):
        for shape in self.__shape_list:
            yield shape

# 用生成器得到一个列表里面的偶数
def get_ou1(list1):
    """正常浪费内存"""
    result = []
    for i in list1:
        if i%2 == 0:
            result.append(i)
    return result

def get_ou(list1):
    """使用生成器"""
    for i in list1:
        if i%2 == 0:
            yield i

def my_enumerate(iterable_targets):
    index = 0
    for item in iterable_targets:
        yield (index,item)
        index+=1

def my_zip(*args):
    index = 0
    length_min =  sys.maxsize
    for item in args:
        length = len(item)
        if length<length_min:
            length_min = length
    for i in range(length_min-1):
        list_result = []
        for item in args:
           list_result.append(item[i])
        yield tuple(list_result)
    
    
if __name__ == '__main__':
    list1 = []
    for i in range(0,10000000):
        list1.append(i)
    time_start =  time.time()
    for i in get_ou(list1):#此时不执行get_ou的函数体，而是生成生成器对象
        pass
        
    time_end = time.time()
    print(time_end-time_start)

    time_start =  time.time()
    for i in get_ou1(list1):
        pass
    time_end =  time.time()
    print(time_end-time_start)


    shape_manager = ShapeManager()
    for i in range(0,10):
        shape_manager.append(Shape())

    for shape in shape_manager.generate():
        print(shape)

    print(enumerate(list1))
    print(my_enumerate(list))

    for item in my_zip(range(1,200),range(3,400)):
        print(item)
        

    list2 = [1,2,'sad',False,1.25]
    #拿到整数
    re = (item for item in list2 if type(item) == int)
    for item in re:
        print(item)
    
    re1 = [item for item in list2 if type(item) == int]
    for item in re1:
        print(item)

