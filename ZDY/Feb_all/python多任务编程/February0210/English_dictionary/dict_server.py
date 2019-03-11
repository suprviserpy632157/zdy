# coding = utf-8
'''
dict project for AID
'''
from socket import *
import pymysql
import os,sys
import time
import signal

# 理解:导入需要的模块后,设置需要提前声明的全局变量,
# 进而进行网络连接的搭建:数据库的连接,基于fork的多进程网络并发模型
# 并在主函数中等待客户端连接,创建子进程,让子进程实现具体的交互内容

# 定义全局变量
# 用户可以直接在命令行后面直接输入(sys.argv)
if len(sys.argv) < 3:
    print('''Start as:
    python3 dict_server.py '0.0.0.0' 8000
    ''')
    sys.exit(0)
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
# 单词本的位置
DICT_TEXT = './dict.txt'

# 搭建网络连接
def main():
    # 创建数据库连接
    db = pymysql.connect("127.0.0.1","root","123456","dict")
    # 创建tcp套接字
    s = socket()
    # 可以去掉,因为端口写外面了,不能用可以直接修改
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    # 僵尸进程处理
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 等待客户端连接
    while True:
        try:
            c,addr = s.accept()
            print("Connect from:",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        
        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c,db)
            sys.exit()
        else:
            c.close()

# 理解:循环接收客户端请求,并根据客户端发送来的请求做出相应的操作

# 处理客户端请求
def do_child(c,db):
    # 循环接收客户端请求
    while True:
        data = c.recv(1024).decode()
        # 打印收到什么样的请求
        print(c.getpeername(),':',data)
        if not data or data[0] == "E":
            c.close()
            sys.exit()
        elif data[0] == "R":
            do_register(c,db,data)
        elif data[0] == "L":
            do_login(c,db,data)
        elif data[0] == "Q":
            do_query(c,db,data)
        elif data[0] == "H":
            do_hist(c,db,data)

# 注册操作:客户端传来的data格式是:R name passward
def do_register(c,db,data):
    L = data.split(" ")
    name = L[1]
    passwd = L[2]
    cursor = db.cursor()
    sql = "select * from user where name = '%s' "%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    # 插入用户
    sql = "insert into user (name,passward) values('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except Exception as e:
        print(e)
        db.rollback()
        c.send(b'FAIL')

def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql = "insert into user(name,passward) values('%s','%s')"%(name,passwd)
    # 查找用户
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FAIL')
    else:
        c.send(b'OK')

def do_query(c,db,data):
    l = data.split(" ")
    name = l[1]
    word = l[2]
    # 无论什么情况都插入历史记录
    cursor = db.cursor()
    tm = time.ctime()
    sql = "insert into hist (name,word,time) values('%s','%s','%s')"%(name,word,tm)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    # 单词本查找
    f = open(DICT_TEXT)
    for line in f:
        # 提取单词
        tmp = line.split(' ')[0]
        if tmp > word:
            break
        elif tmp == word:
            c.send(line.encode())
            f.close()
            return
    c.send("没有找到该单词".encode())
    f.close()

def do_hist(c,db,data):
    name = data.split(" ")[1]
    cursor = db.cursor()
    sql = "select * from hist where name='%s' order by id desc limit 10"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b"FAIL")
    else:
        c.send(b'OK')
        time.sleep(0.1)
    for i in r:
        # 取后三项:
        msg = "%s %s %s"%(i[1],i[2],i[3])
        c.send(msg.encode())
        time.sleep(0.1)
    c.send(b'##')

if __name__ == "__main__":
    main()
