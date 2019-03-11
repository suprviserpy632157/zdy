#１． 输入一个季度１～４输出这个季度有哪几个月，如果输入的不是１～４的整数，则提示用户“输入错误”
a = int( input("请输入数字：") )
if a=＝1:
    print(a,'有１２３月')
elif a=＝2:
    print(a,'有４５６月')
elif a=＝3:
    print(a,'有７８９月')
elif a=＝4:
    print(a,'有１０　１１　１２月')
else:
    print(a)
# ２．输入一年中的月份（１～１２），输出这个月有哪几个季度，如果输入的是其他数，则提示用户“输入错误”
b=int( input("请输入月份（１～１２）"))
if  1 <= b <= 3:
    print(b,'是第一季度')
elif 4 <= b <= 6:
    print(b,'是第二季度')
elif 7 <= b <= 9:
    print(b,'是第三季度')
elif 10 <= b <= 12:
    print(b,'是第四季度')
else:
    print("输入错误")
    

