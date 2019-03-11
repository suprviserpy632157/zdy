# 2.写一个函数myfac(n),用来计算n！
def myfac(n):
    jie=1
    for i in range(1,n+1):
        jie*=i
    return jie
print(myfac(5))
# 递归求n！
def myfac2(n):
    if n==0:
        return 1
    else:
        return n*myfac2(n-1)
print(myfac2(5))
