def myfun1(a):
    global a
    a = 111
    b = 222
    def myfun2(b):
        nonlocal b
myfun1(3)
# 结果会出错，因为函数中的形参名不能
# 和global变量名或者nolocal变量名相同