# def f1():
#     print("132")
# f2=f1   #两个变量同时绑定一个函数
# f2()　　 #f1函数被调用
# f2=f1()   #返回的是Ｎｏｎｅ

# def f1():
#     print("f1")
# def f2():
#     print("f2")
# f1,f2=f2,f1
# f1()

# def f1():
#     print("f1被调用")
# def f2():
#     print("f2被调用")
# def fx(fn):
#     print(fn)
#     fn() #fn调用f1
# fx(f1)

# def goodbye(L):
#     for x in L:
#         print("再见:",x)
# def operator(fn,L):
#     fn(L)
# operator(goodbye,('Tom',"Jerry",'Spike'))

# def myinput(fn):
#     L=[1,3,5,7,9]
#     return fn(L)
# print(myinput(max))
# print(myinput(min))
# print(myinput(sum))

# def get_function():
#     s=input("请输入您要做的操作：")
#     if s == "求最大":
#         return max
#     elif s=='求最小':
#         return min
#     elif s=='求和':
#         return sum
# L=[2,4,6,8,10]
# f=get_function()
# print("f绑定：",f)
# print(f(L))

# # 练习１
# # 写一个计算公式的解释执行器
# # 　已知有如下一些函数
# def myadd(x,y):
#     return x+y
# def mysub(x,y):
#     return x-y
# def mymul(x,y):
#     return x*y
# # 定一个带有一个参数的函数
# # 此函数的在传入字符串“加”或“＋”返回ｍｙａｄｄ函数
# # 此函数的在传入字符串“乘”或“＊”返回ｍｙａｄｄ函数
# def get_func(s):
#     if s=="加"  or s=='＋':
#         return myadd
#     if s in ('乘','*'):
#         return mymul
# # 在主函数中程序如下：
# def main():
#     while True:
#         s=input("请输入计算公式:")
#         L=s.split()
#         a=int(L[0])
#         b=int(L[2])
#         fn =get_func(L[1])
#         print("结果是：",fn(a,b))
# main()

# def get_func(s):
#     def myadd(x,y):
#         return x+y
#     def mysub(x,y):
#         return x-y
#     def mymul(x,y):
#         return x*y
#     if s=="加"  or s=='＋':
#         return myadd
#     if s in ('乘','*'):
#         return mymul
# def main():
#     while True:
#         s=input("请输入计算公式:")
#         L=s.split()
#         a=int(L[0])
#         b=int(L[2])
#         fn =get_func(L[1])
#         print("结果是：",fn(a,b))
# main()

# # 此实例示意函数的嵌套定义
# def fn_outer():
#     print("fn_outer被调用")
#     #此处能否创建新的函数并调用呢？
#     def fn_inner():
#         print("fn_inner被调用")
#     #调用一次
#     fn_inner() 
#     fn_inner()
#     print("fn_outer调用结束")
# fn_outer()

# 此实例示意Ｐｙｔｈｏｎ的作用域
# v=100
# def fun1():
#     # v=200
#     print("fun1.v=",v)
#     def fun2():
#         # v=300
#         print("fun2.v=",v)
#     fun2()
# fun1()
# print("全局的v=",v)

# 练习２
# 执行以下程序，看执行结果是什么?为什么？
L=[1,2,3]
v=100
def f1():
    L.append(4)
    v=200
f1()
print(L)  #[1,2,3,4]
print(v)  #100

def f2():
    # L += [5]  #+=是赋值语句，会出错
    L.extend([5])
    v += 1  #出错
f2()