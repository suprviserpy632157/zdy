'''
http server v1.0
接收浏览器请求
返回固定的相应内容
'''
from socket import *
# 处理客户端(浏览器)请求
def handleClient(connfd):
    print("Request from",connfd.getpeername())
    request = connfd.recv(4096) #接收http请求
    # 将request按行分割
    request_lines = request.splitlines()
    for line in request_lines: #按行打印
        print(line)
    # 发送网址
    try:
        f =open('index.html')
    except IOError:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "\r\n" #拼接空行
        response += "***What a pity***"
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += f.read() #若读取较大，可以循环读累加
    finally:
        # 将结果发送给浏览器
        connfd.send(response.encode())

# 创建套接字（tcp）
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8888))
    sockfd.listen(3)
    print("Listen to the port 8888")
    while 1:
        connfd,addr = sockfd.accept()
        handleClient(connfd)  #负责具体的请求处理
        connfd.close()

if __name__ == "__main__":
    main()