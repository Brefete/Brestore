import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='newbase',
                     charset='utf8')
cur = db.cursor()
try:
    name = input('Name:')
    id = int(input('id:'))
    attack = int(input('attack:'))
    # sql = 'delete from sanguo where id=1;'


    # sql = 'insert into sanguo (name,attack,defence) values (susan,660,555);'
    cur.execute(sql)
    db.commit()

except Exception as e:
    db.rollback()
    print(e)

cur.close()
db.close()

