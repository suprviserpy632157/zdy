from multiprocessing import Process
import time
# 自定义进程类
class  ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        # 调用父类__init__方法
        super().__init__()
    # 重写run方法,打印3次当前时间
    def run(self):
        for i in range(3):
            print("The time is %s"%time.ctime())
            time.sleep(self.value)
# 创建进程对象
p = ClockProcess(2)
# 启动新的进程
p.start()
p.join()