# 创建多个子进程
import multiprocessing as mp
from time import sleep
import os
def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),'---',os.getpid())
def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'---',os.getpid())
def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'---',os.getpid())
# 创建进程对象
things = [th1,th2,th3]
process = []
for th in things:
    p = mp.Process(target = th)
    process.append(p)  #用列表保存进程对象
    # 启动进程
    p.start()
for i in process:
    # 进程回收
    i.join()

