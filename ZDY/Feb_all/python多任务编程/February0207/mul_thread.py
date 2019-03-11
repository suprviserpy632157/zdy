# 多线程效率测试
from test import *
import time
from threading import Thread

counts = []
tm = time.time()
for i in range(10):
    t = Thread(target=count,args=(1,1))
    t.start()
    counts.append(t)
for i in counts:
    i.join()
print("多线程计算密集型效率:",time.time() - tm)

# def io():
#     write()
#     read()
# tm = time.time()
# for i in range(10):
#     t = Thread(target=io)
#     t.start()
#     counts.append(t)
# for i in counts:
#     i.join()
# print("多线程IO密集型效率:",time.time() - tm)