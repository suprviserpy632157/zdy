# 1
# import pdb
# pdb set_trace()
# python3 -m pdb ***.py

# 2.
def student_info():
    while 1:
        n=input("请输入学生姓名：")
    try:
        a=int(input("请输入学生的年龄："))
        s=int(input("请输入学生的成绩:"))
    except ValueError:
        print("输入有误，请重新输入学生信息!")
    except KeyboardInterrupt:
        print("程序退出")
        break 
    

