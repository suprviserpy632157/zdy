# 此实例示意用seek方法来改变文件流的读写位置
f=open("char20.txt",'rb')
print("当前文件的读写位置是：",f.tell())
b=f.read(3)
print("读过三个字节后的读写位置是：",f.tell())
# 此处读取５～９这５个字节
# 1.从文件头开始偏移
f.seek(5,0)
# 2.相对当前位置开始偏移
f.seek(2,1)
# 3.相对文件尾向前开始偏移
f.seek(-15,2)
print("移动后的文件读写位置是：",f.tell())
b=f.read(5)
print("b=",b)
f.close()