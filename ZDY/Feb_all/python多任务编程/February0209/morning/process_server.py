from socket import *
from multiprocessing import Process
import sys
import signal

HOST = '0.0.0.0'
PORT = 8895
ADDR = (HOST,PORT)

# 客户端处理函数
def handle(c):
    print("Connect from",c.getpeername())
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
    # 子进程退出
    sys.exit(0)

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# 循环等待客户端连接
while 1:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        # 主进程结束
        s.close()
        break
    except Exception as e:
        print(e)
        continue
    
    # 创建子进程处理客户端请求,此处可以不传c
    p = Process(target=handle,args=(c,))
    #让子进行随主线程退出
    p.daemon = True 
    p.start()