# file_write.py
# 此实例示意写文件的基本操作
try:
    # １．打开文件
    f=open("mynote.txt",'a')
    # ２．写文件
    f.write("ABCD\n")
    f.write("你好！")
    # f.write({1:2})写操作一定得是字符串
    f.writelines(['abcd','1234\n'])
    # ３．关闭文件
    f.close()
except OSError:
    print("打开文件失败")