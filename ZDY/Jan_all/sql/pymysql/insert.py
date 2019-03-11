# insert.py
# pymysql插入示例
import pymysql
from db_conf import*

try:
    # 链接数据库
    conn = pymysql.connect(host,user,passward,dbname)
    # 获取游标
    cursor = conn.cursor()
    # 执行SQL语句
    sql = '''insert into acct values
    ('622345000000','Robert','C0000',1,curdate(),1,7777.88)'''
    # 将sql作为参数传到游标中,执行插入
    cursor.execute(sql)
    # 提交事物
    conn.commit()
    # 关闭游标
    cursor.close()
    print("插入成功")
except Exception as e:
    # 出现异常回滚事物
    conn.rollback()
    print("数据库操作失败")
    print(e)
finally:
    # 关闭连接
    conn.close()