n=int(input("please input a number:"))
count=1
def f(n,a,b,c):
    global count
    if n==1:
        print("%d:\t%s-->%s"%(count,a,c))
        count+=1
    else:
        f(n-1,a,c,b)
        f(1,a,b,c)
        f(n-1,b,a,c)
f(n,'A','B','C')