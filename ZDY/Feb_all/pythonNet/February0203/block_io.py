# block_io.py
from socket import *
from time import sleep,ctime #打印经过n秒后的时间

sockfd = socket()
sockfd.bind(('0.0.0.0',2222))
sockfd.listen(3)

# 设置非阻塞状态
sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(10)

while 1:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError: #每隔2秒发一次
        sleep(2)
        print("%s connect error"%ctime())
        continue    #发一次回去看一次
    except timeout:
        print("timeout...")
    else:  # 有客户端连接，则执行以下内容
        print("Connect from:",addr)