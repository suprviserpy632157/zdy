# # 1.continue.py
# for x in range(0,5):
#     if x ==2 :
#         continue #之后的所有语句都不会执行
#     print(x)
# 2.打印１０以内的偶数
# for x in range(10):
#     # 如果ｘ是奇数则跳过本次循环
#     if x%2 ！=0 :
#         continue
#     print(x)
# 3.
# x=0
# while x<5:
#     if x==2:
#         x+=1
#         continue
#     print(x)
#     x+=1
# 打印１０以内的偶数（用ｗｈｉｌｅ＋
# ｃｏｎｔｉｎｕｅ采用跳过奇数的方式）
# x = 0
# while x<10:
#     if x%2==1:
#         x+=1
#         continue
#     print(x)
#     x+=1
# continue常用用法
# 求１到１００以内所有不能被２，３，５，７中
# 任意一个数整除的数的和（用continue实现）
he = 0
for x in range(1,101):
    if (x%2==0) or (x%3==0) or (x%5==0) or (x%7==0):
        continue 
    he += x
print(he)

add = 0
i = 1
while i < 101 :
    if (i%2==0) or (i%3==0) or (i%5==0) or (i%7==0):
        i+=1
        continue
    add+=i
    i+=1
print(add)