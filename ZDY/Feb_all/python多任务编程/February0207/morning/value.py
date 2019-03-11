# value.py
from multiprocessing import Value,Process
import time
import random
# 创建共享内存
money = Value('i',5000)

# 创建共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100,900)

m = Process(target = man)
g = Process(target = girl)
m.start()
g.start()
m.join()
g.join()

print("一月余额:",money.value)