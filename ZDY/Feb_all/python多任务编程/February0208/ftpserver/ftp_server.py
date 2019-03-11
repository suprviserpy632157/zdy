'''
ftp 文件服务器
fork server训练
'''
# 导入模块
from socket import *
import os,sys
import signal
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 7795
ADDR = (HOST,PORT)
FILE_PATH = '/home/tarena/ZDY/'

class FTPServer(object):
    def __init__(self,connfd):
        # 所有功能都要连接另一端,所以将连接套接字设置为属性
        self.connfd = connfd
    
    def do_list(self):
        # 从文件库中获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            # 只做一次操作,防止OK与后面的内容粘包
            sleep(0.1)
        files = ""
        for file in file_list:
            # 偶读是否是隐藏文件,路径与文件名连接,只能是普通文件才复合条件
            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                # 用,分割,因为客户端是用,分割的
                files = files + file + ','
        # 将拼接好的字符串传输给客户端
        self.connfd.send(files.encode())
    
    def do_get(self,filename):
        try:
            fd = open(FILE_PATH + filename,'rb')
        except IOError:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        # 发送文件内容
        while 1:
            data = fd.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b"##")
                break
            # rb 打开的,直接send就行
            self.connfd.send(data)
    
    def do_put(self,filename):
        # 判断文件是否存在
        # if os.path.isfile(FILE_PATH + filename) == True:
        if os.path.exists(FILE_PATH + filename):
            # 中文必须是.encode(),不能加b
            self.connfd.send("该文件已存在".encode())
            return
        # 如果不存在
        fd = open(FILE_PATH + filename,'wb')
        self.connfd.send(b'OK')
        # 接收文件
        while 1:
            data = self.connfd.recv(1024)
            # 约定发送##确认发送完毕
            if data == b'##': 
                break
            fd.write(data)
        fd.close()

# 客户端处理函数,想占有多久就占有多久,因为会创建新的进程
def do_requests(connfd):
    ftp = FTPServer(connfd)
    while 1:
        data = connfd.recv(1024).decode()
        # 查看文件列表
        if not data or data[0] == 'Q': #提前写,防止客户端断开时data为空报错
            connfd.close()
            return  #客户端断开连接,服务器没有再连接的必要
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == "G":
            # 取出文件名
            filename = data.split(" ")[-1]
            ftp.do_get(filename)
        elif data[0] == "P":
            filename = data.split(" ")[-1]
            ftp.do_put(filename)

# 网络搭建
def main():
    # 创建tcp套接字
    sockfd = socket()
    # 设置端口重用
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 绑定套接字
    sockfd.bind(ADDR)
    # 监听套接字
    sockfd.listen(5)
    # 打印提示信息
    print("Listen to the port 7795...")
    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 循环接收客户端请求
    while 1:
        try:
            # 接收客户端连接请求
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常:",e)
            # 结束本次循环
            continue
        print("连接客户端:",addr)
        # 创建子进程处理客户端请求
        pid = os.fork()
        if pid == 0:
            # 子进程若不关闭sockfd可能会通过属性对父进程中的sockfd造成影响
            sockfd.close()
            # 由于s关闭,并且不希望子进程继续循环
            do_requests(connfd)  #处理客户端请求
            # 不在子进程中写,子进程直接return就可以
            os._exit(0)     #子进程直接退出
        # 父进程或创建进程失败,都是循环接收新的连接
        else:
            # 父进程只需要连接不需要交互,所以c对他没有,可以直接关闭
            connfd.close()
if __name__ == "__main__":
    main()