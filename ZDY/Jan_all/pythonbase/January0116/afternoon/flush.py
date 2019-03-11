# 此实例示意文件缓冲区的作用及清除方法
fw=open("myflush.txt",'w')

fw.write("hello") #此处执行的write操作没有真正写在磁盘上
fw.flush()  #清空缓冲区
while 1:  #进入死循环
    pass

fw.close()