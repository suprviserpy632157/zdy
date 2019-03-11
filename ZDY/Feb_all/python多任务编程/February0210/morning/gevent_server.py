# coding utf-8
# 主程序阻塞在accept,协程阻塞在recv
'''gevent monkey的使用'''
import gevent
from gevent import monkey
#执行脚本插件,修改原有阻塞行为
monkey.patch_socket()  
from socket import *
# 创建套接字
def server():
    s = socket()
    s.bind(("0.0.0.0",8895))
    s.listen(10)
    while True:
        c,addr = s.accept()
        print("Connect from",addr)
        # # 处理客户端请求
        # handle(c)
        gevent.spawn(handle,c) #协程方案
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()
server()
