# child_child.py
# 创建二级进程处理僵尸
# 理解:父进程创建一级子进程,一级子进程创建二级子进程之后一级子进程直接退出,
# 且父进程直接将一级子进程回收,这样二级子进程成为孤儿进程,一定不会成为僵尸进程,
# 这样,父进程做一件事,二级子进程做另一件事
from time import sleep
import os 
def f1():
    sleep(3)
    print("吃元宵...")
def f2():
    sleep(4)
    print("处理南北甜咸之争...")
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    # 创建二级子进程
    p = os.fork()
    if p == 0:
        # 二级子进程做另一件事
        f2()
    else:
        os._exit(0)
else:
    # 等待一级子进程退出
    os.wait()
    # 执行f1()
    f1()