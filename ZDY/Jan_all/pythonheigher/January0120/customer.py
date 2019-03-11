# customer.py
# 客户类
class Customer:
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id       #顾客编号
        self.cust_name = cust_name   #客户姓名
        self.tel_no = tel_no         #客户电话

    def __str__(self):
        ret = "顾客编号%s,客户姓名%s,客户电话%s"%\
        (self.cust_id, self.cust_name, self.tel_no)
        return ret
