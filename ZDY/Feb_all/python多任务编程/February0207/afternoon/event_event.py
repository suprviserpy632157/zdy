from threading import Thread,Event
from time import sleep
# 设置全局变量,用于通信
s = None
e = Event()
# 写一个线程,给主线程发消息
def foo():
    sleep(0.1)
    print("Foo 前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() #改为天王盖地虎后解除阻塞
f = Thread(target=foo)
f.start()
# 主线程验证口令
print("说对口令就是自己人")
e.wait() #添加阻塞
if s == "天王盖地虎":
    print("确认过眼神,你是对的人")
else:
    print("打死你个龟孙!!!")
 
f.join()