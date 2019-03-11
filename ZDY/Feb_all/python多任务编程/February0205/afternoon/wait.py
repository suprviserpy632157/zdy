# 理解:解决僵尸进程方法之一,wait会返回值有两个:pid和状态
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
    pid,status = os.wait()
    print("pid:",pid)
    # 显示进程原本的退出状态
    # os.WEXITSTATUS本来默认状态会*256,选取此常亮会自动/256
    print("status:",os.WEXITSTATUS(status))
    # print("status:",status)
    while 1:
        pass
