# epoll_server.py
from socket import *
from select import *
# 创建套接字(要关注的IO)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8895))
s.listen(5)
# 创建epoll对象
p = epoll()
# 建立查找字典
fdmap = {s.fileno():s}
# 注册IO
p.register(s,EPOLLIN|EPOLLERR)
# 循环监控
while True:
    events = p.poll()  #阻塞(关注任意一个IO结束结束阻塞)
    # 遍历列表，处理IO
    for fd,event in events:
        if fd == s.fileno(): #说明s就绪
            # 处理IO
            c,addr = s.accept()  #或c，addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 添加新的注册IO
            p.register(c,EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()] = c
        elif event & EPOLLHUP:  #客户端断开
            print("客户端退出")
            p.unregister(fd)   #取消关注
            fdmap[fd].close()
            del fdmap[fd]      #从字典中删除
        elif event & EPOLLIN:  #返回空时，判定POLLIN就绪
            # 因为字典中每次都有保存之前的连接
            data = fdmap[fd].recv(1024)
            print("Receive:",data.decode())
            fdmap[fd].send(b"Receive your message")
s.close()

