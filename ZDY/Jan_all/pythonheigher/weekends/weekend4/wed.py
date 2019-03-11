#16.日期格式应用
# import datetime
# if __name__=="__main__":
#     # 输出今日日期，格式为dd/mm/yyyy
#     print(datetime.date.today().strftime("%d/%m/%Y"))
#     # 创建日期对象
#     birthday = datetime.date(1995,2,2)
#     print(birthday.strftime("%d/%m/%Y"))
#     # 日期算术运算
#     birthday_nextday = birthday +datetime.timedelta(days=1)
#     print(birthday_nextday.strftime("%d/%m/%Y"))
#     # 日期替换(年)
#     new_birthday = birthday.replace(year=birthday.year+1)
#     print(new_birthday.strftime("%d/%m/%Y"))
# 17.辨别字符类型
# # 导入string模块
# import string
# # 输入字符串
# s = input("input a string:\n")
# # 记录letters,space,digit,others
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print("char=%d,space=%d,digit=%d,others=%d"%(letters,space,digit,others))
# 18.简单的数学计算
# a = int(input("please input number:"))
# count = int(input("add numbers:"))
# res = 0
# for i in range(1,count+1):
#     t=0
#     for j in range(i):
#         t=t+10**j
#     res = res + (a*t)
# print(res)
# 19.完数计算
# from sys import stdout
# for j in range(2,1001):
#     k=[]
#     n=-1
#     s=j
#     for i in range(1,j):
#         n+=1
#         s-=i
#         k.append(i)
#     if s==0:
#         print(j)
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write('')
#         print(k[n])
