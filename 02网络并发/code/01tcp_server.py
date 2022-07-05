"""
tcp_server.py   tcp套接字服务端流程
重点代码

注意：功能性代码，注重流程和函数使用
"""
import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8887))

# 设置监听
sockfd.listen(5)



# 收发消息
while True:
    # 阻塞等待链接
    print("Wait for connect...")
    connfd,addr = sockfd.accept()
    print(f"Connect form {addr} ...")

    while True:
        data = connfd.recv(1024)
        if not data:
           break
        print(f"收到：{data.decode()}")
        connfd.send(b'Thanks')
    connfd.close()

# 关闭套接字
sockfd.close()

