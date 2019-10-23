import pymysql
import re

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
f = open('dict.txt')
args_list = []
for line in f:
    tup = re.findall(r'(\S+)\s+(.*)', line)[0]
    args_list.append(tup)
f.close()
sql = 'insert into word (word,name) values (%s,%s);'
try:
    cur.executemany(sql, args_list)
    db.commit()

except:
    db.rollback()

cur.close()
db.close()
