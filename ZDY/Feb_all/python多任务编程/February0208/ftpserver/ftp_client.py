# 导入模块
from socket import *
import sys
from time import sleep

# 具体功能实现
class FTPClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list(self):
        self.sockfd.send(b'L')  #发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            data = self.sockfd.recv(4096).decode()
            # 按,分割
            files = data.split(',')
            for file in files:
                print(file)
        else:
            # 无法完成操作,打印为什么无法完成
            print(data)
    
    def do_quit(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self,filename):
        self.sockfd.send(("G "+filename).encode())
        # 等待服务器的反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 下载文件,以二进制方式打开
            fd = open(filename,'wb')
            while 1:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()          
        else:
            print(data) 
    
    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except IOError:
            print("没有该文件")
            return
        # 做一个filename处理,不能出现../../filename问题
        # 获取真实文件名对路径解析
        filename = filename.split('/')[-1]
        self.sockfd.send(("P " + filename).encode())
        # 等待服务器反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while 1:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    # 表示文件发送完了
                    self.sockfd.send(b'##')
                    break
                # 发送文件内容
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

# 网络连接
def main():
    # 服务器地址
    ADDR = ('127.0.0.1',7795)
    # 创建套接字
    sockfd = socket()
    # 发起连接
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器失败:",e)
        return

    # 创建文件处理对象
    ftp = FTPClient(sockfd)

    # 循环发送请求
    while 1:
        print("\n===========命令选项===========")
        print("***           list         ***")
        print("***        get file        ***")
        print("***        put file        ***")
        print("***           quit         ***")        
        print("==============================")
        cmd = input("输入命令>>")
        if cmd.strip() == 'list':
            ftp.do_list()
        # 判断前三个字母为get
        elif cmd[:3] == 'get':
            # 按空格切割,取文件名
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        # 判断前三个字母为put
        elif cmd[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        else:
            print("请输入正确命令")

if __name__ == "__main__":
    main()