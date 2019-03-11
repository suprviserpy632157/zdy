# 老鹰类,继承自Bird
from bird import *
class Eagle(Bird):
    def eat(self):
        print("我是%s，我只吃肉"%self.name)
    def fly(self):
        print("我是%s,飞的又高又快")