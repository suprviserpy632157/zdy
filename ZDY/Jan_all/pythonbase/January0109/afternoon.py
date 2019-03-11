# star_tuple_args.py
# 星号元组形参的定义和使用
# def func(*args):
#     print("实参个数是：",len(args))
#     print('args=',args)
# func(1,2,3,4)
# func(5,6,7,8,'A','B','C','D')
# func()
# # 练习:1
# # 写一个函数，mysum可以传入任意
# # 个数字参数，返回所有实参的和
# def mysum(*args):
#     # return sum(args)
#     s=0
#     for x in args:
#         s+=x
#     return s
# print(mysum(1,2,3,4))
# print(mysum(1,3,5,7,9))
# name_keyword_args.py
# 在函数形参中定义命名关键字传参，强制让函数调用
# 使用命名关键字传参：
# def func1(a,b,*,c,d):
#     print(a,b,c,d)
# # func1(1,2,3,4)
# func1(1,2,c=30,d=40)
# func1(a=10,b=20,c=30,d=40)

# def func2(a,b,*args,c,d):
#     print(a,b,args,c,d)
# # func1(1,2,3,4)
# func2(1,2,c=30,d=40)
# func2(a=10,b=20,c=30,d=40)
# func2(1,2,3,4,d=400,c=300)
# func2(*"ABCDEFG",**{'c':999,'d':998})
# star_dict_args.py
# 此实例示意用双星号字典形参接受多余的关键字传参
# def fnuc(**kwargs):
#     print("关键字传参的个数是：",len(kwargs))
#     print("kwargs=",kwargs)
# func(name='wei',age=35,address='beijing')
# func(a=1,b=2)
# def func(a,b,*kwargs):
#     print(len(kwargs))
#     print("kwargs=",kwargs)
# func(a=1,b=2,c=3)

# def fn(a,b=20,*args,c=30,d=40,**kwargs):
#     print(a,b,args,c,d,kwargs)
# fn(1)
# fn(100,200,300,400,c='C',d='D',e='E')
# 练习：
# 已知内建函数ｍａｘ帮助文档
# max(...)
# max(iterable) -->value
# max(arg1,arg2,*args)-->value
# 仿造ｍａｘ写一个ｍｙｍａｘ函数，功能与ｍａｘ完全相同
# def mymax(*args):
#     #判断是否是一个可迭代参数的情况
#     if len(args)==1:
#         #一定绑定一个可迭代对象
#         l=args[0]
#         #假设第一个元素最大
#         zuida=l[0]
#         for x in l:
#             if x>zuida:
#                 zuida = x
#         return zuida
#     #否则有多个参数的情况
#     else:
#         zuida= args[0]
#         for x in args:
#             if x > zuida:
#                 zuida = x
#         return zuida 
# def mymax(a,*args):
#     if len(args)==0:
#         l=a
#         zuida=l[0]
#         for x in l:
#             if x>zuida:
#                 zuida = x
#         return zuida
#     else:
#         zuida= a
#         for x in args:
#             if x > zuida:
#                 zuida = x
#         return zuida 
# print(mymax([6,8,3,5]))
# print(mymax(100,200))
# print(mymax(1,3,5,9,7))

# a=100
# b=200
# def fx(c):
#     d=400
#     print(a,b,c,d)
# fx(300)
# print("a=",a)
# print("b=",b)
# #print('c',)# 出错

a=1 
b=2
c=3
def fn(c,d):
    e=300
    #此处有多少个局部变量？３
    print(locals())
    #此处有多少个全局变量？４
    print(globals())
    print(c) #100
    print(globals()['c'])
fn(100,200)