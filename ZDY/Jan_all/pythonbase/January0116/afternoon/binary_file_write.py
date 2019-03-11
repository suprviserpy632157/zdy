# 此实例示意写入２５６个字节到一个文件中，
# 第一个字节的值为０，第二个字节的值为１．．．
try:
    f=open('myfile.bin','wb')  #wb为二进制写操作
    b=bytes(range(256)) #创建一个２５６个字节的字节串
    print(b)
    r=f.write(b)  # 写入２５６个字节到文件中
    print("成功写入了",r,"个字节") #注：f.write()返回值为写入的字节数
    f.close()
except OSError:
    print("文件打开失败!")