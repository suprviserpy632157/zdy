# Car类： 车辆类(简单类)
# 属性：car_id（车辆id号）name（车辆名称）is_lend（是否租借）
#      price（每天单价） start_date(起租日期) end_date(终止日期)
# 方法：__str__()
class Car:
    def __init__(self,car_id,name,is_lend,price):
        self.car_id = car_id    #车辆编号
        self.name = name        #车辆名称
        self.is_lend = is_lend  #是否租借
        self.price = price      #每天单价
        self.start_date = ""    #起租日期
        self.end_date = ""      #终止日期
        self.cust_id = ""       #租车客户编号  

    def __str__(self):
        ret = "车辆id:%s,车辆名称:%s,是否租借:%s,每天单价:%.2f"%\
        (self.car_id,self.name,self.is_lend,self.price)
        return ret
# Customer类：（简单类）
# 属性：cust_id（顾客编号），cust_name（客户姓名），tel_no（客户电话）
# 方法：__str__()
#  
class Customer:
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id       #顾客编号
        self.cust_name = cust_name   #客户姓名
        self.tel_no = tel_no         #客户电话

    def __str__(self):
        ret = "顾客编号%s,客户姓名%s,客户电话%s"%\
        (self.cust_id, self.cust_name, self.tel_no)
        return ret

# CarStore类(汽车租赁模拟程序)
# 属性：cars（所有车辆列表），customers（所有客户列表）
# 方法：__load_cars()      加载所有车辆信息
#      __load_customers() 加载所有客户信息
#      print_cars_info()  打印所有车辆信息
#      add_car()          添加车辆
#      del_car()          删除汽车
#      lend()             租车
#      back()             还车
class CarStore(Car,Customer):
    def __init__(self):
        self.cars = []            #车辆列表
        self.custs = []           #客户列表
        self.__load_cars()        #加载车辆列表
        self.__load_customers()   #加载客户列表
    
    # # 加载车辆
    def __load_cars(self):
        with open("cars_list.txt") as f:
            line = f.readline(256).replace("\n","")
            custinfo = line.split(",")
            car_id = custinfo[0]
            car_name = custinfo[1]
            is_len = custinfo[2]
            price = float(custinfo[3])
            car = Car(car_id,car_name,is_len,price)
            self.cars.append(car)  #对象添加到列表
    #     self.cars.append(Car("1","GOLF","否",400))
    #     self.cars.append(Car("2","凯越","否",350))
    #     self.cars.append(Car("3","奥迪","否",1200))
    #     self.cars.append(Car("4","凯美瑞","否",800))
    #     self.cars.append(Car("5","宝来","否",450))
   
    # 加载客户列表
    def __load_customers(self):
        cust1 = Customer("c0001","康小狗","13999978944")
        cust2 = Customer("c0002","曲老秀","13999978945")
        cust3 = Customer("c0003","卞狗子","13999978946")
        self.custs.append(cust1)
        self.custs.append(cust2)
        self.custs.append(cust3)
    
    # 打印所有车辆信息
    def print_cars_info(self):
        for car in self.cars:   #遍历车辆列表并打印
            print(car)
    
    # 查找车辆
    def find_car(self,car_id):  #根据车辆编号查询
        for car in self.cars:
            if car.car_id == car_id:  #编号相等
                print(car)
                return 
        print("未找到车辆信息")
        return
   
    # 添加车辆
    def add_car(self,car):
        if isinstance(car,Car):  #car是Car的实例
            self.cars.append(car)
        else:
            print("对象类型有误")
        #可以添加id号是否存在的逻辑判断
        return
   
    # 删除汽车
    def del_car(self,car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)    #删除对象
        return
   
    # 租车
    def lend(self,car_id,cust_id,start_date,end_date):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_lend == "是":    #已出租
                    print("该车辆已经出租")
                    return
                else:      #未出租
                    setattr(car,"is_lend","是")  #改状态
                    setattr(car,"cust_id",cust_id)
                    setattr(car,"start_date",start_date)
                    setattr(car,"end_date",end_date)
                    print("车辆出租登记完成")
                    return
        print("未找到车辆信息")
        return
    
    # 还车
    def back(self,car_id):
        for car in self.cars:
            if car.car_id == car_id:
                setattr(car,"is_lend","否")  #改状态
                setattr(car,"cust_id","")
                setattr(car,"start_date","")
                setattr(car,"end_date","")
                print("还车登记完成")
                return
        print("未找到车辆信息")
        return

if __name__ == "__main__":
    car_store = CarStore()       #实例化租车店对象
    car_store.find_car("3")      #查找编号为3的编号
    car = Car("6","捷达","否",300)
    car_store.add_car(car)       #将car这个对象添加到cars列表
    car_store.print_cars_info()
    car_store.del_car("6")       #将编号为６的汽车删除
    car_store.lend("3","c0001","2018-1-1","2018-1-3")
    car_store.print_cars_info()
    car_store.back("3")
    car_store.print_cars_info()

