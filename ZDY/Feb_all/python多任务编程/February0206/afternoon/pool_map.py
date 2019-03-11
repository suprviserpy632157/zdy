# pool_map.py
from multiprocessing import Pool
from time import sleep
def fun(n):
    sleep(1)
    return n*n
pool = Pool()
# 使用map将事件放入进程池
r = pool.map(fun,range(1,6))
pool.close()
pool.join()
print("结果:",r)