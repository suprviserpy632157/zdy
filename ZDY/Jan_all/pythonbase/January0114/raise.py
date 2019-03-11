# raise.py
def make_except():
    print("函数开始...")
    # int("aaaaa") #int函数内抛出异常
    # raise ValueError #触发ValueError类型的异常
    raise ZeroDivisionError
    print("函数结束")
try:
    make_except()
    print("make_except调用完毕!")
except ValueError:
    print("make_except函数调用发生异常")
print("程序正常退出!")