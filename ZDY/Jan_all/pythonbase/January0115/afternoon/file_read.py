# 
# 此实例示意打开一个文件，同时对文件的内容进行读取操作
try:
    # １．打开文件
    f=open("myfile.txt")
    print("文件打开成功")
    # 2.读取文件
    s=f.read() #读取全部内容
    print("读取字符的个数是：",len(s)) #+回车键了
    print("文件的内容是：",s)
    # 3.关闭文件
    f.close()
    print("文件关闭成功")
except OSError:
    print("error")


