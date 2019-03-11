# udp_server.py
from socket import *
# 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
# 绑定地址
server_addr = ("0.0.0.0",8895)
sockfd.bind(server_addr)
# 消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print("Receive from %s:%s"%(addr,data.decode())) #%s将元组强转为字符串
    sockfd.sendto("Thanks for your message".encode(),addr)
# 关闭套接字
sockfd.close()
    
