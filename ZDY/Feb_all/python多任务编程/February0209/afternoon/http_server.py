# http_server.py
# coding=utf-8(编码格式)
'''
HTTP Server v2.0
*多线程并发
*基本的request解析
*能够反馈基本数据
*使用类封装
'''
# 导入模块
from socket import *
from threading import Thread
import sys

# 封装具体的类作为HTTP server功能模块
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        # 添加对象属性(认为用户可能需要的都可以设置为属性)
        self.server_address = server_addr
        # 存放网页的文件夹位置,目录与本模块为并列关系,同属于afternoon文件夹下
        self.static_dir = static_dir
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            try:
                # connfd不能变为属性(不能self.)
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print("Error:",e)
                continue
            # 创建多线程处理请求
            clientThread = Thread(target=self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
    
    # 具体处理http请求
    def handle(self,connfd):
        # 接收请求
        request = connfd.recv(4096)
        # 防止浏览器异常断开
        if not request:
            connfd.close()
            return
        # 请求解析
        requestHeaders = request.splitlines()  #按行分割
        print(connfd.getpeername(),":",requestHeaders[0])  #打印请求行
        # 获取请求内容
        getRequest = str(requestHeaders[0]).split(' ')[1]
        # 如果请求内容是'/'或以html结尾为获取网页
        if getRequest == '/' or getRequest[-5:] == '.html':
            # print("想获取网页")
            self.get_html(connfd,getRequest)
        else:
            # print("想获取其它内容")
            self.get_data(connfd,getRequest)
        connfd.close()

    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            # 拼接路径,找到主页
            filename = self.static_dir + "/index.html"
        else:
            filename = self.static_dir + getRequest
        # print(filename)
        try:
            f = open(filename)
        except IOError:
            # 没有找到网页
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseBody = "Sorry,Not found the page"
        else:
            # 返回网页内容
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = f.read()
        finally:
            # 不论结果如何,结果发回给客户端(浏览器)
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self,connfd,getRequest):
        responseHeaders = "HTTP/1.1 200 OK\r\n"
        responseHeaders += "\r\n"
        responseBody = "<p>waiting httpserver v3.0</p>"
        response = responseHeaders + responseBody
        connfd.send(response.encode())

if __name__ == "__main__":
    # 用户提供的内容有:
    # 使用者自己设定address
    server_addr = ('0.0.0.0',7795)
    # 用户提供存放网页的目录,请求自带斜杠
    static_dir = "./static"

    # 创建服务器对象
    httpd = HTTPServer(server_addr,static_dir)
    # 启动服务
    httpd.server_forever()