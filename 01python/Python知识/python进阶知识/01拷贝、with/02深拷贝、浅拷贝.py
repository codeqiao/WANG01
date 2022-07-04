"""
总结：
拷贝其实很简单，只是有时仅仅是最顶层的那个引用拷贝了，有时又编程了递归拷贝，到底用哪种？
简单来说，如果浅拷贝能用则用，否则再用深拷贝，这样节省内存


1. 目的
现在有个需求，遍历当前程序的文件夹，获取到所有文件，然后调用了一个函数对这些文件简单的测试了一下

浅拷贝：对于一个对象的顶层拷贝
通俗的理解是：拷贝了引用，并没有拷贝内容

深拷贝：对于一个对象所有层次的拷贝(递归)

"""



#代码简单的测试如下：

import os
import copy


def count_file(files):
    """
    测试列表中，非隐藏文件的个数
    :param files:
    :return:
    """
    # 4. 提出隐藏文件名
    temp = ""
    for temp in files:
        if temp.startswith("."):
            files.remove(temp)

    # 5. 排序打印测试
    files.sort()
    for file in files:
        print(file)


# 1. 遍历出当前文件夹中所有的文件
file_names = os.listdir(".")

print("-" * 30)

# 2. 打印所有的文件名
for file in file_names:
    print(file)

print("-" * 30)

# 2. 调用一个函数，用来测试除了隐藏文件之外的文件的个数
count_file(file_names)

print("-" * 30)

# 3. 打印所有的文件名
for file in file_names:
    print(file)




"""
6.1 浅拷贝对不可变类型和可变类型的copy不同
copy.copy对于可变类型，会进行浅拷贝
copy.copy对于不可变类型，不会拷贝，仅仅是指向

"""
s = [1,3,4,5,[234,[1,2,2],3,4,23,2,2]]

s1 = copy.copy(s)

print(id(s))
print(id(s1))
