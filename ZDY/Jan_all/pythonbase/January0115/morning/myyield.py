# myyield
# 此实例示意生成器函数的定义和使用
def myyield():
    print("即将生成２")
    yield 2  #生成２
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("myyield函数运行结束!")
for x in myyield():
    print(x)
print("程序正常结束!")
# g=myyield() #生成器函数调用将返回生成器对象，ｇ绑定一个生成器
# # print(g)
# it=iter(g) #让生成器提供迭代器
# print(next(it))  #2
# print(next(it))
# print(next(it))
# print(next(it))