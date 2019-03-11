# # 已知有列表：Ｌ＝[３，５]
# # １）用索引和切片操作，将原序列改为　
# # 　　Ｌ=[1,2,3,4,5,6]
# L = [3,5]
# L[0:0]=[1,2] #1235
# L[3:3]=[4]   #12345
# L[len(L):]=[6]
# print(L)
# #  2)将列表反转，删除最后一个元素后，打印此列表
# # 　　．．．
# # 　　ｐｒｉｎｔ（Ｌ） #［６，５，４，３，２］
# L1=L[::-1]  #654321  会改变id
# L[::]=L[::-1]  #不会改变id
# del L1[5]   #或del L1[-1]
# print(L1)
# 1.写程序，让用户循环输入一些正整数，当输入－１时结束输入，
# 将这些整数存于列表Ｌ中
# １）打印出您共输入了几个有效的数（不算结束的－１）
# ２）打印输入数的最大值
# ３）打印输入数的最小值
# ４）打印输入数的平均值
# L=[]
# while 1:
#     num=int(input("Please input number:"))
#     if num == -1:
#         break
#     L+=[num]
# print(len(L))
# print(max(L))
# print(min(L))
# print(sum(L)/len(L))
# 写程序，让用户输入两个或以上的正整数，
# 当输入小于０的数时结束输入（不允许输入重复的数）
# １）打印这些数的和
# ２）打印最大数
# ３）打印这些数最二大的数
# ４）删除最小的一个数,并打印列表
a=[]
while 1:
    x = int(input("Please input number:"))
    if x <0 :
        if len(a)<2:
            print("您输入的数字太少")
            continue
        break
    if x not in a:
        a+=[x]
print("he=",sum(a))
L=sorted(a)
print("max=",L[-1])
print("max2=",L[-2])
min_number =L[0]
for i in range(len(a)):
    if a[i]==min_number:
        del a[i]
        break
print("del min list = ",a)
