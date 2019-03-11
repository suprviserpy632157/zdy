# tcp_client.py
from socket import *
# 创建套接字
sockfd = socket()
# 发起连接
server_addr = ('127.40.71.193',8895)
sockfd.connect(server_addr)
while 1:
    # 消息收发(先发后收)
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server:",data.decode())
# 关闭套接字
sockfd.close()
