from threading import Lock,Thread

a = b = 0

# 创建一个锁对象
lock = Lock()

def value():
    while 1:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = Thread(target=value)
t.start()
while 1:
    with lock:
        a += 1
        b += 1
t.join()