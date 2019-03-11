#exception.py 
def f1():
    err=ValueError("一个错误")
    raise err
def f2():
    f1()
def f3():
    f2()
def f4():
    f3()
try:
    f4()
except ValueError as err:
    print(err)
