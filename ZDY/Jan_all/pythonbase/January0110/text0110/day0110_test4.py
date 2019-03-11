# 4.	实现带界面的学生信息管理系统
# 界面操作如下：
# +----------------------+
# |1）添加学生信息         |
# |2）显示学生信息         |
# |3）删除学生信息         |
# |4）修改学生信息         |
# |q）退出                |
# +----------------------+
# 学生信息包括：姓名，年龄，成绩，
# （与之前相同），每个功能写一个函数与之相对应
student_info=[]
def input_student():
    while 1:
        n=input("please input name:")
        # 如果用户输入空字符串就结束输入
        if not n:
            break
        a=int(input("please input age:"))
        s=int(input("please input score:"))
        # 每次创建一个新字典
        student_info.append({'name':n,"age":a,"score":s})
    return " "

def output_student(infos):
    print('''+---------------+----------+----------+
|     name      |   age    |  score   |
+---------------+----------+----------+''')
    for x in student_info:
        print("|",
                (x.get("name")).center(15),
                "|",
                str(x.get("age")).center(10),
                "|",
                str(x["score"]).center(10),
                "|",
                sep='')
    print('''+---------------+----------+----------+''')

def del_student(infos):
    delname =input("请输入要删除学生的姓名：")
    for temp in student_info:
        if temp['name']==delname:
            student_info.clear()
            print("successful")
            break
        print("查无此人，删除失败！")

def change_stuinfo(infos):
    changename=input("请输入要修改学生的姓名")
    while 1:
        changemass=int(input("1.修改学生的姓名\n2.修改年龄\n3.修改成绩"))
        if changemass==1:
            newname=input("请输入修改后的姓名：")
            for x in student_info:
                student_info['name']=newname
            print("姓名修改成功")
        elif changemass==2:
            newage=int(input("请输入修改后的年龄：")) 
            student_info['age']=newage
            print("age修改成功") 
        elif changemass==3:
            newscore=int(input("请输入修改后的成绩："))
            student_info['score']=newscore
            print("score修改成功") 
    print("没有学生信息，无法进行修改操作！")

def main():
    #此列表用于保存学生数据
    infos=[]
    while 1:
        print("1)添加学生信息")
        print("2)显示学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")
        print("q)退出")
        s=input("请选择：")
        if s=="1":
            infos+=input_student()
        elif s=="2":
            output_student(input_student)
        elif s=="3":
            del_student(input_student)
        elif s=="4":
            change_stuinfo(input_student)
        elif s=="q":
            break                
main()