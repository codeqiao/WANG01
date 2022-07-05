"""
httpserver v1.0
基本要求：
1、获取来自浏览器的请求
2、判断如果请求内容是/ 将index.html返回给客户端
3、如果请求的是其他内容则返回404
"""

from socket import *
from urllib import response

def request(connfd:socket):
    # 获取请求将请求内容提取出来
    data = connfd.recv(4096)
    # 防止浏览器异常退出
    if not data:
        return
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]
    # 判断请求内容是不是/ 是则返回html 否则返回404
    if info == '/':
        with open('index.html','r') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response+="Content-Type:text/html\r\n"
        response+="\r\n"
        response+="<h1>Sorry....</h1>"
    # 发送给浏览器
    connfd.send(response.encode())

# 搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(3)

while True:
    connfd,addr = sockfd.accept()
    request(connfd) # 处理客户端