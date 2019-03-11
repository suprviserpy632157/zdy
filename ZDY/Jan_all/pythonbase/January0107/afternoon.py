# 写程序，实现以下要求
# 用户输入一个整数代表这个季度，打印这个
# 季度的信息，用户输入的信息不在字典内打印不存在
# seasons={
#     1:'pring has 1,2,3month',
#     2:'summer has 4,5,6month',
#     3:'automn has 7,8,9month',
#     4:'winter has 10,11,12month'
#     }
# print(seasons)
# x=int(input("Please input a number(1-4):"))
# d={}
# d[1]='spring has 1,2,3month'
# d[2]='summer has 4,5,6month'
# d[3]='automn has 7,8,9month'
# d[4]='winter has 10,11,12month'
# if x in d:
#     print(d[x])
# else:
#     print("error")
# d={'name':'zdy','birthday':(1995,2)}
# for k in d:
#     print("键",k,'值',d[k])  
# 写一个程序，输入一个字符串，写程序统计
# 出这个字符串的字符个数字和每个字符的次数  
# s=input("Please input a string:")
# d=dict()
# for i in s:
#     #如果是第一次出现这个字符
#     if i not in d: 
#         d[i] = 1 
#     #如果不是第一次出现这个字符   
#     else:
#         d[i]+=1
# for k in d:
#     print("char",k,':',d[k],"per")
# # 生成一个字典，键为数字（１０）以内，值为键的平方
# d={x:x**2 for x in range(10)}
# print(d)
# 有如下字符串列表
# L=['tarena','xiaozhang','hello']
# 生成如下字典：
# d={'tarena':6,'xiaozhang':9,'hello':5}
# L=['tarena','xiaozhang','hello']
# d={k:len(k) for k in L}
# print(d)
# 已知有两个字符串列表：
Nos=[1001,1002,1005,1008]
names =['Tom','Jerry','Spike','Tyke']
d={}
for i in range(len(Nos)):
    d[Nos[i]]=names[i]
print(d)
# 改写
c={Nos[i]:names[i] for i in range(len(Nos))}
print(c)
a={}
for n in Nos:
    a[n]=names[Nos.index(n)]
print(a)
b={n:names[Nos.index(n)] for n in Nos}
print(b)