alist=['hello','world']
for i,v in enumerate(alist):
    print('index',i,':',v)

f=open("student_info.txt",'w')
f.write("name: Bob  age:30  score:90")
f.write("name: Bob  age:30  score:90")
f.close()
def myyield():
    f=open("student_info.txt",'r')
    while 1:
        n=f.readline()
        if not n:
            break
        yield n
for x in myyield():
    print(x) 