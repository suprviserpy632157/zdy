# def myfun1(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# # myfun1(1,2,3)  #1 to a,2 to b,3 to c

# L1=[11,22,33]
# t2=(100,200,300)
# s3="ABC"
# myfun1(L1[0],L1[1],L1[2])
# myfun1(*L1)  #　＊是拆解序列
# myfun1(*t2)
# myfun1(*s3)

# myfun1(b=22,c=33,a=11)

# d1={'c':33,'a':11,'b':22}
# myfun1(**d1)
# myfun1(c=d1['c'],a=d1['a'],b=d1['b'])
# 练习1
# 已知有列表：
# 　Ｌ=[1,2,True,None,3.14]
# 调用print函数，打印用“＃”分割的文字信息
# l=[1,2,True,None,3.14]
# print(*l,sep="#")

# myfun1(*[100,200],300)
# myfun1(100,*[200],300)
# myfun1(100,**{'c':300,'b':200})
# myfun1(100,c=300,b=200)
# myfun1(**{'c':300,'b':200},a=100)

# 当函数的实参为可变数据类型时，
# 在函数内部可以改为容器的内容
# l=[1,2,3,4]
# t=(1.1,2.2,3.3,4.4)
# def append_5(x):
#     # x.append(5)
#     x+=(5,)
# append_5(l)
# print(l)
# append_5(t)
# print(t)

# 写一个函数，此函数读取用户输入的数据，
# 最后保存于全局变量的列表
# ｌ中，当用户输入小于０的时候结束输入
# l=[]
# def input_number(l1):
#     while 1:
#         x=int(input("please input:"))
#         if x <0:
#             break
#         l1.append(x)
# input_number(l)
# print(l)
# input_number(l)
# print(l)

# def info(name,age=1,address='不详'):
#     print(name,'今年',age,'岁，家庭住址：',address)
# info("zdy",23,"beijing")
# info('tarena',15)
# info("qwer")

# 写一个函数myadd,此函数可以
# 计算两个数，三个数积四个数的和
def myadd(a,b,c=0,d=0):
    return a+b+c+d
print(myadd(10,20))
print(myadd(100,200,300))
print(myadd(1,2,3,4))
 