import gevent
# import time
# 先执行roo,跳转到bar,再跳入foo继续执行,再跳入bar执行完毕
def foo():
    print("Running foo")
    gevent.sleep(3)
    print("Foo again")

def bar():
    print("Running bar")
    gevent.sleep(2)
    print("Bar again")

# 这只是有了执行的条件,但还没有执行的契机
f = gevent.spawn(foo)
b = gevent.spawn(bar)

# 契机(并不是所有阻塞都能触发他的执行)
# time.sleep(5)
gevent.joinall([f,b])