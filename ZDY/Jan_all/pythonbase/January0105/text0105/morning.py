# # 1.任意输入一段字符串
# # １）计算出这个字符串中空格的个数，并打印出这个个数
# # 　（要求只用ｆｏｒ语句，不允许使用ｓ．ｃｏｕｎｔ方法）
# # ２）计算出字符串中全部英文字母（Ａ－Ｚ和ａ－ｚ）的个数
# # 　　并打印这个个数
# # 思考：能否用ｗｈｉｌｅ语句实现上述功能
# a = input("plesae input a string:")
# blanks_count = 0
# alaph_count = 0
# i = 0  #i代表字符串的索引
# while i < len(a):  
#     ch = a[i]
#     #　统计个数
#     if ch == " ":
#         blanks_count += 1
#     if 65<=ord(ch)<65+26 or 97<=ord(ch)<97+26:
#         alaph_count += 1
#     i+=1 
# # 遍历输入的字符串，当有字符串有＂　＂时，blanks_count加１
# for ch in a :
#     if ch == " ":
#         blanks_count += 1
# print(" The number of space is: ",blanks_count)
# for b in a :
#     if 65<=ord(b)<65+26 or 97<=ord(b)<97+26:
#         alaph_count += 1       
# print("The number of alaph is:",alaph_count)
# # ２．输入一个字符串，从尾到头输出这个字符串
# a = input("plesae input a string:")
# for ch in a[::-1] :
#     print(ch)
# # 用ｗｈｉｌｅ循环
# i=len(a)-1
# while i >= 0:
#     print(a[i])
#     i-=1
# # 1.用ｆｏｒ语句打印１－２０的整数，打印在一行内
# for x in range(21):
#     print(x,end = " ")
# print()
# # 2.求１００以内有那些整数与自身＋１的乘积在对１１求余的结果＝８，打印出这些数
# for x in range(101):
#     if x*(x+1)%11==8:
#         print(x,end = " ")
# print()
# # 3.计算１＋３＋５＋７＋．．．＋９９的和分别用ｆｏｒ和ｗｈｉｌｅ语句实现
# sum = 0
# for x in range(1,100,2):
#     sum+=x
# print(sum)

# he = 0
# i = 1
# while i<100:
#     he+=i
#     i+=2
# print(he)
# １．输入一个整数，打印正方形的宽和高，打印相应的正方形
a = int(input("please input a number:"))
for _ in range(1,a+1) :
    for y in range(1,a+1):
        print(y,end=" ")
    print()
print()

# 2.输入一个整数，打印正方形的宽和高，打印相应的正方形
b=int(input("please input a number:"))
for x in range(1,b+1):
    #打印一行从ｘ开始的ｂ个数字
    for y in range(x,b+x):
        print("%2d"%y,end=" ")  
    print()
print()