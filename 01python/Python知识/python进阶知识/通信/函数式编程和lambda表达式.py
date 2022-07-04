"""
找出0-10000中能被4，7，9，11, 111整除的数

lambda 是天然的实参

思考：这样的代码满足分而治之，低耦合，可扩展性强
"""
import sys
sys.path.append("./../")
from common.list_help import ListHelper


# 变化的 "封装"
def find_2(item:int):
    return item%2 == 0

def find_7(item:int):
    return item%7 == 0

def find_9(item:int):
    return item%9 == 0

def find_11(item:int):
    return item%11 == 0

def find_111(item:int):
    return item%111 == 0

# 不变的 “继承”
# def find(list1:list,find_way):
#     for item in list1:
#         if find_way(item):
#             yield  item

#lambda表达式
def func01():
    return 100
a = lambda :100

def func02(p1,p2):
    return p1>p2
a1 = lambda p1,p2:p1>p2

def func03(p1):
    print("参数是：",p1)
a2 = lambda p1:print("参数是：",p1)


if __name__ == "__main__":
    list1 = list(range(1,10000,100))
    generator = ListHelper.find_all(list1,lambda item: item%111 == 0)
    for item in generator:
        print (item)
    # 此处的item就是列表中的元素
    print(ListHelper.find_single(list1,find_111))
    print(ListHelper.is_exists(list1,lambda p1: p1 == 0))
    print(ListHelper.get_count(list1,lambda item:item == 1))
    print(ListHelper.sum(list1,lambda item:item)) 