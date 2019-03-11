# unix_send.py
from socket import *
# 确保两边使用同一个套接字文件
sock_file = "./sock"

# 创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)
sockfd.connect(sock_file)

while 1:
    msg = input(">>")
    if not msg:
        break
    # 消息收发
    data = sockfd.send(msg.encode())

sockfd.close()
