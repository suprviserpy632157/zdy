# sock_server.py
'''
使用socketserver模块完成网络并发模型
'''
from socketserver import *
# 创建tcp 多进程并发
class Server(ForkingMixIn,TCPServer):
# 多线程TCP并发
# class Server(ThreadingMixIn,TCPServer)
# class Server(ThreadingTCPServer)
    pass
# 具体请求处理类
class Handler(StreamRequestHandler): #UDP:继承DatagramRequestHandle
    # 重写具体处理方法
    def handle(self):
        print("Connect from",self.client_address)
        while 1:
            # self.request <=> accept返回的connfd
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b"OK")

server_addr = ("0.0.0.0",7795)
# 创建服务器对象,通过参数传到类中自定义变量
server = Server(server_addr,Handler)
# 启动服务
server.serve_forever()