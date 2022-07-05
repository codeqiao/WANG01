from socket import*

sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)
connfd,addr = sockfd.accept()

with open('2.png','wb') as f:
    data = connfd.recv(1024)
    while data:
        f.write(data)
        data = connfd.recv(1024)

connfd.close()
sockfd.close()