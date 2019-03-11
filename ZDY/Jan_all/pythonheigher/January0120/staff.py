# staff.py
# 主要演示__slots__属性实例
class Staff:
    "这是一个员工类"
    __slots__ = ["no","name","position"]
    def __init__(self,no,name,position):
        self.no = no              #编号
        self.name = name          #姓名
        self.position = position  #职位
    def __str__(self):
        ret = "no:%s,name:%s,position:%s"%(self.no,self.name,self.position)
        return ret  
    def work(self):     #员工的工作方法
        print("%s正在工作"%self.name)

# 定义机器人类，继承自Staff类
class ServiceRobot(Staff):
    def __init__(self,no,name,position):
        super().__init__(no,name,position)   
    def work(self):   #重写工作方法
        print("%s的工作,教练"%self.name)

if __name__ == "__main__":
    staff = Staff("0001","Jerry","manager")
    print(staff)
    robot = ServiceRobot("0002","阿童木","射击教练")
    print(robot)
    robot.work()
    #如果没有__slots__属性限制则成绩一个新属性执行不会报错，
    # 但没有起到给属性赋值的作用
    # staff.positino = "副总经理" 