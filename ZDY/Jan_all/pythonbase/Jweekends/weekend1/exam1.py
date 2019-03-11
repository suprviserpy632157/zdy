# 有４个数字：１２３４，能组成多少个互不相同且无重复数字的三位数？
# 各是多少？
# bai = 0
# shi = 0
# ge = 0
# i = int(input("please give a number:"))
# j = int(input("please give a number:"))
# k = int(input("please give a number:"))
# if i>4 or i<1 or j>4 or j<1 or k>4 or k<1 :
#     print("range is 1 to 4 !")
# elif i==j or j==k :
#     print("i,j,k is different number!")
# else:
#     while i <= 4 :
#         bai = i
#         while j != bai and j<=4:
#             shi = j
#             while k!= bai and k!=shi and k<=4:
#                 ge = k
#                 print("%d%d%d"%(bai,shi,ge))
#                 k+=1  
#             j+=1
#         i+=1
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if x!=y and x!=z and y!=z :
                print("%d%d%d"%(x,y,z))
x=1
a=0
while x<=4: 
    y=1
    while y<=4:
        z=1
        while z<=4:
            if x!=y and x!=z and y!=z:
                a+=1
                print("%d%d%d"%(x,y,z))
            z+=1
        y+=1
    x+=1
print(a)