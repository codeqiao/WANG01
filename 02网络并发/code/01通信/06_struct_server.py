from socket import*
import struct

st = struct.Struct('i32sif')

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
# 绑定地址
sockfd.bind(('0.0.0.0',8888))

# 收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    id,name,age,score = st.unpack(data)
    name = name.decode()
    score = round(score,1)
    print(id,name,age,score)
    sockfd.sendto(b"Thanks",addr)
    
# 关闭套接字
sockfd.close()