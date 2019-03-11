# 3.修改之前的学生管理系统
#   要求添加4个功能
# |5) 按学生成绩高-低显示学生的信息|
# |6) 按学生成绩低-高显示学生的信息|
# |7) 按学生年龄高-低显示学生的信息|
# |8) 按学生年龄低-高显示学生的信息|
def show_menu():
    """显示菜单"""
    print('+---------------------------+')
    print('|1)添加学生信息               |')
    print('|2)显示学生信息               |')
    print('|3)删除学生信息               |')
    print('|4)修改学生信息               |')
    print('|5)按学生成绩高-低显示学生的信息|')
    print('|6)按学生成绩低-高显示学生的信息|')
    print('|7)按学生年龄高-低显示学生的信息|')
    print('|8)按学生年龄低-高显示学生的信息|')
    print('|q）退出                     |')
    print('+---------------------------+')
def input_student():
    L=[]
    while 1:
        n=input("请输入学生的姓名：")
        if not n:
            break
        a=int(input("please input age:"))
        if a>200 or a<0:
            print("请输入正确的年龄！")
            break
        s=int(input("please input score:"))
        if s>100 or s<0:
            print("请输入正确的分数！")
            break
        d = {}
        d['name']=n
        d['age']=a
        d['score']=s 
        L.append(d)
    return L
def output_student(L):
    print('''+---------------+----------+----------+
|     name      |   age    |  score   |
+---------------+----------+----------+''')
    for x in L:
        print("|",
                (x.get("name")).center(15),
                "|",
                str(x.get("age")).center(10),
                "|",
                str(x["score"]).center(10),
                "|",
                sep='')
    print('''+---------------+----------+----------+''')
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
            student_info['name']=newname
            student_info['age']=newage
            student_info['score']=newscore
            break
    else:
        print("没有学生信息，无法修改！")
def student_score_sort_h_l(L):
    def get_score(d):
        return d['score']
    L2=sorted(L,key=get_score,reverse=True)
    output_student(L2) 

def student_score_sort_l_h(L):
    L2=sorted(L,key=lambda d:d['score'])
    output_student(L2)
def student_age_sort_h_l(L):
    L2=sorted(L,key=lambda d:d['age'],reverse=True)
    output_student(L2)
def student_age_sort_l_h(L):
    L2=sorted(L,key=lambda d:d['age'])
    output_student(L2)
def main():
    #此列表用于保存学生数据
    infos=[]
    while 1:
        show_menu()
        s=input("请选择：")
        if s=="1":
            infos+=input_student()
        elif s=="2":
            output_student(infos)
        elif s=="3":
            del_stu(infos)
        elif s=="4":
            modify_stu(infos)
        elif s=="5":
            student_score_sort_h_l(infos)
        elif s=="6":
            student_score_sort_l_h(infos)
        elif s=="7":
            student_age_sort_h_l(infos)
        elif s=="8":
            student_age_sort_l_h(infos)
        elif s=="q":
            break                
main()