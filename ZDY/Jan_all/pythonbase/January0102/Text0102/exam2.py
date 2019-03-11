# 输入一个数，用ｉｆ语句、表达式计算这个数的绝对值，并打印数的绝对值

a = int(input("请输入一个数："))
if a <= 0:
    b = abs(a)
    print(b)
else:
    print(a)

x = int( input ("请输入一个数："))
result = -x if x < 0 else x
print(x,'的绝对值是：',result)