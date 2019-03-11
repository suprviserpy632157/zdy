# pool.py
from multiprocessing import Pool
from time import sleep,ctime

# 进程事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

# 创建进程池,有几个进程就会执行几个进程,其它的在等待进入
pool = Pool()
result = []
# 向进程池添加事件
for i in range(10):
    msg = "hello %d"%i
    r = pool.apply_async(func=worker,args=(msg,))
    result.append(r) #存储函数事件对象
# 关闭进程池,关闭之后就不能继续放事件了
pool.close()
# 回收进程池
pool.join()
for i in result:
    #通过对象的get方法可以获取事件函数返回值
    print(i.get())