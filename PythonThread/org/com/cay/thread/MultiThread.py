#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: org.com.cay.thread.MultiThread

@email: 412425870@qq.com
'''
from threading import Thread
import urllib.request
import time

class CreateThread(Thread):
    def __init__(self, url):
        self._url = url
        super(CreateThread,self).__init__()
    
    def run(self):
        response = urllib.request.urlopen(self._url)
        print(self._url, response.getcode())
    
def get_responses():
    urls = ['http://www.baidu.com', 'http://www.tencent.com','http://www.360.com','http://www.taobao.com','http://www.qiyi.com']
    starttime = time.time()
    threads = []
    for url in urls:
        t = CreateThread(url)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print('total time: {0}'.format(time.time() - starttime))

if __name__ == '__main__':
    get_responses()