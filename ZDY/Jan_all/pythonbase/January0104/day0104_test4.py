# 写程序求：
#     1/1-1/3+1/5-1/7+……+（+-）1/（2*n-1）
#     1）	求当n取1000000时这个算式的和
#     2）	求当n取1000000时这个算式的和*4
#           是多少（3.1415…）
# n = int(input("please give a number:"))
# i = 1
# j = 0
# k = 0
# count = 0
# while i <= n :
#     j += 1/i
#     count += 1
#     if count%2 == 0 :
#         k = (1/i) *(-1)
#         j = 1/(i-2) 
#     i += 2
# print(j+k)
# print((j+k)*4)
s=0 #累加和
n = 1 #分母
sign = 1 # 符号
while n<=1000000:
    s+=sign*1/(2*n-1)
    sign *= -1 # 改变符号的正负号
    n+=1
print("s=",s)
print("4*s=",4*s)   
    