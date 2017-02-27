#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: com.cay.account

@email: 412425870@qq.com
'''
import sys
import pymysql


class TransferMoney(object):
    
    def __init__(self, conn):
        self.conn = conn
        pass

    
    def check_acct_avaiable(self, source_acctid):
        cursor = self.conn.cursor()
        sql = "select * from Account where id = %d" % source_acctid
        try:
            print(sql)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('帐号%d出错' % source_acctid)
        finally:
            cursor.close()
    
    
    def has_enough_money(self, source_acctid, money):
        cursor = self.conn.cursor()
        sql = "select * from Account where id = %s and money > %d " % (source_acctid , money)
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('帐号%d金额不足' % source_acctid)
        finally:
            cursor.close()
    
    
    def reduce_money(self, source_acctid, money):
        cursor = self.conn.cursor()
        sql = "update Account set money = money - %d where id = %s" % (money, source_acctid)
        try:
            print(sql)
            cursor.execute(sql)
            
            if cursor.rowcount != 1:
                raise Exception('帐号%d减款失败' % source_acctid)
        finally:
            cursor.close()
    
    
    def add_money(self, target_acctid, money):
        cursor = self.conn.cursor()
        sql = "update Account set money = money + %d where id = %s" % (money, target_acctid)
        try:
            print(sql)
            cursor.execute(sql)
            
            if cursor.rowcount != 1:
                raise Exception('帐号%d加款失败' % target_acctid)
        finally:
            cursor.close()
    
    
    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_avaiable(source_acctid)
            self.check_acct_avaiable(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        pass
    
    
if __name__ == '__main__':
    source_acctid = int(sys.argv[1])
    target_acctid = int(sys.argv[2])
    money = int(sys.argv[3])
    
    conn = pymysql.connect(
                           host = '127.0.0.1',
                           user = 'root',
                           passwd = 'Cay20130621',
                           port = 3306,
                           db = 'test',
                           charset = 'utf8')
    
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print("转账出错", e)
    finally:
        conn.close()
    