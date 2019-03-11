# 看下列语句块的输出结果是什么？为什么？
# L=[2,3,5,7]
# A=[x*10 for x in L]
# it=iter(A)
# print(next(it))
# L[1]=33
# print(next(it))
# print("------------")
# L=[2,3,5,7]
# A=(x*10 for x in L)
# it=iter(A)
# print(next(it))
# L[1]=33
# print(next(it))

numbers=[10086,10000,10010,95588]
names=['中国移动','中国电信','中国联通']
d=dict(zip(numbers,names))
for t in zip(numbers,names,range(1,10000),range(1,3)):
    print(t)
# for i in zip(numbers,names):
#     print("i=",i)
# for n,na in zip(numbers,names):
#     print(na,'的客服电话是：',n)
# print(d)