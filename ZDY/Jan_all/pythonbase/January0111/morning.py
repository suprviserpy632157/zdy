# map.py
# 此实例示意ｍａｐ的用法
# def power2(x):
#     return x**2
# print(sum(map(power2,range(1,10))))
# # 生成一个可迭代对象，此
# # 可迭代对象可以生成
# # １～９自然数的平方
# for x in map(power2,range(1,10)):
#     print(x)
# 生成一个可迭代对象，此可迭代对象可以生成
# １＊＊４，２＊＊３，３＊＊２，４＊＊１
# for x in map(pow,[1,2,3,4],[4,3,2,1]):
#     print(x)
# for x in map(pow,[1,2,3,4],[4,3,2,1,0],range(5,10)):
#     print(x)
# 练习１
# 求1**2+2**2+3**2+...+9**2的和
# 求1**3+2**3+3**3+...9**3的和
# 求1**9,2**8,3**7+...+9**1的和
# print(sum(map(power2,range(1,10))))
# print(sum(map(lambda x:x**2,range(1,10))))
# print(sum(map(pow,range(1,10),[3]*9)))
# print(sum(map(pow,range(1,10),range(9,0,-1))))

# filter.py
# 此实例示意fliter的用法
# def is_odd(x):
#     "判奇"
#     return x%2==1
# # 打印１～２０的奇数
# for x in filter(is_odd,range(20)):
#     print(x)
# print("---------------------")
# for x in filter(lambda x :x%2==1,range(10)):
#     print(x)

# 生成２０以内的全部偶数
# L=list(filter(lambda x:x%2==0,range(20)))
# print(L)
# L2=[x for x in filter(lambda x:x%2==0,range(20))]
# print("L2=",L2)

# 练习：
# 用filter生成能够提供偶数的可迭代对象，
# 生成将1~20的偶数，将这些偶数存于列表中
# L=list(filter(lambda x:x%2==0,range(1,20)))
# print(L)
# # 用ｆｉｌｔｅｒ函数将1~100
# # 之间所有的素数ｐｒｉｍｅ放入到列表中
# def is_prime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# L1=list(filter(is_prime,range(100)))
# L2=[x for x in filter(is_prime,range(100))]
# L3=[x for x in range(100) if is_prime(x)]
# print(L1)
# print(L2)
# print(L3)

# L=[5,-2,-4,0,3,1]
# L1=sorted(L,key=abs)
# print(L1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
# names=['Tom','Jerry','Spike','Tyke']
# print(sorted(names,key=len))

#练习：排序的依据为字符串的反序
names=['Tom','Jerry','Spike','Tyke']
def is_reverse(x):
    "x绑定需要排序的可迭代对象提供的元素"
    r=x[::-1]
    print("要排序的元素",x,"排序的依据是：",r)
    return r
print(sorted(names,key=is_reverse))