# unix_recv.py
from socket import *
import os
sock_file = './sock'  #原本没有这个文件

# 判断文件是否存在，存在就删除
if os.path.exists(sock_file):
    os.remove(sock_file)

# 创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

# 绑定套接字文件
sockfd.bind(sock_file)

# 监听，接收客户端连接
sockfd.listen(3)
while 1:
    c,addr = sockfd.accept()
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()