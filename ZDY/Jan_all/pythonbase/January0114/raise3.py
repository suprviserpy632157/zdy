# 此实例示意用raise无参调用来传递异常信息
def f1():
    print("f1开始．．．")
    raise ValueError("f1内部发生错误!")
    print("f1结束！！！")
def f2():
    try:
        f1()
    except ValueError as e:
        print("f2中已收到f1中发生的错误：",e)
        raise 
try:
    f2()
except ValueError as err:
    print("主程序中已收到f2中发生的错误:",err)