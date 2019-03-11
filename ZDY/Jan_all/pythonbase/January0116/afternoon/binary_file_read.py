# 此实例示意用二进制模式操作文件，实现
# 读取文件myfile.bin数据中的前10个字节
fr=open('myfile.bin','rb')
b=fr.read(10)
print("b=",b)
fr.close()