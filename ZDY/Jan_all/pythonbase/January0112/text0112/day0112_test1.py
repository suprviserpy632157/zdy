# 1.编写函数fun，其功能是计算并返回下列多项式的和
# sn=1+1/1！+1/2！+1/3！+…+1/n！
# 建议用数学模块中的math.factorical（x）函数
# 求当n=20时，sn的值
# def fun(n):
#     from math import factorial as fac
#     s=0
#     if n==0:
#         return 1
#     else:
#         return 1/n*1/fac(n-1)
# print("he=",sum(map(fun,range(0,21))))
    # return sum([1/fac(x) for x in range(1+n)])

def fun2(n):
    from math import factorial as fac
    sn=0
    for x in range(0,n+1):
        sn+=1/fac(x)
    return sn
print(fun2(20))

