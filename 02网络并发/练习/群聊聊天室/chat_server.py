from socket import*
import os,sys

"""
全局变量：很多封装模块都要用或者有固定的含义
"""

ADDR = ('0.0.0.0',8888) #服务器地址
USERS = {}

# 处理退出请求
def do_exit(sockfd:socket,name):
    msg = f"\n管理员：{name}退出群聊"
    sockfd.sendto('EXIT'.encode(),USERS[name])
    del USERS[name]
    for addr in USERS.values():
        sockfd.sendto(msg.encode(),addr)

# 处理聊天请求
def do_chat(sockfd:socket,name:str,text:str):
    msg = f"\n{name}: {text}"
    for n,addr in USERS.items():
        if n != name:
            sockfd.sendto(msg.encode(),addr)

# 处理登录请求
def do_login(sockfd:socket,name,address):
    if name not in USERS:
        sockfd.sendto('OK'.encode(),address)
        msg = f"\n欢迎'{name}'进入聊天室"
        for addr in USERS.values():
            sockfd.sendto(msg.encode(),addr)
        USERS[name]=address
    else:
        sockfd.sendto("\n该用户名已存在".encode(),address)

# 循环接受请求
def do_request(sockfd:socket):
    while True:
        data,addr = sockfd.recvfrom(1024)
        tmp = data.decode().split(' ')
        if tmp[0]=="L":
            do_login(sockfd,tmp[1],addr)  #执行登录工作
        if tmp[0]=='C':
            text = ''.join(tmp[2:])
            name = tmp[1]
            do_chat(sockfd,name,text)
        if tmp[0]=='Q':
            do_exit(sockfd,tmp[1])

# 搭建网络
def main():
    sockfd = socket(AF_INET,SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        while True:
            text = input("Msg>> ")
            msg = f'C 管理员 {text}'
            sockfd.sendto(msg.encode(),ADDR)
    else:
        # 请求处理函数
        do_request(sockfd)


main()