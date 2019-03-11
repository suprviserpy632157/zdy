# tcp_server.py 连接一个客户端（连接多个客户端讲了进程线程后继续）
import socket
# 创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定地址(元组(ip,port))
sockfd.bind(('0.0.0.0',4444))
# 设置监听
sockfd.listen(5)
while 1:
    # 等待处理客户端连接
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept() #自动完成三次握手(阻塞，等待客户端响应) 
    except KeyboardInterrupt:
        print("Server exit")
        break
    print("Connect from",addr)  #客户端地址
    while 1:
        # 消息收发(使用新产生的与客户端连接的套接字,先发后收)
        data = connfd.recv(1024) #recv中参数表示接受数据字节的大小
        if not data:   #收到消息是空就退出
            break
        print("Receive message:",data.decode())
        n = connfd.send(b"Receive your message") #send中参数类型必须为bytes
        # n = connfd.send("Receive your message".encode())
        print("Send %d bytes"%n)
    # 关闭客户端的套接字
    connfd.close()
# 关闭套接字
sockfd.close()  #自动完成四次挥手
