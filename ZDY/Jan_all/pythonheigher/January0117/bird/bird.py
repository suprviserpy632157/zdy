# 鸟类
class Bird:
    def __init__(self,name,age,skill):
        self.name=name
        self.age=age
        self.skill=skill
    def eat(self):
        print("%seating..."%self.name)

    def fly(self):
        print("%sflying..."%self.name)

    def reproduction(self):
        print("%sproducting..."%self.name)