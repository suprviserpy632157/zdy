# acct_manage_ui.py
# 用户接口层
# 测试
from db_oper_change import *
from acct_manage import *
if __name__ == "__main__":
    db_oper = DBOper()  #实例化数据访问对象
    db_oper.open_conn() #打开连接
    am = AcctManage(db_oper) #实例化账户管理对象
    
    # 根据用户输入，进行不同操作
    def print_menu(): #打印主菜单
    menu = '''
    --------------- 账户管理程序 ---------------
      1 - 查询所有账户      2 - 根据账号查询
      3 - 根据户名查询      4 - 新增账户
      5 - 修改账户         6 - 删除账户
      其它 - 退出
    '''
    print(menu)  
    oper = input("请选取要执行的操作：")
    while True:
        if oper == "1" : #查询所有账户，并返回对象列表
            accts = am.query_all_acct() 
            for acct in accts:  #打印结果
                print(acct)
        elif oper == "2" : #根据账户查询，返回一个acct对象
            acct_no = input("请输入要查询的账号:")
            acct = am.query_by_id(acct_no) #查询
            print(acct)  #打印得到的对象
        elif oper == "3":  #根据户名查询
            query_by_name()
        elif oper == "4":  #新增账户
            add_acct()
        elif oper == "5":  #修改账户
            pass
        elif oper == "6":  #删除账户
            pass
        else:
            break
    db_oper_change.close_conn()

# # acct_manage_ui.py
# # 账户管理程序ui层
# from db_oper import *
# from acct import *
# from acct_manage import *

# # 全局变量
# db_oper = None
# am = None

# def print_menu(): #打印主菜单
#     menu = '''
#     --------------- 账户管理程序 ---------------
#       1 - 查询所有账户      2 - 根据账号查询
#       3 - 根据户名查询      4 - 新增账户
#       5 - 修改账户         6 - 删除账户
#       其它 - 退出
#     '''
#     print(menu)  

# def query_all():   #查询所有账户
#     accts = am.query_all_acct()
#     for a in accts:
#         print(a)

# def query_by_id(): #根据账号查询
#     acct_no = input("请输入要查询的账号：")
#     if not acct_no:
#         print("输入账号不合法")
#         return
    
#     acct = am.query_by_id(acct_no)
#     print("\n查询结果:")
#     print(acct)   #打印账户信息
#     print("\n")

# def query_by_name(): #根据户名查询
#     acct_name = input("请输入要查询的户名：")
#     if not acct_name:
#         print("输入账号不合法")
#         return
    
#     accts = am.query_by_name(acct_name)
#     print("\n查询结果:")
#     for acct in accts:
#         print(acct)   #打印账户信息
#     print("\n")

# def add_acct(): #新增账户
#     try:
#         acct_no = input("请输入账号:")
#         acct_name = input("请输入户名:")
#         acct_type = int(input("请输入账户类型(1-借记卡 2-理财卡  3-代缴代扣卡)："))
#         balance = float(input("请输入开户金额:"))
#         assert acct_type in [1, 2, 3]
#         assert balance >= 0.000001

#         new_acct = Acct(acct_no, acct_name, acct_type, balance)
#         am.insert_acct(new_acct)
#     except Exception as e:
#         print("操作错误")
#         print(e)
#     return    

# def main(): #主函数
#     global db_oper
#     global am
#     db_oper = DBOper()    #实例化数据访问对象
#     db_oper.open_conn()   #打开数据库连接
#     am = AcctManage(db_oper)  #实例化AcctManage对象

#     while True:
#         print_menu()
#         oper = input("请选则要执行的操作:")
#         if oper == "1":  #查询所有账户
#             query_all()
#         elif oper == "2":  #根据账号查询
#             query_by_id()
#         elif oper == "3":  #根据户名查询
#             query_by_name()
#         elif oper == "4":  #新增账户
#             add_acct()
#         elif oper == "5":  #修改账户
#             pass
#         elif oper == "6":  #删除账户
#             pass
#         else:
#             break
#     db_oper.close_conn()

# if __name__ == "__main__":
#     main()
