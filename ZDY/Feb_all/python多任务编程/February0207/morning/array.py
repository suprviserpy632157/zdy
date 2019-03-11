from multiprocessing import Array,Process
import time
# 创建共享内存
# shm = Array('i',[1,2,3,4,5])

# 创建共享内存,指定开辟空间大小
shm = Array('i',6)

# 存入字符串
# shm = Array('c',b'Hello')
def fun():
    for i in shm:
        print(i)
    shm[2] = 300
    # shm[0] = b'h'

p = Process(target = fun)
p.start()
p.join()
for i in shm:
    print(i,end=' ')
print(shm.value) #只有打印字符串时,才能.value