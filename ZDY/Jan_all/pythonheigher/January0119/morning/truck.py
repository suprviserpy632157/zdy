# 卡车类，演示运算符的重载
class Truck:
    def __init__(self,load):
        self.load = load  #载重属性

    def __add__(self,valve):  #重载加运算符
        print("add被调用")
        return Truck(self.load+valve)

    def __mul__(self,rhs):   #重载乘运算符
        return Truck(self.load * rhs)
    
    def __radd__(self,value):  #反向＋运算符重载，支持３＋truck操作
        return Truck(self.load+value)

    def __rmul__(self,rhs):   #反向*运算符重载
        return Truck(self.load * rhs)

    def __iadd__(self,value):   #复合运算符重载
        print("iadd被调用")
        return Truck(self.load+value)

    def __str__(self):
        return "load:%d"%self.load 

    def __gt__(self,other):     #重载>运算符
        # return (self.load > other.load)
        print("__gt__()方法被调用")
        if self.load > other.load:
            return True
        else:
            return False
    
    # def __lt__(self,other):    #重载>运算符
    #     if self.load < other.load:
    #         return True
    #     else:
    #         return False

if __name__ == "__main__":
    t = Truck(20)
    t2 = Truck(30)
    print(t>t2)  #调用__gt__
    print(t<t2)  #调用__lt__
    # t2 = t+1             #t2接受返回的对象
    # print(t2)
    # print(t*2)
    # t2 = 1+t      #调用__radd__()方法
    # print(t2)
    # t3= 3*t
    # print(t3)
    # t+=1
    # print(t)   #调用__iadd__()方法