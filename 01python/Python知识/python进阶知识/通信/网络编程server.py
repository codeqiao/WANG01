import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockfd.bind(('0.0.0.0', 8888))

sockfd.listen(10)

print ('Waiting for connect...')
connfd,addr = sockfd.accept()

print("Connect from",addr)


data = connfd.recv(1024)
print("收到",data)
n = connfd.send(b'Thanks')

print("发送了%d个字节"%n)

#关闭套接字
connfd.close()
sockfd.close()





