# 输入某年某月某日，判断这一天是一年的第几天
year = int(input("please input a year:"))
month = int(input("please input a month:"))
day = int(input("please input a day:"))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12 :
    sum = months[month-1]
else:
    print("error")
    sum += day
leap = 0
if(year%400==0)or(year%4==0)and(year%100!=0):
    leap = 1
if(leap == 1 )and(month > 2):
    sum+=1
print("It's the %dth day"%sum)