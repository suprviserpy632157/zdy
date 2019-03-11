# 练习
# 猜数字游戏随机生成一个0~100之间的数字，用变量ｘ绑定让用户循环输入一个整数，
# 用变量ｙ绑定输出猜数字的结果如果ｘ＝ｙ成功，ｙ>x“您猜大了”,ｙ<ｘ“您猜小了”直到猜对为止
import random
# x=random.randrange(0,101)
x=random.randint(0,100)
count=0
while 1:
    y=int(input("输入一个整数:"))
    count+=1
    if y==x:
        print("您猜对了!")
        break
    elif y>x:
        print("您猜大了!")
    elif y<x:
        print("您猜小了!")
print("您共猜了%d次"%count)