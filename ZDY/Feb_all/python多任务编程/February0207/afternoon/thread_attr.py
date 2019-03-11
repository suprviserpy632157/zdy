from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun)
# 线程名称
print(t.name)
t.setName('Tim')
print(t.getName())
print(t.name)
# 设置daemon为True
t.setDaemon(True)
# t.daemon = True
t.start()
# 查看线程生命周期
print("alive:",t.is_alive())
# t.join()