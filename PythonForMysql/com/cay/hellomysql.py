#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: com.cay.hellomysql

@email: 412425870@qq.com
'''

import pymysql

conn = pymysql.connect(
                       host = '127.0.0.1', 
                       port = 3306, 
                       user = 'root', 
                       passwd = 'Cay20130621',
                       db = 'test',
                       charset = 'utf8'
                       )

cursor = conn.cursor()

# sql: select
sql = 'select * from tmp_user'
cursor.execute(sql)
print(cursor.rowcount) #查看数据库中记录条数

rs = cursor.fetchone() #抓取一条数据
print(rs)

rs = cursor.fetchmany(3)#抓取三条数据
print(rs)

rs = cursor.fetchall()#抓取所有的数据
print(rs)

print('===============================')
cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print("id=%d, name=%s"% row)

# sql: insert
sql_insert = 'insert into tmp_user(name) values("张三")'
sql_update = 'update tmp_user set name="李四" where id=4'
sql_delete = 'delete from tmp_user where id=4'  

try:
    cursor.execute(sql_update)
    print(cursor.rowcount) # 此时查看影响数据库中的条数
    conn.commit()
    
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()