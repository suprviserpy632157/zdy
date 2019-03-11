# 写程序求：
# 1/1+1/3+1/5+1/7+……+1/99的和
i = 1
he = 0 # 用于累加
while i < 100 :   
    he += 1/i
    i += 2
print(he)

sum = 0
for x in range(1,100,2):
    sum += 1/x
print(sum) 