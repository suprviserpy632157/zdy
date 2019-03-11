from socket import *
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

f = open("2.BMP",'wb') #二进制方式打开
while 1 :
    data = c.recv(1024) #循环接收，每次接收1024
    if not data:
        break
    f.write(data)
f.close()
c.close()
s.close()