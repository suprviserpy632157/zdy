# student.py
def input_student():
    L=[]
    while 1:
        n=input("请输入学生的姓名：")
        if not n:
            break
        try:
            a=int(input("please input age:"))
        except ValueError:
            print("您的输入有错，请重新输入!!!")
            continue
        if a>140 or a<0:
            print("请输入正确的年龄！")
            break
        try:
            s=int(input("please input score:"))
        except ValueError:
            print("您的输入有错，请重新输入!!!")
            continue
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
        i+=1
    else:
        print("删除失败")

def modify_stu(L):
    name=input("请输入学生的姓名：")
    for i in range(len(L)):
        d=L[i]
        if d['name']==name:
            newname=input("请输入修改后的姓名：")
            newage=input("请输入修改后的年龄：")
            newscore=input("请输入修改后的成绩：")
            L['name']=newname
            L['age']=newage
            L['score']=newscore
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
def stu_read():
    L=[] #先创建一个准备存放文件的列表
    try:
        # １．打开文件
        # f=open("./si.txt")
        # f=open("/home/tarena/test/student_project/si.txt")
        f=open("si.txt")
        # print("文件打开成功")
        # 2.读取文件
        try:
            while True:
                line = f.readline() #读取一行
                if not line:
                    break
                s=line.strip() #去掉左右两端的空白字符
                lst=s.split(",")
                n=lst[0]
                a=int(lst[1])
                scr=int(lst[2])
                d=dict(name=n,age=a,score=scr)
                L.append(d)
        # s=f.read() #读取全部内容
        # print("读取字符的个数是：",len(s)) #+回车键了
        # print("文件的内容是：",s)
        finally:
            # 3.关闭文件
            f.close()
            print("读取数据成功")
    except OSError:
        print("读取数据失败")
    except ValueError:
        print("数据类型错误")
    return L

def save_to_file(L):
    try:
        f=open("si.txt",'w')
        # 循环写入每个学生的信息
        for d in L:
            # 每次写入一个学生的信息
            f.write(d['name'])
            f.write(',')
            f.write(str(d['age']))
            f.write(',')
            f.write(str(d['score']))
            f.write('\n')
        f.close()
        print("保存成功")
    except OSError:
        print("打开文件失败")
# L=[dict(name='xiaozhang',age=20,score=100),
# dict(name='xiaoli',age=18,score=98)]

# save_to_file(L)