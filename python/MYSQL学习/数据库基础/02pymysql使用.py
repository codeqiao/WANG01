
"""
   

   
    
    
"""

from tkinter import scrolledtext
import pymysql

# 1、建立数据库连接
db = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='stu',
                    charset='utf8')
# 2、创建游标对象
cur = db.cursor()
# 3、游标方法
# sql = "insert into class values (7,'emma',17,'w',76.5);"
# cur.execute(sql)
# 4、提交到数据库、
# db.commit() # 将写操作提交

# ×××××××××××××××××××××××　数据库读  ××××××××××××××××××××××××××××
# 获取数据库数据
sql = "select*from class where sex='w';"
cur.execute(sql)

# print(cur.fetchone())
#print(cur.fetchmany(2))
print(cur.fetchall())

# ×××××××××××××××××××××××　数据库写  ××××××××××××××××××××××××××××

try:
    #写sql语句执行
    #插入操作
    name = input("name: ")
    age = input("age: ")
    score = input("score: ")
    sql = "insert into class (name,age,score) values (%s,%s,%s)"
    cur.execute(sql,[name,age,score]) # 该方法只能给values传
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

# 5、关闭游标对象
cur.close()
# 6、断开数据库连接
db.close()