from socket import *
from threading import Thread

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
    # 线程不能写sys.exit()

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

# 循环等待客户端连接
while 1:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        # 主线程结束
        s.close()
        break
    except Exception as e:
        print(e)
        continue
    
    # 创建线程处理客户端请求
    t = Thread(target=handle,args=(c,))
    #让分支线程随主线程退出
    t.setDaemon(True) 
    t.start()
    # 不能join(),主线程不能轻易退出