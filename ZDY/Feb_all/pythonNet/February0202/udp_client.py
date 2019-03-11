# udp_client.py
from socket import *
# 服务器地址
HOST = '172.40.71.128'
PORT = 8888
ADDR = (HOST,PORT)
# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
# 收发消息
while True:
    data = input("Msg>>")
    if not data:
        break    
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("Receive from server:",msg.decode())
# 关闭套接字
sockfd.close()