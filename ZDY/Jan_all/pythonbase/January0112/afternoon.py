# 练习：
# １．输入一个圆的半径，打印出这个圆的面积
# ２．输入一个圆的面积，打印出这个圆的半径
# import math
# r = float(input("输入一个圆的半径"))
# print(math.pi*r**2)
# s=float(input("输入一个圆的面积"))
# print(math.sqrt(s/math.pi))

# 另解
# import math as m
# r = float(input("输入一个圆的半径"))
# print(m.pi*r**2)
# s=float(input("输入一个圆的面积"))
# print(m.sqrt(s/m.pi))
# 继续精简
# from math import pi,sqrt
# r = float(input("输入一个圆的半径"))
# print(pi*r**2)
# s=float(input("输入一个圆的面积"))
# print(sqrt(s/pi))
# time_sleep.py
# import time
# print("这是第一行")
# # 让程序在此处睡眠１０秒
# time.sleep(10)
# print("这是第二行")

# 练习:
# 写一个程序，输出你的出生日期
# １）算出你已经出生了多少天
# ２）算出你出生那天是星期几
import time 
y=int(input("请输入出生的年："))
m=int(input("请输入出生的月："))
d=int(input("请输入出生的日："))
t=(y,m,d,0,0,0,0,0,0)
# 先得到出生时没计算机时间秒数，得到当前时间的秒数
birth_second=time.mktime(t)
# 活了多少秒
life_sec=time.time()-birth_second
life_days=life_sec/60/60//24
print("您已出生",life_days,'天')
birth_tuple=time.localtime(birth_second)
print("您出生那天是星期:",birth_tuple[6])

# # test_argv．py
# print("hello world!")
# import sys
# print(sys.argv)

# import sys
# def f1():
#     print(2)
#     # 程序退出
#     sys.exit()
#     print(3)
# print(1)
# f1()
# print(4)