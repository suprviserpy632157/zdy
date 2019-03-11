# 家用小汽车类，继承实例
from car import *
# 定义mini_car类，继承自Car类
class mini_car(Car):
    pass

if __name__=="__main__":
    mycar=mini_car("AUTO","black",1.40)
    mycar.startup() #启动
    mycar.run()     #行驶
    mycar.stop()    #停止
    mycar.info()    #打印信息