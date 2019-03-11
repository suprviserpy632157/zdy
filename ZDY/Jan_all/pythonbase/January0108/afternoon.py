# def.py
# 此实例示意有ｄｅｆ语句定义一个没有参数的函数
# def say_hello():
#     print("hello word!")
#     print("hello china")
#     print("helllo python!")
# say_hello()
# def2.py
# 此实例示意有ｄｅｆ语句定义有参数的函数，函数名为ｍｙｍａｘ
# def mymax(a,b):
#     print("a=",a)
#     print("b=",b)
#     if a>b:
#         print(a,">",b)
#     else:
#         print(a,"<=",b)
# mymax(10,100)  #函数调用
# mymax(10,2)
# 练习１
# 写一个函数ｍｙａｄｄ，此函数中的参数列表里
# # 有两个参数ｘ，ｙ此函数的功能是打印x+y的和
# def myadd(num1,num2):
#     print("sum=",num1+num2)
# myadd("ABC","123")
# v=myadd(100,200)
# print(v) #None
# 练习２
# 写一个函数print_even,传入一个
# 参数ｎ代表终止的整数，打印０～ｎ
# 之间所有的偶数
# def print_even(n):
#     for i in range(0,n,2):
#         print(i)
# print_even(10)
# 练习３
# 写一个程序mymax,实现返回两个数的最大值
# def mymax(a,b):
#     # if a>b:
#     #     return a
#     # else:
#     #     return b
#     if a>b:
#         return a
#     return b
# print(mymax(100,200))
# print(mymax("ABC","ABCD"))
# 练习４
# 写一个函数myadd，实现给出两个数，返回这两个数的和
# def myadd(x,y):
#     return x+y
# a=int(input("please input the first number:"))
# b=int(input("please input the second number:"))
# print("your input numbers add =",myadd(a,b))
# 练习５
# 写一个函数　input_number,用于获取用户循环往返整数，
# 当用户输入负数时，结束
# 将用户输入的数字以列表的形式返回，再用内建函数
# ｍａｘ，ｍｉｎ，ｓｕｍ求出用户输入的最大值，最小值，及和
def input_number():
    l=[]  #创建空列表
    #循环输入正整数，存入列表
    while 1:
        x=int(input("please input a number:"))
        if x <0:
            break
        l.append(x)
        # l+=[x]
    return l   #返回上述列表的引用关系 
L=input_number()
print("max=",max(L))
print("min=",min(L))
print("sum=",sum(L))
