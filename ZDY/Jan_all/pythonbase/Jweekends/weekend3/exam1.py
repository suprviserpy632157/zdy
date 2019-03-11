# 1.每次考试之后，教师都要统计考试成绩，
# 一般包括：平均分，对所有人按成绩从高到低排列，
# 谁成绩最好，谁成绩最差。
stu={'沃利贝尔':100,'璐璐':99,'奥菲那':92,'贾克斯':97,'伊泽瑞尔':96}
def average(x):
    score=x.values()
    scores=0
    for i in score:
        scores=scores+int(i)
        ave=scores/len(score)
    return(ave)
print("5位的平均分是：", average(stu))
def stu_sort(x):
    arr_l=[]
    for k in x:
        y=(x[k],k)
        arr_l.append(y)
        h_l=sorted(arr_l,reverse=True)
        y2=[]
        for k1 in h_l:
            y3=(k1[1],k1[0])
            y2.append(y3)
    return y2
print("５人成绩从高到低：",stu_sort(stu))
def stu_max(x):
    z=stu_sort(x)
    z2=z[0][1]
    z3=[]
    for k in z:
        if k[1]==z2:
            z3.append((k[0],k[1]))
    return z3
print("成绩最好的是：",stu_max(stu))
def stu_min(x):
    s=stu_sort(x)
    s2=s[len(s)-1][1]
    s3=[]
    for k in s:
        if k[1]==s2:
            s3.append((k[0],k[1]))
    return s3
print("成绩最差的是：",stu_min(stu))