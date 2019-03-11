from threading import Thread
from time import sleep,ctime
# 创建进程Thread类
class MyThread(Thread):
    # 重写__init__方法添加自己的属性，使用super加载父类属性
    def __init__(self,target=None,args=(),kwargs={},name='kxx'):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    # 重写run方法
    def run(self):
        self.target(*self.args,**self.kwargs)

def player(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),kwargs={'song':'凉凉'},name="happy")
t.start()
t.join()