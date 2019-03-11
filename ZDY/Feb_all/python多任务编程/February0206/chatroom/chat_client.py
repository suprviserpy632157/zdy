from socket import *
import os,sys

#服务器地址
ADDR = ("127.0.0.1",7795)

#消息发送
def send_msg(s,name):
    #循环发送
    while 1:
        try:
            text = input("Say:")
        except Exception:
            text = 'quit'
        # strip:去掉字符两边的空格
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("You are exiting the chatroom") 
        msg = "C %s %s"%(name,text)  #C表示请求类型是聊天
        s.sendto(msg.encode(),ADDR)

#消息接收
def recv_msg(s):
    while 1:
        data,addr = s.recvfrom(2048)
        # 如果服务器发来NoProblem表示客户退出
        if data.decode() == 'NoProblem':
            sys.exit()
        print(data.decode()+'\nsay:',end = '')

#创建网络连接
def main():
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    #循环发送消息
    while True:
        #输入姓名
        name = input("Please input your name:")
        #L表示登录,加一个空格传输过去便于切割
        msg = "L " + name
        # 将姓名发送给服务端
        s.sendto(msg.encode(),ADDR)
        #等待服务端反馈
        data,addr = s.recvfrom(1024)
        #允许则进入聊天室 
        if data.decode() == "OK":
            print("You are coming chatroom")
            break
        #如果不允许进入，则在循环中重新输入
        else:
            #打印不允许登录的原因
            print(data.decode())
    #创建新的进程，一个用于收消息，一个用于发消息
    pid = os.fork()
    if pid < 0:
        sys.exit("error!!")
    elif pid == 0:
        send_msg(s,name)
    else: 
        recv_msg(s)

if __name__ == "__main__":
    main()
