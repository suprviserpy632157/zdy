L=[]
while 1:
    n=input("please input name:")
    # 如果用户输入空字符串就结束输入
    if not n:
        break
    a=int(input("please input age:"))
    s=int(input("please input score:"))
    d = list()
    d['name']=n
    d['age']=a
    d['score']=s 
    L.append(d)
print('''+---------------+----------+----------+
|     name      |   age    |  score   |
+---------------+----------+----------+''')
for x in student_info:
    name = str(d['name'])
    age=str(d['age'])
    score = str(d['score'])
    print("|%s|%s|%s|"%(name.center(15),age.center(10),score.center(10))
print("+---------------+----------+----------+")