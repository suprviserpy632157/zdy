from greenlet import greenlet
# 执行test1,执行test2,跳回来,继续
# 执行test没执行完的内容,再执行test2没执行完的内容
def test1():
    print("执行test1")
    gr2.switch()
    print("结束test1")
    gr2.switch()

def test2():
    print("执行test2")
    gr1.switch()
    print("结束test2")

# 将函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)

# 执行协程1
gr1.switch()