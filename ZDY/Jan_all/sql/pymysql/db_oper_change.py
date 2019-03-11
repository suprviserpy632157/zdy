# db_oper.py
# 数据库访问类
import pymysql
import db_conf
class DBOper:
    # 构造方法
    def __init__(self):
        self.host = db_conf.host
        self.user = db_conf.user
        self.passward = db_conf.passward
        self.dbname = db_conf.dbname
        self.db_conn = None       #数据库连接对象

    def open_conn(self):# 连接数据库
        try:
            self.db_conn = pymysql.connect(
                self.host,self.user,self.passward,self.dbname)
        except Exception as e:
            print("数据库连接错误")
            print(e)
        else:
            print("数据连接成功")

    def close_conn(self):# 关闭数据连接
        try:
            self.db_conn.close()
        except Exception as e:
            print("数据库关闭错误")
            print(e)
        else:
            print("数据关闭成功")

    # 执行查询，返回结果集
    def do_query(self,sql):
        if not sql:  #参数语句合法性判断
            print("sql语句不合法")
            return None

        if sql=="":  #参数语句合法性判断
            print("sql语句不合法")
            return None

        try:
            cursor = self.db_conn.cursor()  #获取游标
            cursor.execute(sql)          #执行SQL语句
            result = cursor.fetchall()   #获取数据
            cursor.close()               #关闭游标
            return result                #返回查询结果
        except Exception as e:
            print("查询出错")
            print(e)
            return None

    # 执行增删改等变更操作
    def do_update(self,sql):
        if not sql:  #参数语句合法性判断
            print("sql语句不合法")
            return None

        if sql=="":  #参数语句合法性判断
            print("sql语句不合法")
            return None

        try:
                cursor = self.db_conn.cursor() #获取游标
                result = cursor.execute(sql) #执行SQL语句
                self.db_conn.commit() #提交事物
                cursor.close()
                return result   #返回受影响的笔数
        except Exception as e:
            print("执行SQL语句出错")
            print(e)
            return None
if __name__ == "__main__":
    oper = DBOper()   #实例化数据库操作对象
    oper.open_conn()  #连接数据库
    #查询测试
    oper.do_query("select * from acct") 
    # 修改测试 
    sql = '''insert into acct values
    ('622345000000','Peter','C0000',1,curdate(),1,8888.88) '''
    ret = oper.do_update(sql)
    if not ret:  #返回空对象
        print("执行修改错误")
    else:        #非空对象，执行成功
        print("影响笔数：%d"%ret)
    oper.close_conn()  #关闭数据库连接