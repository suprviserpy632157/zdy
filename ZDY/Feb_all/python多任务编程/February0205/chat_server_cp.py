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
    # 判断姓名是否存在,不允许登录就结束
    if name in user:
        # 将结果反馈给客户端
        s.sendto("The user is exist".encode(),addr)
        return
    # 将结果反馈给客户端    
    s.sendto('OK'.encode(),addr)
    # 将登录信息通知其他人
    msg = "Welcome %s coming our chatroom"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    # 允许登录则将用户信息插入数据机构保存
    # 将用户加入user
    user[name] = addr

# 处理聊天
def do_chat(s,name,text):
    msg = "%s : %s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
            if text == 'Q':
                s.sendto('NoProblem'.encode(),user[i])
                mess = "%s exit our chatroom"%name
                for j in user:
                    s.sendto(mess.encode(),user[i])
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

# 创建网络连接
def main():
    ADDR = ('0.0.0.0',7795)
    # 创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 处理各种客户端请求
    do_requests(s)

if __name__ == "__main__":
    main()