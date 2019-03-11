# 定义一个三位数的整数，
#    要求使用算术运算符取出这个三位数的每一位
#    并计算这三个位数的数字之和。
# ** 　//是取整，　　/ 是求商
num = int(input("please give a number(3 status)"))
bai = num//100
shi = (num-bai*100)//10
ge  = num % 10
print("%d+%d+%d=%d"%(ge,shi,bai,bai+shi+ge))

n = 10
n += 20
print(n)

i = 10 
j = 20
if i + 10 > 20  and  j == 20 :
    print("true")
else:
    print("false")