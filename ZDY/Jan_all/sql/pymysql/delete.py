# delete.py
# pymysql删除示例
import pymysql
from db_conf import*

try:
    # 链接数据库
    conn = pymysql.connect(host,user,passward,dbname)
    # 获取游标
    cursor = conn.cursor()
    # 执行SQL语句
    sql = '''delete from acct where acct_no = "622345000000" '''
    # 将sql作为参数传到游标中,执行插入
    cursor.execute(sql)
    # 提交事物
    conn.commit()
    # 关闭游标
    cursor.close()
    print("删除成功,影响笔数%d"%cursor.rowcount)
except Exception as e:
    # 出现异常回滚事物
    conn.rollback()
    print("数据库操作失败")
    print(e)
finally:
    # 关闭连接
    conn.close()