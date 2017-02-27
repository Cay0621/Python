#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql

resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup = BeautifulSoup(resp, 'html.parser')

listUrls = soup.find_all('a', href=re.compile(r'^/wiki/'))

for url in listUrls:
    if not re.search(r'\.(jpg|JPG)$', url['href']):
        '''
            #为了测试str的join函数，别无其他
            url['href'] = url['href'][1:]
            print(url.get_text(), ' <----> ', '/'.join(['https://en.wikipedia.org', url['href']]))
        '''
        connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     db='test',
                                     user='root',
                                     passwd='Cay20130621',
                                     charset='utf8')

        try:
            cursor = connection.cursor()
            sql = 'insert into wikiurl(urlname,urlhref) values(%s,%s)'
            cursor.execute(sql, (url.get_text(), "/" + url['href']))

            connection.commit()
        finally:
            connection.close()
