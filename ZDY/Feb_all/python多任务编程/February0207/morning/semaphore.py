# semaphore.py
from multiprocessing import Semaphore,Process
from time import sleep
import os
# 创建信号量 设置为3
sem = Semaphore(3)
def fun():
    print("%d 想执行事件"%os.getpid())
    # 想执行事件必须得到信号量资源,都会执行
    sem.acquire()
    # 只能执行3句,其它两个进程被上一步阻塞
    print("%s抢到了一个信号量,可以执行操作"%os.getpid())
    sleep(3)
    print("%d执行完事再增加信号量"%os.getpid())
    # 增加信号量
    sem.release()
jobs = []
for i in range(5):
    p = Process(target = fun)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print(sem.get_value())