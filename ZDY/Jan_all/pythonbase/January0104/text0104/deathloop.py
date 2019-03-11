# 任意输入一些整数，当输入负数时结束，输入完成后，打印输入的
# 数字和
s=0 #记录累加和

while True :
    nums = int(input("please input a number:"))
    if nums < 0:
        break
    s+=nums
print("sum=",s)
