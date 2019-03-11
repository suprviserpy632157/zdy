#iterator.py
L=[2,3,5,7]
#如何遍历Ｌ中的数据
# # 1
# i=0
# while i<len(L):
#     x=L[i]
#     print(x)
#     i+=1
# # 2
# for x in L:
#     print(x)
# 3 用迭代器遍历
it=iter(L)
while 1:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
