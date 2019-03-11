# 账户类s
# 属性：账号（acct_no）户名（acct_name）开户日期（reg_date）类型（acct_type）（借记卡、贷记卡）
#      状态（acct_atatus）（正常、挂失、冻结、注销） 余额（balance）
# 方法：存款（diposite）取款（draw）冻结（freeze）解冻（unfreeze）
#      挂失（report_loss）解挂失（relieve_lose）修改账户信息（modify_acct_info）
dict_status={0:"正常",1:"冻结",2:"挂失",3:"注销"} #状态字典
dict_type={0:"借记卡",1:"贷记卡"}                #类型字典
class Account:
    def __init__(self,acct_no,acct_name,reg_date,acct_type,acct_status,balance):
        self.acct_no = acct_no                 #账号
        self.acct_name = acct_name             #户名
        self.reg_date = reg_date               #开户日期
        self.acct_type = acct_type             #类型
        self.acct_status = acct_status         #状态
        self.balance = balance                 #余额
    # 存款
    def diposite(self,amt):
        print("存款前的余额：%.2f"%self.balance)
        self.balance += amt                    #修改余额
        print("存款后的余额：%.2f"%self.balance)
        # if self.acct_status == '正常':
        #     savemoney=int(input("Please input money:"))
        #     self.balance += savemoney
        # return self.balance
    # 取款
    def draw(self,amt):
        if self.acct_status == 0:              #正常状态
            if self.balance <amt:              #余额不足
                print("余额不足")
                return
            else:                              #余额充足
                print("存款前的余额：%.2f"%self.balance)
                self.balance -= amt            #修改余额
                print("存款后的余额：%.2f"%self.balance)
        else:                                  #非正常状态
            print("状态不允许取款")
        # if self.acct_status == "正常" and self.balance>=100:
        #     money=int(input("Please take out money:"))
        #     if money <= self.balance:
        #         self.balance -= money 
        # print("%s取出%.2f元,剩余%.2f元"%(self.acct_name,money,self.balance))
    # 冻结
    def freeze(self):
        if self.acct_status != 0:
            print("状态不允许冻结")
            return
        self.acct_status = 1                    #状态重置为冻结
        print("账户已冻结")
        # if self.balance < 0:
        #     if self.acct_status == "注销" or self.acct_status == "挂失":
        #         print("无法冻结")
        #     self.acct_status = "冻结"
    # 解冻
    def unfreeze(self):
        if self.acct_status != 1:               #判断已冻结
            print("状态不允许解冻")
            return
        self.acct_status = 0                    #状态置为正常
        print("账户已解冻")
        # if self.balance < 0 and self.acct_status=="冻结":
        #     returnmoney = int(input("Please input return money:"))
        #     self.balance += returnmoney
        #     if self.balance >=0 and self.acct_status=="冻结":
        #         self.acct_status=="正常"
        # else:
        #     print("解冻失败")
    # 挂失
    def report_loss(self):
        if self.acct_status != 0:
            print("状态不允许挂失")
            return
        self.acct_status = 2                     #状态重置为挂失
        print("账户已挂失")
    # 解挂
    def relieve_lose(self):
        if self.acct_status != 2:                #判断已挂失
            print("状态不允许解挂")
        self.acct_status = 0                     #状态置为正常
        print("账户已解挂")
    # 修改账户信息
    def modify_acct_info(self,new_no,new_name):
        self.acct_no = new_no
        self.acct_name = new_name
        return "修改后的账号%s,户名%s"%(self.acct_no,self.acct_name)

    def __str__(self):                          #重写__str__()
        # 将状态转换为对应的字符串
        status = dict_status[self.acct_status]
        # 将类型转换为对应的字符串
        type = dict_type[self.acct_type]
        ret = "账号:%s,户名:%s,开户日期:%s,类型%s,状态:%s,余额:%.2f"%\
        (self.acct_no,self.acct_name,self.reg_date,type,status,self.balance)
        return ret

if __name__=="__main__":
    ac=Account("622345001","张狗蛋","2019-1-6",0,0,2000)
    ac.diposite(1000.00)                        #存款
    ac.draw(500)                                #取款
    print(ac)                                   #打印账户信息
    ac.freeze()                                 #冻结
    print(ac)                                   #打印账户信息
    ac.unfreeze()                               #解冻
    print(ac)                                   #打印账户信息
    ac.report_loss()                            #挂失
    print(ac)                                   #打印账户信息
    ac.relieve_lose()                           #解挂 
    print(ac)                                   #打印账户信息
    a = ac.modify_acct_info("002","李二狗")
    print(a)


