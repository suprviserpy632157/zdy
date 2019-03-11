from socket import *
from time import sleep
# 目标地址
dest = ('172.40.71.128',9999)
# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)
# 设置可以发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data = '''
   ****************
 千里姻缘一线牵，请你珍惜这段缘
   ****************
'''
while 1:
    sleep(1)
    s.sendto(data.encode(),dest)
s.close()