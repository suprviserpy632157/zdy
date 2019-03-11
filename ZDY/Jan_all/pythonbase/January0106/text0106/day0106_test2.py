# 2.有一些数存于列表中，如：
#   L=[1,3,2,1,6,4,2，…，98,82]
#   1）	将列表中出现数字存入到另一个列表L2中
#       要求：重复出现多次的数只在L2列表中保留一份（去重）
#   2）	将列表中出现两次的数字存于L3列表中，在L3列表中只保留一份
L2 = []
L =[1,2,1,3,6,4,4,2,3,98,2,82]
# import copy
# L2=copy.deepcopy(L)
# for i in L2:
#     if L2.count(i)>1 and (i in L2):
#         L2.remove(i)
for x in L:
    if x not in L2:
        L2.append(x)
print(L)
print(L2)
L3=[]
for j in L:
    if L.count(j)==2 and (j not in L3):
        L3.append(j)
print(L3)