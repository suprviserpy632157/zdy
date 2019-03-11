# #1.
# for i in [1,2]:
#     for j in [1,2,3]:
#         print(i,j)
#         break    结束的是内层ｆｏｒ循环
#     else:
#         print("for_j")
# else:
#     print("for_j") 
# 2.
s="Python2best"
s1=[3,5,4,2]
s2=[]
s2+=s
print(s2)
s2[5:]="3"
s2+='!'
print(s2)
print(len(s2))
print(s2.pop(len(s2) -2))
s2.clear()
sum = 0
for x in s1:
    sum+=x
print(sum)

