# pipe.py
from multiprocessing import Process,Pipe
import os,time
# 创建管道对象
fd1,fd2 = Pipe(False)
# 创建进程函数
def fun(num):
    time.sleep(3)
    # 向管道写入内容
    fd2.send({num:os.getpid()})
jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    # 保存进程对象
    jobs.append(p)
    p.start()
for i in range(5):
    # 父进程中读取管道内容
    data = fd1.recv()
    print(data)
for i in jobs:
    i.join()