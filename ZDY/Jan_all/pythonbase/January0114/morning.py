# 写一个函数get_score()来获取学生输入的成绩(0~100)的整数
# 如果输入出现异常，则此函数返回０，否则返回用户输入的成绩
def get_score():
    s=int(input("please input number(0~100):"))
    if s<0 or s >100:
        return 0
    return s
try:
    score=get_score()
except:
    score=0
# else:
#     print(score)
print("student's score is :",score)
