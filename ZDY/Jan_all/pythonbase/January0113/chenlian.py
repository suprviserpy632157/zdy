import time
def myfn(n):
    """myfn函数是输出n遍"hello world"n为参数"""
    if n ==0:
        return 
    print("hello world")
    time.sleep(1)
    return myfn(n-1)
print(myfn(3))
a=myfn
print(a.__name__)
print(myfn.__name__)

from math import pi
print(pi)
