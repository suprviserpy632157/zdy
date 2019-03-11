# lambda.py
# def myadd(x,y):
#     return x+y
# myadd=lambda x,y:x+y
# print("20+30=",myadd(20,30))
# print("1+2=",myadd(1,2))
# 练习：
# 写一个lambda表达式
# 　fx=lambda n:...
# 此表达式创建的函数判断ｎ这个数的２次方
# 加１能否被５整除，能返回ｔｒｕｅ,否则
# 返回ｆａｌｓｅ
# # fx=lambda n:True if (n**2+1)%5==0 else False
# fx=lambda n: (n**2+1)%5==0
# print(fx(3))
# print(fx(4))
# 2.写一个lambda表达式来创建函数，
# 此函数返回两个形参变量的最大值
# # def mymax(x,y):
# #     if x>y:
# #         return x
# #     return y
# mymax = lambda x,y:x if x>y else y
# print(mymax(100,200))
# print(mymax("100","20"))
# def fx(f,x,y):
#     print(f(x,y))
# fx((lambda a,b:a+b),100,200)
# fx((lambda a,b:a*b),3,4)