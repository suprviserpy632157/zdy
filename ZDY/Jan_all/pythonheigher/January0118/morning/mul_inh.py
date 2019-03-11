# 多重继承实例
# 超人类继承自战士，飞行者，喷火者
# 三个类
class Fighter:
    def fight(self):
        print("我能打")
    def roar(self):
        print("战士吼叫：打死你个龟孙！！！")

class Flyer:
    def fly(self):
        print("我能上天")
    def roar(self):
        print("飞行者吼叫：好尴尬呀！")

class Firer:
    def fire(self):
        print("我能吐火")
# 超人类继承自战士，飞行者，喷火者三个类
class SuperMan(Fighter,Flyer,Firer):
    pass

if __name__=="__main__":
    sp=SuperMan()
    sp.fight()
    sp.fly()
    sp.fire()
    sp.roar()
    # print(SuperMan.__mro__)
    print(SuperMan.__bases__)
    print(Fighter.__base__)
    print(Flyer.__base__)