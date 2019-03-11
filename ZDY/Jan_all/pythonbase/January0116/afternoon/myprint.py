import sys
def myprint(*args,sep=' ',end='\n',file=sys.stdout,flush=False):    
    # 如果是第二次打印，则执行此语句
    flag=False  #当第一次循环后，将此变量置为True
    for x in args:
        if flag:
            file.write(sep)
        file.write(str(x))
        flag=True
    # 打印ned
    file.write(end)
    # return s

myprint("hello world")
myprint(1,2,3)
myprint(5,6,7,8,sep='#')
myprint(1,2,3,4,sep=',',end=' ')