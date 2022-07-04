# 1、为什么要用文件？
# 如果一个程序中的某些数据，恰巧这些数据比较重要，当程序关闭后仍需保留这些数据
# 那么此时我们就可以使用到文件，下次重启后就可以用到这些数据

# 2、什么是文件
# 例如：txt、mp3

# 3、文件的特点
# 他们存储在U盘、硬盘的设备上。

# 4、操作文件的基本流程

## 4.1 写入数据
"""
    w是write的缩写
    wb是写入二进制
"""
with open("test.txt",'w',encoding='utf-8') as f:
    f.write("Hello World!")


## 4.2 读取数据
with open("test.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)

"""
注意：
    1、写入数据和读取数据分开，尽量不要用一个实例化对象既读又写
"""