# db_oper.py
# 数据库访问类
import pymysql
from db_conf import*
class DBOper:
    # 构造方法
    def __init__(self):
        self.host = host
        self.user = user
        self.passward = passward
        self.dbname = dbname
        self.conn = None

    def open_conn(self):# 连接数据库
        try:
            self.conn = pymysql.connect(
                self.host,self.user,self.passward,self.dbname)
            print("数据连接成功")
        except Exception as e:
            self.conn.rollback()
            print("数据库操作失败")
            print(e)
    def close_conn(self):# 关闭数据连接
        self.conn.close()
        print("关闭数据连接成功")
    # 执行查询，返回结果集
    def do_query(self,sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()  
            return result
            cursor.close()
        except Exception as e:
            self.conn.rollback()
            print("数据库操作失败")
            print(e)
    # 执行增删改等变更操作
    def do_update(self,sql):
        try:
            if 'insert' in sql: 
                cursor = self.conn.cursor()
                cursor.execute(sql)
                self.conn.commit()
                cursor.close()
                print("插入成功")
            elif 'update' in sql:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                self.conn.commit()
                cursor.close()
                print("修改成功,影响笔数%d"%cursor.rowcount)
            elif 'delete' in sql:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                self.conn.commit()
                cursor.close()
                print("删除成功")
        except Exception as e:
            self.conn.rollback()
            print("数据库操作失败")
            print(e)
if __name__ == "__main__":
    oper = DBOper()
    oper.open_conn()
    oper.do_query("select * from acct")
    oper.do_update('''update acct set balance = balance - 100 
    where acct_no = '622345000003' ''')
    oper.do_update('''insert into acct values
    ('622345000010','kxx','C0010',1,curdate(),1,6666.88)''')
    oper.close_conn()