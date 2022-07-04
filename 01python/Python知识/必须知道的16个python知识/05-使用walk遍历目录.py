
"""
os模块中的walk的功能
walk能遍历出文件夹中的所有文件夹，文件
    返回的是一个迭代器
"""
import os

for temp in os.walk("./"):
    print("-"*30)
    print(type(temp))
    print(temp)


"""
('./', ['必须知道的16个python知识'], ['test.txt'])
第一个：　表示当前的路径
第二个：　当前文件夹中的文件夹
第三个：　当前文件夹中的文件
"""   