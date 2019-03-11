# 3.改写之前的学生信息管理程序
# 用两个函数来封装功能代码块
#    函数1：input_student()   返回学生信息字典的列表
#    函数2：output_student(L)   打印学生信息的表格
# def input_student()：
# …
#    def output_student(L)
#         …
# Infos = input_student()
# print（infos）  #打印列表[{…},{…}]
# output_student(infos)     #根据实参infos打印表格
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
        # t=((d["name"]).center(15),
        #    str(d["age"]).center(10),
        #    str(d["score"]).center(10))
        # line = "|%s|%s|%s|"%t
        # print(line)
        print("|",
                (x.get("name")).center(15),
                "|",
                str(x.get("age")).center(10),
                "|",
                str(x["score"]).center(10),
                "|",
                sep='')
    print('''+---------------+----------+----------+''')

infos=input_student()
print(infos)
output_student(infos)