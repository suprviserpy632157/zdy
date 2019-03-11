from socket import *
s = socket()
s.connect(('127.0.0.1',8888))
f = open('1.JPG','rb')
while 1:
    data = f.read(1024)
    if not data:
        break
    s.send(data) #data正好是bytes格式
f.close()
s.close()