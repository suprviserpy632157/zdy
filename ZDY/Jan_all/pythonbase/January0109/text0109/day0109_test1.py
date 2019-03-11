# 1.算出100~999以内的水仙花数
# 水仙花数是指百位的3次方加上
# 十位的三次方加上个位的3次方等于原数的整数
# eg：153=1**3+5**3+3**3
for i in range(100,1000):
    bai = i//100
    shi = i//10%10
    ge =i%10
    if i == bai**3+shi**3+ge**3:
        print(i,"是水仙花数")
# 方法２
for x in range(100,1000):
    s=str(x)
    bai=int(s[0])
    shi=int(s[1])
    ge=int(s[2])
    if x == bai**3+shi**3+ge**3:
        print(x,"是水仙花数")
# 方法3
for bai in range(1,10):
    for shi in range(0,10):
        for ge in range(10):
            x = bai*100+shi*10+ge
            if x == bai**3+shi**3+ge**3:
                print(x,"是水仙花数")
