from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())
p = Process(target = tm,name = "kxx")
# p.daemon = True
p.start()
print("Process name:",p.name)
print("Process PID:",p.pid)
print("alive",p.is_alive())
p.join(2)
print("***************")