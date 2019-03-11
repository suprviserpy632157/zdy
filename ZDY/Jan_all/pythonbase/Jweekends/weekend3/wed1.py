# # 1.1,2,3,4组成所有排序不同的三位数
# # 将百位范围确定
# for i in range(1,5):
#     # 将十位范围确定
#     for j in range(1,5):
#         # 将个位范围确定
#         for k in range(1,5):
#             # 判断三个数必须都不相同才能打印
#             if(i!=k)and(i!=j)and(j!=k):
#                 # 打印所有可能得到的三位数
#                 print(i,j,k)
# # 2.企业发奖金
# try:
#     i=int(input("净利润:"))
# except ValueError:
#     print("error")
# # 利润限制
# arr=[1000000,600000,400000,200000,100000]
# # 利润比例
# rat=[0.01,0.015,0.03,0.05,0.075,0.1]
# # 统计奖金
# r=0
# for idx in range(0,6):   
#     # 异常处理
#     try:
#         # 判断条件：利润大于对应的利润限制
#         if i>arr[idx]:
#             # 钱数与其对应的比例相乘
#             r+=(i-arr[idx]*rat[idx])
#             # 打印低一级的钱数（1000000完了继续打印600000对应的利润）
#             print(i-arr[idx]*rat[idx])
#             # 低一级的利润赋值给ｉ让其继续循环
#             i=arr[idx]
#     # 发生了IndexError错误立即返回
#     except IndexError:
#         break
# # 打印所得奖金
# print(r)
# # 3.完全平方数
# # 导入math模块
# import math as m
# # 遍历10000内的数字
# for i in range(10000):
#     # 一个整数加上100和加上268后都是一个完全平方数
#     x=int(m.sqrt(i+100))
#     y=int(m.sqrt(i+268))
#     if(x*x==i+100)and(y*y==i+268):
#         print(i)
# #4.日期计算
# # 输入要查询的年月日
# try:
#     year=int(input('year:'))
#     month=int(input('month:'))
#     day=int(input('day:'))
# except ValueError:
#     print("error2")
# except:
#     print("error3")
# # 给出月份天数累加元组
# months=(0,31,59,90,120,151,181,212,243,273,304,334)
# # 判断月份是否合法
# if 0<month<=12:
#     # 索引下标并将对应的数字相加
#     sum=months[month-1]
# else:
#     print("date error")
#     sum+=day
# leap = 0
# # 闰年判断
# if(year%400==0)or((year%4==0)and(year%100!=0)):
#     leap=1
# # ２月之后加一天
# if(leap==1)and(month>2):
#     sum+=1
# # 打印这是一年的第几天
# print("it is the %dth day,"%sum)
# # 5.整数顺序排列
# # 准备一个空列表添加整数
# L=[]
# # ３以内遍历
# for i in range(3):
#     # 请输入３个数    
#     x=int(input("interger:"))
#     # 列表添加输入的３个数
#     L.append(x)
# # 列表排序
# L.sort()
# print(L)
# # 6.1斐波那契数
# def fib(n):
#     # a,b分别赋值1,1
#     a,b=1,1
#     # 遍历剩余的数
#     for i in range(n-1):
#         # b的值赋给a,a+b的值赋给b
#         a,b=b,a+b
#     return a
# def fibo(n):
#     # 给出终止条件
#     if n==1 or n==2:
#         return 1
#     # 递归返回斐波那契数列
#     return fibo(n-1)+fibo(n-2)
# # 6.2输出指定的斐波那契数列
# def fib_f(n):
#     # 如果输入１打印列表[1]
#     if n ==1:
#         return [1]
#     # 如果输入２打印列表[1,1]
#     if n ==2:
#         return [1,1]
#     # 用fibs将列表[1,1]绑定
#     fibs=[1,1]
#     # 从２到ｎ遍历
#     for i in range(2,n):
#         # 添加下一个斐波那契数，即：将原fibs中的最后一个数和倒数第二个数相加
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# print(fib_f(5))
# 7.列表数据赋值
# x=[1,2,3]
# y=x[:]
# print(y)
# # 8.九九乘法表
# # 8.1.长方形完整格式
# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print()
# # 8.2.左上三角形
# for i in range(1,10):
#     for j in range(i,10):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print()
# # 8.3.右上三角形
# for i in range(1,10):
#     for k in range(1,i):
#         # 7个空格
#         print(end="       ")
#     for j in range(i,10):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print()
# # 8.4.左下三角形
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print()
# # 8.5.右下三角形
# for i in range(1,10):
#     for k in range(1,10-i):
#         # 7个空格
#         print(end="       ")
#     for j in range(1,1+i):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print()
# # 9 time.sleep
# # 导入time模块
# import time
# myD={1:'a',2:'b'}
# # 遍历key,value
# for key,value in dict.items(myD):
#     print(key,value)
#     # 睡眠１秒接着打印
#     time.sleep(1)
# # 10.时间格式化
# # 导入time模块
# import time 
# # time.strftime函数接收以时间元组，并返回可读字符串表示的当地时间，格式由format决定
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
# # 暂停一秒
# time.sleep(1)
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
# # 10.兔子算法
# # 刚开始的两只兔子都只能生一个
# a=1
# b=1
# # 从第三只兔子开始遍历
# for i in range(1,21):
#     print((a,b),)
#     # 若i对３取余为０
#     if(i%3)==0:
#         # 换行
#         print(" ")
#     # 第三只开始＝它前两只的和
#     a=a+b
#     # 第四只开始＝它前两只的和
#     b=a+b
