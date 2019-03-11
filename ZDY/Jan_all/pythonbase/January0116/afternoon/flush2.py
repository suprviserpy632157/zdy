# 此实例示意文件缓冲区的作用及清除方法
fw=open("myflush.txt",'w')

fw.write("hello") #此处执行的write操作没有真正写在磁盘上
import time
while 1:  #进入死循环
    time.sleep(0.1)
    print(time.time())
    fw.write('A'*1000+'\n')

fw.close()