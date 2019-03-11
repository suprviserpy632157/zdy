import pymysql

f = open("dict.txt")
db = pymysql.connect("localhost","root","123456","dict")

cursor = db.cursor()

for line in f:
    tmp = line.split(" ")
    word = tmp[0]
    interpret = ' '.join(tmp[1:]).strip()
    sql = 'insert into words(word,interpret) values("%s","%s")'%(word,interpret)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
f.close()