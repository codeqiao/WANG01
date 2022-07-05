from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

addr = ('127.0.0.1',8888)
# 收发消息
while True:
    data = input('data:')
    if not data:
        break
    sockfd.sendto(data.encode(),addr)
    data,addr = sockfd.recvfrom(1024)
    print(data.decode())
    
    
# 关闭套接字
sockfd.close()