import pymysql
import re
f = open("dict.txt")
# 连接数据库
db = pymysql.connect("127.0.0.1","root","123456","dict")
cursor = db.cursor()
# 循环接收
for line in f:
    L = re.split(r"\s\s\s+",line)
    word = L[0]
    interpret = ''.join(L[1:])
    sql = "insert into words(word,interpret) values('%s','%s')"%(word,interpret)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
f.close()