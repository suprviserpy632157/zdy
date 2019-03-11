year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日子："))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0　<= month <= 12:
    sum = months[month-1]
else:
    print('error')
    


