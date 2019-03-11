# 理解:避免僵尸进程的方法之一,waitpid返回值,
# -1:表示等待任意子进程退出,os.WNOHANG:表示非阻塞
# 也就是说,父子进程都在做事,等到子进程结束后,父进程去做别的事
# waitpid.py
import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(2)
else:
    # 非阻塞等待
    while 1:
        p,status = os.waitpid(-1,os.WNOHANG) #没有子进程退出,返回两个0
        if p != 0:
            break
        sleep(1)
        print("做了点其它事情")
    while 1:
        print("完成父进程的其它事件")
        sleep(2)