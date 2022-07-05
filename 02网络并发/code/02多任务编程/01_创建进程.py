"""
fork 创建进程演示
"""
import os

pid = os.fork()
if pid<0:
    print("创建失败")
elif pid == 0:
    print("这是新进程")
else:
    print('这个是老进程')