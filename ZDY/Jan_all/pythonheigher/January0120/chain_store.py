# 连锁店类，类属性/类方法实例
from staff import *
from customer import *
class ChainStore:
    # 类属性
    store_num = 0                          #连锁店门店数量
    total_income = 0                       #所有门店总营业额度
    store_list = []                        #所有门店对象列表
    cust_list = [ ]                        #所有会员列表
    def __init__(self,store_no,store_name,address,manager):
        print("门店开张")
        self.store_no = store_no           #编号
        self.store_name = store_name       #店名
        self.address = address             #地址
        self.manager = manager             #经理
        self.myincome = 0                  #本店营业额度
        ChainStore.store_num += 1          #门店开张，总门店数量加1
        ChainStore.store_list.append(self) #添加当前对象到所有门店列表中       
        self.staff_list = []               #连锁店包含一组员工，组合关系

    def do_business(self,income):
        print("正在营业")
        self.myincome += income            #营业额累加
        ChainStore.total_income += income  #将本店的营业额度累加到总的营业额度上去
    def __str__(self):
        ret = "编号%s,名称%s,地址%s,店长%s,总营业额%.2f"%\
        (self.store_no,self.store_name,self.address,\
        self.manager,self.myincome)
        return ret

    def add_staff(self,staff):
        self.staff_list.append(staff)

    def del_staff(self,no):
        for staff in self.staff_list:
            if staff.no == no:
                self.staff_list.remove(staff) #删除对象
        return
    
    def print_all_staff(self):
        for staff in self.staff_list:
            print(staff)
    # 关闭一家店
    def __del__(self): #析构函数
        print("%s门店关闭"%self.store_name)
        ChainStore.store_num -= 1  #减少一家门店

    @classmethod
    def print_total(cls):
        print("门店数量：%d,营业额度：%.2f"%(cls.store_num,cls.total_income))
        for store in cls.store_list:        #遍历门店列表
            print(str(store))
    @staticmethod
    def print_regulation():    #静态方法，打印管理条例
        regulation = '''
        -------连锁店管理条例-------
        第一条：考勤
        第二条：不迟到，不早退，不旷工
        第三条：有事向经理请假
        ．．．
        '''
        print(regulation)

    def cust_reg(self,cust):   #会员注册
        ChainStore.cust_list.append(cust)

    def print_cust_info(self):  #打印会员
        for cust in ChainStore.cust_list:
            print(cust)

if __name__ == "__main__":
    # # 第一家分店
    store1 = ChainStore("1","西单旗舰店","西单","王小小")
    # store1.cust_reg(Customer("1","悟空","13636365959"))
    # store1.cust_reg(Customer("2","无能","13654548787"))
    # store1.print_cust_info()
    # store1.add_staff(Staff("0001","Jerry","manager"))
    # store1.add_staff(Staff("0002","Tom","staff"))
    # store1.add_staff(ServiceRobot("0003","Jim","cooker"))
    # store1.print_all_staff()   #打印所有员工信息
    # store1.do_business(20000)   #营业
    # ChainStore.print_total()    #调用类方法
    # print("门店数量：",ChainStore.store_num)
    # print("总营业额度：",ChainStore.total_income)
    # print("--------------------------------------")
    # 第二家分店
    store2 = ChainStore("2","中关村店","中关村","康小小")
    store1.do_business(25000)   #营业
    del store2   #销毁store2对象
    # print("门店数量：",ChainStore.store_num)
    # print("总营业额度：",ChainStore.total_income)
    # ChainStore.print_total()    #调用类方法
    # ChainStore.print_regulation() #通过类调用静态方法
    # store2.print_regulation()     #通过对象调用静态方法


