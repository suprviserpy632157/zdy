# 鸵鸟类,继承自Bird
from bird import *
class Ostrich(Bird):
    def fly(self):  #重写fly方法
        print("我是%s,太重了不能飞"%self.name)
    def eat(self):
        print("我是%s,我是杂食动物")
