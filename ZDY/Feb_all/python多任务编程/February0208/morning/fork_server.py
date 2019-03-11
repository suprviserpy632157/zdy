# fork_server.py
# 基于fork的并发模型
from socket import *
import os,sys
import signal

# 客户端处理函数,想占有多久就占有多久,因为会创建新的进程
def client_handle(c):
    print("客户端:",c.getpeername())
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive message')
    c.close()
# 创建监听套接字
HOST = '0.0.0.0'
PORT = 8895
ADDR = (HOST,PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
# 提示
print("Listen to the port 8895...")

# 循环等待客户端连接
while 1:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("Error:",e)
        continue
    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        # 子进程若不关闭s可能会通过属性对父进程中的s造成影响
        s.close()
        # 由于s关闭,并且不希望子进程继续循环
        client_handle(c) #处理客户端请求
        os._exit(0)     #子进程直接退出
    # 父进程或创建进程失败,都是循环接收新的连接
    else:
        # 父进程只需要连接不需要交互,所以c对他没有,可以直接关闭
        c.close()

