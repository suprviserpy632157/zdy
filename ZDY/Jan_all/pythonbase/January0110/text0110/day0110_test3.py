# 3.写一个函数计算：
# 1+2**2+3**3+…+n**n的和
# （n给个小点的数来进行测试）
# 方法１
def mul_mi(n):
    a=0
    for i in range(1,n+1):
        a+=i**i
    return a
print(mul_mi(3))
# 方法２
def mysum(n):
    s=sum([x**x for x in range(1,1+n)])
    return s
print(mysum(3))
# 方法３
def mysum2(n):
    return sum(map(lambda x :x**x,range(1,n+1)))
print(mysum(3))
