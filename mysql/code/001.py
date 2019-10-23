import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='newbase',
                     charset='utf8')
cur = db.cursor()

# 执行各种多数据库的读写操作
# name = input('Name:')
# sql = "select * from sanguo where name='%s';"%name
sql = 'select * from sanguo where country=%s and attack>%s;'
cur.execute(sql,['蜀国',260])

for i in cur:
    print(i)

# many_row = cur.fetchmany(2)
# print(many_row)

# all_row = cur.fetchall()
# print(all_row)



cur.close()
db.close()
