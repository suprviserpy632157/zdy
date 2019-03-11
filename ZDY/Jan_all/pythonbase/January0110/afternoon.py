# v=100
# def f1():
#     global v
#     v=200
# f1()
# print(v)

# v=100
# def fx():
#     v=200
#     global v
#     v+=300
# fx()
# print(v)

# v=100
# def fx(v):
#     print(v)
#     global v  
#     v=300
# fx(200)
# print(v)

# 练习
# 用全局变量记录一个函数ｆｘ调用的次数
# count = 0
# def fx(name):
#     print("你好",name)
#     global count
#     count+=1
# fx("小张")
# fx("小李")
# print("fx函数共被调用",count,'次')

# v=100
# def f1():
#     v=200
#     print("f1.v=",v)
#     #此处嵌入另一个函数
#     def f2():
#         #声明ｖ为外部嵌套函数作用域的变量 
#         v=300
#         #再嵌入另一个函数
#         def f3():
#             nonlocal v
#             v=400
#         f3()
#         print("f2.v=",v)
#     f2()
#     print("f1执行后f1.v=",v)
# f1()

# eval.py
# x=100
# y=200
# s="x+y+1"
# r=eval(s)
# print("r=",r)
# # 先创建一个局部作用域的字典
# local_scope={'x':1,'y':2}
# a=eval(s,None,local_scope)
# print('a=',a)
# # 创建一个全局作用域的字典
# global_scope={'x':10,'y':20}
# b=eval(s,global_scope)
# print('b=',b)
# # 两个作用域都存在
# c=eval(s,{'x':10,'y':20},{'x':1})
# print("c=",c)

# exec.py
s=''' 
myadd=lambda x,y:x+y

print("20+30=",myadd(20,30))
print("1+2=",myadd(1,2))
'''
exec(s)