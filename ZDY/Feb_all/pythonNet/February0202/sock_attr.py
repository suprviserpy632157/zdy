from socket import *
# 创建套接字对象
s = socket()

# 对套接字设置为可以立即重用端口
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

print(s.family)  #地址类型
print(s.type)    #套接字类型

s.bind(('172.40.71.193',8888))
print(s.getsockname()) #获取绑定的address
print(s.fileno())  #获取文件描述符

s.listen(3)
c,addr = s.accept()
# 获取c对应的客户端地址，相当于addr
print(c.getpeername())

c.recv(103)