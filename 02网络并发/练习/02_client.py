from socket import*

sockfd = socket()
sockfd.connect(('127.0.0.1',8888))

with open('1.png','rb') as f:
    sockfd.send(f.read())
    

sockfd.close()