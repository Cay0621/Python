#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: org.com.cay.thread.threadrace

@email: 412425870@qq.com
'''
from threading import Thread, Lock

number = 0
lock = Lock()

class NewThread(Thread):        
    def run(self):
        global number
        
        lock.acquire() #加锁
        #read_value = number;
#         print('before number: ',read_value)
        print('before:', number)
#         number = read_value + 1
        number += 1
        print('after number: ',number)
        lock.release() #解锁
        
def threadrace():
    threads = []
    for _ in range(5000):
        t = NewThread()
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
                
    print('total number: ', number)
    
if __name__ == '__main__':
    threadrace()    
        