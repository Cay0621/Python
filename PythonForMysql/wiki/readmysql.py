#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@file: wiki.readmysql

@email: 412425870@qq.com

@author: Cay

@pythonVersion: Python3.5

@function: 

@version: 
'''

import pymysql

connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     db='test',
                                     user='root',
                                     passwd='Cay20130621',
                                     charset='utf8')

try:
    cursor = connection.cursor()
    count = cursor.execute('select urlname, urlhref from wikiurl')
    print(count)
    
    result = cursor.fetchone()#获取一条数据记录
    result = cursor.fetchmany(size=3)#读取三条数据记录
    result = cursor.fetchall()#获取所有数据记录
    print(result)
finally:
    connection.close()
