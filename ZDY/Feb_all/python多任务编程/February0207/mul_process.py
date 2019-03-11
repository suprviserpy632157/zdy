# 多进程效率测试
from test import *
from multiprocessing import Process
import time

counts = []

# t = time.time()
# for i in range(10):
#     p = Process(target=count,args=(1,1))
#     p.start()
#     counts.append(p)
# for i in counts:
#     i.join()
# print("多进程计算密集型效率:",time.time() - t)

def io():
    write()
    read()
t = time.time()
for i in range(10):
    p = Process(target=io)
    p.start()
    counts.append(p)
for i in counts:
    i.join()
print("多进程IO密集型效率:",time.time() - t)