# pass.py
# 让程序输入一个学生的成绩（０～１００），不在这个范围则报错

score = int(input("请输入学生的成绩（０～１００）"))
if 0<=score<=100:
    # print("这个学生的成绩是：",score)
    pass
else:
    print("输入有误！！！")