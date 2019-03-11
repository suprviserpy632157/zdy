# query.py
# pymysql查询示例
import pymysql
from db_conf import*
# 建立数据库连接
conn = pymysql.connect(host,user,passward,dbname)
# 获取游标对象
cursor = conn.cursor()
# 使用游标对象提供的方法，执行SQL语句
cursor.execute("select * from acct")
result = cursor.fetchall()   #提取查询到的数据
for r in result:             #遍历结果集，取字段打印
    tmp = "账号：%s,户名：%s,金额：%s"%(r[0],r[1],r[6])
    print(tmp)
# 关闭游标
cursor.close()
# 关闭数据库连接
conn.close()
