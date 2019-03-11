# 使用select完成一个服务程序，要求将从客户端发来的信息写入到一个文件中，
# 同时监控服务端的终端输入，将输入内容也写入该文件
from socket import *
from select import select
from sys import stdin
from time import ctime
# 创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",3333))
s.listen(5)

# 日志文件(以a（添加）的方式打开)
f = open("day3.txt","a")

# 添加到关注列表
rlist = [s,sys.stdin]
wlist = []
xlist = []
# 循环监控
while 1:
    # 监控关注的IO(死等，不做超时检测)
    rs,ws,xs = select(rlist,wlist,xlist)
    # 循环遍历返回值列表，确定就行的IO
    for r in rs:
        # s就绪，有客户端请求连接
        if r is s:
            c,addr = s.accept() #r.accept()也可以，此时r,s一样 
            # 将客户端连接套接字加入关注
            rlist.append(c)
        if r is sys.stdin:
            f.write("%s %s"%(ctime(),r.readline())
            f.flush()
        #某个客户端发信息则c就绪
        else:  
            data = c.recv(1024)
            if not data:  #当客户端回车时，回复一次空
                rlist.remove(r)  # 此时的空无需关注，直接移除
                continue #退出本次for循环，进行下一次for循环
            f.write("%s %s\n"%(ctime(),data.decode())
            f.flush()
            # print("Receive:",data.decode())
            
    #         f.close()
    #         # 当r放入wlist表示希望主动操作r这个IO
    #         wlist.append(r)
    #         wlist.append(stdin)

    # # 如果wlist有IO则会立即返回ws
    # for w in ws:
    #     w.send(b"OK")
    #     f1 = open("day3.txt","wb")
    #     f1.write(data)
    #     f1.close()
    #     # 回复玩之后立即删除，否则回进入死循环
    #     # 只要有另一个客户端发送信息，就会进行一次回复
    #     wlist.remove(w)
    # for x in xs:
    #     pass