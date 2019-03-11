# mydeco1.py
# 此实例示意装饰器的原理和语法
# def mydeco(fn):
#     def fx():
#         print("+++++++++++++++++++")
#         fn()
#         print("-------------------")
#     return fx
# def myfunc():
#     '''被装饰函数 '''
#     print("函数myfun被调用")
# myfunc=mydeco(myfunc)
# myfunc()
# myfunc()
# myfunc()

# def mydeco(fn):
#     def fx():
#         print("hello")
#     return fx
# @mydeco
# def myfunc():
#     '''被装饰函数 '''
#     print("函数myfun被调用")
# # myfunc=mydeco(myfunc)
# myfunc()
# myfunc()
# myfunc()

# 此实例示意函数装饰器的使用
# 以银行存取款业务为例，来为存取款业务添加新的功能
# 1.添加了权限验证
# 2.添加了短消息提醒
# def privileged_check(fn):
#     def fx(n,x):
#         print("正在检测权限．．．")
#         fn(n,x)
#     return fx
# def send_message(fn):
#     def fy(n,x):
#         fn(n,x)
#         print("正在发送消息给",n)
#     return fy
# @privileged_check
# def savemoney(name,x):   
#     print(name,'存钱',x,'元')
# @send_message
# @privileged_check
# def withdraw(name,x):
#     print(name,'取钱',x,'元')
# savemoney('小王',200)
# savemoney('小赵',400)
# withdraw('小李',500)

L=[1,2,3]
def f(n=0,lst=[]):
    '''缺省参数[]在def语句执行时
就已经创建该列表，并一直被f函数绑定'''
    lst.append(n)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)
# 修改方法
print("----------------------")
L=[1,2,3]
def f(n=0,lst=None):
    if lst is None:
        #创建一个空列表
        lst=[]  
    lst.append(n)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)