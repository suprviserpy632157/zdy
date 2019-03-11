# 3.《学生信息管理项目》
# 输入任意个学生的姓名，年龄，成绩，
# 每个学生的信息存入字典，然后放入列表中，
# 每个学生的信息需要手动输入，
# 当输入姓名为空时，结束输入
# 创建一个空列表
student_info=[]
while 1:
    n=input("please input name:")
    # 如果用户输入空字符串就结束输入
    if not n:
        break
    a=int(input("please input age:"))
    s=int(input("please input score:"))
    # 每次创建一个新字典
    student_info.append({'name':n,"age":a,"score":s})
print('''+---------------+----------+----------+
|     name      |   age    |  score   |
+---------------+----------+----------+''')
for x in student_info:
    print("+",
            (x.get("name")).center(15),
            "|",
            str(x.get("age")).center(10),
            "|",
            str(x["score"]).center(10),
            "|",
            sep='')
print('''+---------------+----------+----------+''')