# tuple1
# lis=[2,3,'k',['qwe',20,['k',['tt',3,'1']],89],'ab','adv']
# lis[3][2][1][0]='TT'
# print(lis)
# lis[3][2][1][0]=lis[3][2][1][0].upper()
# print(lis)
# lis.remove(3)
# lis.insert(1,'100')
# print(lis)
# lis[3][2][1][2]=101
# print(lis)
# li=[1,2,3]
# li[2]=33
# print(li)
# li=['taibai','alexC','AbC','egon','Ritian','Wusir','aqc']
# b=[]
# for i in li:
#     s=i.strip()
#     if (s.startswith("A")or s.startswith("a"))and s.endswith("c"):
#         b.append(s)
#     for x in b:
#         print(x)
# print("----------")
# for i in li:
#     s=i.strip()
#     if s[0].upper()=='A'and s[-1]=='c':
#         b.append(s)
#     for x in b:
#         print(x)
# tuple2
# name = [['100','张三'],['200','李四'],['300','王五']]
# def getName(sno):
#     for i in range(0,len(name)):
#         if sno==name[i][0]:
#             print(name[i][1])
#     return name
# getName('300')
# tuple3
# 11.素数计算输出
# 累计最终共有几个素数
h=0
# 
leap=1
# 从math模块中导入求根运算并命名为s
from math import sqrt as s
# 从101开始遍历
for m in range(101,201):
    # 将从101开始的数加１并转为int函数
    k = int(s(m+1))
    # 从2开始遍历
    for i in range(2,k+1):
        # 若从101开始的数对从2开始遍历的数取余为０
        if m % i == 0 :
            # 将leap置０并退出判断
            leap = 0
            break
    # 若leap为１
    if leap == 1 :
        # 打印是素数的数
        print("%-4d"%m,end=' ')
        h += 1
        # 累计１０个数换一次行
        if h % 10 == 0 :
            print("")
    
    leap = 1
print("The total is %d" % h)
# 12．水仙花数for循环
# 导入math模块
import math
# 在100到1000之间遍历
for i in range(100,1000):
    # 用math中的floor方法向下取整
    # 101/100 -->x=1
    x = math.floor(i/100)
    # 111-1*100=11 11/10-->y=1
    y = math.floor((i-x*100)/10)
    # 102-(102/10)-->10 *10 -->1 
    z = i - math.floor(i/10)*10
    # 水仙花数判断条件
    if i == x**3 + y**3 + z**3 :
        print(i)
# 13.分解质因数

