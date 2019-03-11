# 次实例示意用ｗｈｉｌｅ语句打印５行ｈｅｌｌｏ
# i = 0 #先创建一个变量，用来控制循环的次数
# while i < 5:
#     print("hello")
#     i+=1
# print("end")
# 打印１～１０的整数
# i = 1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print("end")
# 问题：
# 写一个程序，输入一个整数n，打印如下内容
#   这是第一行
#   这是第二行
#   这是第三行
#   …
#   这是第n行
# n=int(input("please give a number:"))
# i=1  #控制循环次数的变量（循环变量）
# while i<=n:
#     print("This line is",i)
#     i+=1
# else:
#     print("end")
# 练习
# １．写程序打印１～２０的整数
# ２．写程序，打印１～２０的整数，打印在１行内
# ３．写程序，打印１～２０的整数，每行５个打印４行
# i=1
# while i<=20:
#     print(i)
#     i+=1

# j=1
# while j<=20:
#     print(j,end=' ')
#     j += 1
# print() #换行

# x=1
# while x<=20:
#     print(x,end=' ',flush=True)
#     if x%5==0:
#         print()
#     x+=1
# 4.写一个程序输入一个开始的整数存于ｂｅｇｉｎ变量中，
# 　输入一个结束的整数存于ｅｎｄ变量中
# 　打印从ｂｅｇｉｎ到ｅｎｄ（不包含ｅｎｄ）的每个整数
# 　打印在一行内
# 思考：如何实现每５个打印在一行内，打印多少行？
# begin = int(input("please input a start number:"))
# end = int(input("please input an end number:"))
# count = 0  
# while begin<end:
#     print(begin,end=' ',flush=True)
#     count　+=　1　　
#     if count%5==0:
#         print()　　
#     begin+=1
# print()
# ５．计算１＋２＋３＋．．．＋１００的和并打印这个和
# i = 1
# he = 0
# while i<=100:
#     i+=1  
#     he += i   
# print(he)
# 6.输入一个整数ｎ，打印一个宽度和高度都为ｎ个字符的长方形
i = 1
num = int(input("please input a number:"))
print(num*"#")
while i <= num-2 :    #此循环会走ｎｕｍ－２次 
    print("#"+' '*(num-2)+"#")
    i+=1
if num >= 2:
    print(num*"#")