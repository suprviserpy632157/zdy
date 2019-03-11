# 输入一个整数１～１２代表月份，打印这个月在哪个季度

month = int( input ( '月份（１～１２）'))
if 1<=month<=12:
    print("合法的月份")
    if month<=3:
        print("spring")
    elif month<=6:
        print("summer")
    elif month<=9:
        print("automn")
    elif month<=12:
        print("winter")
else:
    print("error")