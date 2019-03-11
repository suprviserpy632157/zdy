# 生成一个１～９的平方的元组
# t=tuple()
# for i in range(1,10):
#     t+=(i**2,)
# print(t)
# 方法２
# L=[x**2 for x in range(1,10)]
# t=tuple(L)
# print(t)
# 方法3
# t=tuple(x**2 for x in range(1,10))
# print(t)
#方法４
g = (x**2 for x in range(1,10))
t=tuple(g)
print(t)
