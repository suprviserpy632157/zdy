#已知有列表：
# １．写一个生成器函数，让此函数能够
# 动态提供数据，数据为原列表的数字平方加１
# ２．写一个生成器表达式，让此函数能够
# 动态提供数据，数据为原列表的数字的平方加１
# ３．创建一个列表，此列表内的数据为原列表Ｌ的数字的平方和加１
L=[2,3,5,7]
def fun(lst):
    for x in lst:
        yield x**2+1
for x in fun(L):
    print(x)

g=(x**2+1 for x in L)
for x in g:
    print(x)
# for x in (b**2+1 for b in L):
#     print(x)

L=[x**2+1 for x in L]
print(L)