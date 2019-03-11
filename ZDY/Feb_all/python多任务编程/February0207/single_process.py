# 单进程(线程)效率测试
from test import *
import time 
# count
# t = time.time()
# for i in range(10):
#     count(1,1)
# print("单进程计算密集型效率:",time.time() - t)

# IO
t = time.time()
for i in range(10):
    write()
    read()
print("单进程计算IO密集型效率:",time.time() - t)
