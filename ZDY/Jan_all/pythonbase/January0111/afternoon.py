# def story():
#     print("从前有座山，山上有座庙，庙里有个老和尚讲故事")
#     story()
# story()

# def fx(n):
#     print('递归进入第',n,'层')
#     if n ==3:
#         return
#     fx(n+1)
#     print("递归退出第",n,'层')
# fx(1)
# print("程序退出")

#写一个递归函数,此函数求
# １＋２＋３＋４＋５＋．．．＋ｎ的和
# def mysum(n):
#     if n==1:
#         return 1
#     return n+mysum(n-1)
# print(mysum(100))

# 练习
# 已知有５位朋友在一起
# 第５个人说他比第４个人大２岁
# 第４个人说他比第３个人大２岁
# 第３个人说他比第２个人大２岁
# 第２个人说他比第１个人大２岁
# 第一个人说他１０岁
# def fivefriends(n):
#     if n==1:
#         return 10
#     else:
#         n=2+fivefriends(n-1)
#         return n
# print("第５个人的年龄为：",fivefriends(5))
# print("第３个人的年龄为：",fivefriends(3))

# closure.py
# 用全局变量保存压岁钱
# money=1000
# def child_buy(obj,m):
#     global money
#     if money > m:
#         money -= m
#         print('买',obj,'花了',m,'元，\
# 剩余',money,'元')
#     else:
#         print("买",obj,'lose')
# child_buy("变形金刚",200)
# child_buy("漫画三国",100)
# child_buy("手机",1300)
# 用局部变量保存压岁钱
# def child_buy(obj,m):
#     money=1000
#     if money > m:
#         money -= m
#         print('买',obj,'花了',m,'元，\
# 剩余',money,'元')
#     else:
#         print("买",obj,'lose')
# child_buy("变形金刚",200)
# child_buy("漫画三国",100)
# child_buy("手机",1300)

# def give_yasuiqian(money):
#     def child_buy(obj,m):
#         nonlocal money
#         if money > m:
#             money -= m
#             print('买',obj,'花了',m,'元，剩余',money,'元')
#         else:
#             print("买",obj,'lose')
#     #返回内嵌函数的引用关系
#     return child_buy
# cb=give_yasuiqian(1000)
# cb("变形金刚",200)
# cb("漫画三国",100)
# cb("手机",1300)

# closure_make_power.py
# 此实例示意闭包的应用
# 生成若干个次方
def make_power(y):
    def fn(x):
        return x**y
    return fn
pow2=make_power(2)
print("5的平方是：",pow2(5))
print("6的平方是：",pow2(6))
pow3=make_power(3)
print("7的立方是：",pow3(7))