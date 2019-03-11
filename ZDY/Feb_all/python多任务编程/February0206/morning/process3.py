from multiprocessing import Process
from time import sleep
# 带参数进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")
# p = Process(target = worker,args = (2,'Evil'))
# p = Process(target = worker,kwargs = {'name':'Angle','sec':2})
p = Process(target = worker,args = (2,),kwargs = {'name':'Angle'})
p.start()
p.join()