# 1.写一个函数mysum(n),此函数用来计算
# 1+2+3+4+…+n的和（要求：不能使用sum）
def mysum(n):
    he=0
    for i in range(1,n+1):
        he+=i
    return he
print(mysum(100))
print(mysum(4))

def mysum2(n):
    return sum(range(1,n+1))
print(mysum(100))
print(mysum(4))