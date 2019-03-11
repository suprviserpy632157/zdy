# fork.py
# 理解:通过导入os模块调用fork方法
# 配合if语句让父子进程分别做不同的事
import os
from time import sleep
# 创建新的进程
pid = os.fork()
# 如果创建进程失败
if pid < 0:
    print("Create process failed!")
# 子进程执行内容
elif pid ==0:
    sleep(2)
    print("New process")
# 父进程执行内容
else:
    sleep(1)
    print("The old process")
# 父子进程都要执行的内容
print("fork test over")