import random
class Car():
    # 构造方法，主要作用是对属性进行初始化
    def __init__(self,name,color,output_volumn):
        self.name = name
        self.color = color
        self.output_volumn =output_volumn
        self.__distance=0.00 #私有属性行驶里程
        self.__oil=8.00 #每百公里耗油量
    
    def __calc_distance(self): #计算行驶里程的方法
        dist=random.randint(1,400)
        self.__distance += dist

    def get_distance(self): #获得行驶里程
        return self.__distance #返回行驶里程这个属性

    def startup(self):
        print("汽车启动")

    def run(self):
        # 调用行驶里程方法
        self.__calc_distance()
        real_oil=self.__oil/100*self.get_distance()
        print("汽车行驶了%.2f公里，油耗%.2f升"%(self.__distance,real_oil))

    def stop(self):
        print("汽车停止")   

    def info(self): #打印汽车信息
        print("名称%s,颜色%s,排量%.1f"%(self.name,self.color,self.output_volumn))
        
if __name__=="__main__":
    # 实例化：根据类创建对象（根据模型制作具体产品）
    car = Car("Auto","blue",2.0)
    car.startup()
    car.run()
    car.stop()
    car.info()
    # car.__distance=0.00 #在类外部进行修改
    # 通过调用get_distance()方法获取行驶里程
    print("行驶里程：%.2f"%car.get_distance())