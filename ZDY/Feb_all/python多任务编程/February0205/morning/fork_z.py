# fork_z.py
# 僵尸进程的产生过程
# 理解:父进程不退出,子进程先于父进程退出,尽量避免僵尸进程
import os 
from time import sleep

pid = os.fork()

if pid == 0:
    print("Child PID",os.getpid())
    os._exit(0)
else:
    print("Parent process,我的儿！")
    while 1:
        pass