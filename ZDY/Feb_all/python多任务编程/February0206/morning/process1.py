import multiprocessing as mp
from time import sleep
# 编写进程函数

a = 1 
def fun(): #a的修改结果只在子进程内生效
    sleep(3)
    global a
    print("a=",a)
    a = 10000
    print("子进程执行事件")

# 创建进程对象
p = mp.Process(target=fun)
# 启动进程
p.start()

sleep(2)
print("父进程事件")
# 回收进程,阻塞进程:等待子进程结束回收
p.join(1)
print("parent a =",a)