def input_student():
    L=[]
    while 1:
        n=input("please input name:")
        # 如果用户输入空字符串就结束输入
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
        print("|%s|%s|%s|"%(name.center(15-get_chinese_char_count(name)),
        age.center(10),
        score.center(10))
    print("+---------------+----------+----------+")
infos=input_student()
print(infos)
output_student(infos)