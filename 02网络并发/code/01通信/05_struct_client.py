# sourcery skip: avoid-builtin-shadow
from socket import *
import struct


st = struct.Struct('i32sif')

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

addr = ('127.0.0.1',8888)
# 收发消息
while True:
    id = int(input('id:'))
    age = int(input('age:'))
    name = input('name:').encode()
    score = float(input('score:'))
    data = st.pack(id,name,age,score)
    if not data:
        break
    sockfd.sendto(data,addr)
    data,addr = sockfd.recvfrom(1024)
    print(data.decode())
    
    
# 关闭套接字
sockfd.close()