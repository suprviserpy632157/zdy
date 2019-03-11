# 编写代码，１－７七个数字，分别代表周一到周日，如果输入的
# 数字是６或７输出＂周末＂，１－５输出＂工作日＂，其他输出＂错误＂
num = int(input("please input a number:"))
if num == 6 or num == 7 :
    print("weekend")
elif  1 <= num <= 5 :
    print("workday")
else:
    print("error") 