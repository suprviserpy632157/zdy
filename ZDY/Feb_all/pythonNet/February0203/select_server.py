from socket import *
from select import select
# 创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",3333))
s.listen(5)

# 添加到关注列表
rlist = [s]
wlist = []
xlist = []

while 1:
    # 监控关注的IO
    rs,ws,xs = select(rlist,wlist,xlist)
    # 循环遍历返回值列表，确定就行的IO
    for r in rs:
        # s就绪，有客户端请求连接
        if r is s:
            c,addr = s.accept() #r.accept()也可以，此时r,s一样
            print("Connect from",addr)
            # 将客户端连接套接字加入关注
            rlist.append(c)
        #某个客户端发信息则c就绪
        else:  
            data = r.recv(1024)
            if not data:  #当客户端回车时，回复一次空
                rlist.remove(r)  # 此时的空无需关注，直接移除
                r.close()
                continue #退出本次for循环，进行下一次for循环
            print("Receive:",data.decode())
            # r.send(b"OK")  #回信息(可以不发送)

            # 当r放入wlist表示希望主动操作r这个IO
            wlist.append(r)

    # 如果wlist有IO则会立即返回ws
    for w in ws:
        w.send(b"收到!老铁!")
        # 回复玩之后立即删除，否则回进入死循环
        # 只要有另一个客户端发送信息，就会进行一次回复
        wlist.remove(w)
    for x in xs:
        pass