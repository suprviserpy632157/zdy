# 1.写程序算出1~20的阶乘的和，即：
# 　　　　1！+2！+…+20！
def mysum(n):
    if n==1:
        return 1
    def f(n):
        if n==1:
            return 1
        return f(n-1)*n
    return mysum(n-1)+f(n) 
print(mysum(20))
# 方法２
def myfac(x):
    if x==0:
        return 1
    return x*myfac(x-1)
print("he",sum(map(myfac,range(1,21))))
# s=0
# for x in range(1,21):
#     s+=myfac(x)
# print(s)
