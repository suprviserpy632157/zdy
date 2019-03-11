# coding=utf-8
'''
Chatroom
env:python3.5
exc:socket and fork
'''
from socket import *
import os,sys

# 用于存储用户{name:addr}
user = {}

# 处理登录
def do_loadin(s,name,addr):
    # 判断姓名是否存在,或不合法,则不允许登录就结束
    if (name in user) or name == "Manager":
        # 将结果反馈给客户端
        s.sendto("The user is exist".encode(),addr)
        return
    # 将结果反馈给客户端    
    s.sendto('OK'.encode(),addr)
    # 将登录信息通知其他人
    msg = "\nWelcome %s coming our chatroom"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    # 允许登录则将用户信息插入数据机构保存
    # 将用户加入user
    user[name] = addr

# 处理聊天
def do_chat(s,name,text):
    msg = "\n%s : %s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

# 处理退出
def do_quit(s,name):
    msg = "\n%s is exiting our chatroom"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b"NoProblem",user[i])
    # 将用户删除
    del user[name]

def do_requests(s):
    while True:
        # 接收姓名
        data,addr = s.recvfrom(1024)
        # 解析发过来的请求
        msgList = data.decode().split(' ')
        # 区分请求类型
        if msgList[0] == 'L':
            do_loadin(s,msgList[1],addr)
        elif msgList[0] == 'C':
            # 重新组织消息内容,索引2之后内容重新拼接回去
            text = ' '.join(msgList[2:])
            do_chat(s,msgList[1],text)
        elif msgList[0] == 'Q':
            do_quit(s,msgList[1])

# 创建网络连接
def main():
    ADDR = ('0.0.0.0',7795)
    # 创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 单独创建进程用于发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Error")
        return
    elif pid == 0:
        while 1:
            msg = input("Manager message:")
            msg = "C Manager" + msg
            s.sendto(msg.encode(),ADDR)
    else:
        # 处理各种客户端请求
        do_requests(s)

if __name__ == "__main__":
    main()