# stdout.py
# 此实例示意标准输出文件
import sys
sys.stdout.write("hello world\n")
#关闭文件后，print()将不再可用
sys.stdout.close()  
print("hello world")
f= open('mynote.txt','w')
print(1,2,3,4,file=f)#写入内容到文件myprint.txt中
print("hello world!!!!",file=f)