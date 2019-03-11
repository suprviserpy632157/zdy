# acct_manage.py
# 账户管理类（业务逻辑层）
# 实现账户新增、修改、查询、删除等逻辑处理
from db_oper_change import *
class Acct:  #账户类，仅用于数据传输
    def __init__(self,acct_no,acct_name,acct_type,balance):
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.acct_type = acct_type
        self.balance = balance
    def __str__(self):
        ret = "账号：%s,户名：%s,类型%d,余额：%.2f"%\
        (self.acct_no,self.acct_name,self.acct_type,self.balance)
        return ret 

class AcctManage: #账户管理类
    def  __init__(self,db_oper):
        self.db_oper = db_oper #数据访问对象

    #查询所有账户信息
    def query_all_acct(self):
        accts = []  #返回的Acct对象列表，可能有多个对象
        # 拼装做需要的SQL
        sql = "select * from acct"
        # 执行查询
        result = self.db_oper.do_query(sql)
        if not result:
            print("查询结果为空")
            return None
        # 返回结果:实例化一个acct的对象列表返回(因为元组处理起来不方便，成为对象时候才方便)
        for acct_info in result:
            acct_no = acct_info[0]          #账号
            acct_name = acct_info[1]        #户名
            acct_type = int(acct_info[3])   #类型
            balance = acct_info[6]          #余额
            accts.append(Acct(acct_no,acct_name,acct_type,balance))
        return accts                #返回对象列表
    
    # 根据账户查询，最多返回一个对象
    def query_by_id(self,acct_no):
        if not acct_no:
            print("账号对象非法")
            return None
        if acct_no == "":
            print("账号不能为空")
            return None
        sql = '''select * from acct 
        where acct_no = "%s" '''%acct_no
        result = self.db_oper_change.do_query(sql) #执行查询
        if not result:
            print("查询返回空对象")
            return None
        # 提取查询结果，实例化一个Acct对象返回
        acct_info = result[0]          #获取第一行数据
        acct_no = acct_info[0]         #账号
        acct_name = acct_info[1]       #户名
        acct_type = int(acct_info[3])  #类型
        balance = acct_info[6]         #余额
        return Acct(acct_no,acct_name,acct_type,balance)
    
    def query_by_name(self,acct_name):
        if not acct_name:
            print("姓名不存在")
            return None
        if acct_name == "":
            print("姓名不能为空")
            return None
        accts=[]
        sql = '''select * from acct where acct_name = "%s" '''%acct_name
        result = self.db_oper_change.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None
        for acct_info in result:
            acct_no = acct_info[0]
            acct_name = acct_info[1]
            acct_type = int(acct_info[3])
            balance = acct_info[6]
            accts.append(Acct(acct_no, acct_name, acct_type, balance))

        return accts

  
    def insert_acct(self, acct):  #插入对象
        sql = '''insert into acct(acct_no, acct_name, acct_type, balance) \
                 values('%s','%s',%d,%.2f)
        ''' % (acct.acct_no, acct.acct_name, acct.acct_type, acct.balance)
        print("\nsql:%s\n" % sql)
        result = self.db_oper_change.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return 

    def update_acct(self, acct):
        sql = '''update acct \
                 set acct_type = %d,
                     balance = %.2f
                where acct_no = '%s'
        ''' % (acct.acct_type, acct.balance, acct.acct_no)
        print("\nsql:%s\n" % sql)
        result = self.db_oper_change.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return

    def delete_acct(self,acct):
        sql = '''delete from acct where acct_no = '%s' '''%acct.acct_no
        print("\nsql:%s\n"%sql)
        result = self.db_oper_change.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return
    
