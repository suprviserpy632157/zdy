# copy_file.py
# 父子进程共同复制一个文件，分别复制文件的上半部分和下半部分到一个新文件中
from multiprocessing import Process
import os
from time import sleep

filename = "day6.txt"
# 获取文件的大小
size = os.path.getsize(filename)
print(size)
# f = open(filename,'rb')

# 复制上半部分
def top():
    #这么做是为了让子进程先运行,此时他们用的偏移量是一样的,由于f与外部资源有关联,
    # 公用了同一套属性,属性之间会有影响.索引应该各自打开
    # sleep(1) 
    f = open(filename,'rb')
    n = size//2
    fw = open("half_top.txt",'wb')
    # n特别大时,大于1024的部分直接读,直到小于1024时结束读取
    # fw.write(f.read(n))
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

# 复制下半部分
def boot():
    f = open(filename,'rb')
    fw = open('half_bottom.txt','wb')
    n = size//2
    # 从头开始,移动size//2个字节
    f.seek(n,0) 
    while 1:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

t = Process(target = top)
b = Process(target = boot)
t.start()
b.start()
t.join()
b.join()