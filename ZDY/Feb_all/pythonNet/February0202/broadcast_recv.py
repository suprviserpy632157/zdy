from socket import * 
# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)
# 设置可以接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1) #1是bool值
# 选择一个接收地址
s.bind(('0.0.0.0',8888))
while 1:
    try:
        msg,addr = s.recvfrom(2048)
        print("从%s接收广播：%s"%(addr,msg.decode()))
    except KeyboardInterrupt:
        break
    except Exception as e:
        print("error:",e)

s.close()