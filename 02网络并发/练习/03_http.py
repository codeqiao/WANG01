from socket import *

sockfd = socket()
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(5)

while True:
    confd,addr = sockfd.accept()
    print(f"Connert from {addr}")
    data = confd.recv(4096)
    print(data)

    response = """HTTP/1.1 200 OK
    Content-Type:text/html

    <h1>Hello World</h1>
    """
    confd.send(response.encode())
    confd.close()

sockfd.close()
