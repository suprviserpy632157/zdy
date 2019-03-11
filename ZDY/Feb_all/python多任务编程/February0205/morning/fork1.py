# 理解:在子进程中修改,在父进程中不变
import os 
from time import sleep

print("********")
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed!")
# 子进程会打印a=1，因为将赋值语句的空间也进行了复制
elif pid == 0:
    print("Child process")
    print("a=%d"%a)
    # 这是子进程执行的，父进程不会执行，所以父进程中a仍为1
    a = 10000
else:
    sleep(1)
    print("Parent process")
    print("a:",a)
# 父子进程都执行一次
print("all a=",a)