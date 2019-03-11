# raise2.py
def make_except():
    print("函数开始...")
    # raise ZeroDivisionError
    error = ValueError("这是故意制造的错误!!!")
    raise error #发错误通知
    print("函数结束")
try:
    make_except()
    print("make_except调用完毕!")
except ZeroDivisionError:
    print("make_except函数调用发生异常")
except ValueError as err:
    print("发生了值错误!!!")
    print("err=",err)
print("程序正常退出!")