# assert.py
# 获取学生成绩
def get_score():
    s =int(input("请输入学生的成绩："))
    # assert 0<=s<=100,'成绩超出范围!'
    if bool(0<=s<=100)==False:
        raise AssertionError('成绩超出范围!')
    return s
try:
    score = get_score() 
    print("学生成绩为：",score)
except AssertionError:
    print("断言失败!")
print("程序正常退出!")
