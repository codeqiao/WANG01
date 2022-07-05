"""
tcp_client.py   tcp客户端流程
重点代码
"""
from socket import *

# 创建tcp套接字
sockfd = socket() # 使用默认参数 -> tcp套接字

# 连接
sockfd.connect(('127.0.0.1',8887))

# 收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("Server:",data.decode())

# 关闭
sockfd.close()

