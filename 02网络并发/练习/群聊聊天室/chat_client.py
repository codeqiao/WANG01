"""
客户端
"""
from socket import*
import sys,os

ADDR = ('127.0.0.1',8888)

# 循环发送消息
def send_msg(sockfd:socket,name:str):
    while True:
        try:
            text = input("Msg>> ")
        except KeyboardInterrupt:
            text='quit'
        if text.strip() == 'quit':
            msg = f'Q {name}'
            sockfd.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")

        msg = f'C {name} {text}'
        sockfd.sendto(msg.encode(),ADDR)

# 循环接受消息
def recv_msg(sockfd:socket):
    while True:
        try:
            data,addr = sockfd.recvfrom(1024)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode()=='EXIT':
            sys.exit()
        print(data.decode(),"\nMsg>> ",end='')

# 向服务器发出请求
def do_request(sockfd:socket):
    while True:
        name = input("name: ")
        msg = f'L {name}'
        sockfd.sendto(msg.encode(),ADDR)
        # 接受反馈
        data,addr = sockfd.recvfrom(128)
        if data.decode()=='OK':
            print("您已经成功进入聊天室")
            break
        else:
            print(data.decode())
    
    # 已经进入到聊天室当中
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(sockfd,name)  # 子进程不断的发消息
    else:
        recv_msg(sockfd)  # 父进程不断的收消息

#客户端请求函数
def main():
    sockfd = socket(AF_INET,SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    do_request(sockfd)  


main()