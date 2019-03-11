def shoe_menu():
    """显示菜单"""
    print('+----------------------+')
    print('|1）添加学生信息         |')
    print('|2）显示学生信息         |')
    print('|3）删除学生信息         |')
    print('|4）修改学生信息         |')
    print('|q）退出                |')
    print('+----------------------+')
def input_student():
    L=[]
    while 1:
        n=input("please input name:")
        if not n:
            break
        a=int(input("please input age:"))
        s=int(input("please input score:"))
        d = {}
        d['name']=n
        d['age']=a
        d['score']=s 
        L.append(d)
    return L
def output_student(L):
    print('''+---------------+----------+----------+''')
    print('''|     name      |   age    |  score   |''')
    print('''+---------------+----------+----------+''')
    for d in L:
        name = str(d['name'])
        age=str(d['age'])
        score = str(d['score'])
        print("|%s|%s|%s|"%(name.center(15),
        age.center(10),
        score.center(10))
    print("+---------------+----------+----------+")
def del_stu(L):
    name=input("请输入学生的姓名：")
    #i代表列表的索引
    i=0
    while i<len(L):
        d=L[i]
        if d['name']==name:
            del L[i]
            print("删除",name,"成功")
            break
    else:
        print("删除失败")

def modify_stu(L):
    name=input("请输入学生的姓名：")
    for i in range(len(L)):
        d=L[i]
        if d['name']==name:
            newname=input("请输入修改后的姓名：")
            newage=int(input("请输入修改后的年龄："))
            newscore=int(input("请输入修改后的成绩："))
            L['name']=newname
            L['age']=newage
            L['score']=newscore
            break 
    else:
        print("没有学生信息，无法修改！")

def main():
    #此列表用于保存学生数据
    infos=[]
    while 1:
        shoe_menu()
        s=input("请选择：")
        if s=="1":
            infos+=input_student()
        elif s=="2":
            output_student(input_student)
        elif s=="3":
            del_stu(input_student)
        elif s=="4":
            modify_stu(input_student)
        elif s=="q":
            break                
main()