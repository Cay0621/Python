#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: org.com.cay.thread.SingleThread

@email: 412425870@qq.com
'''
import urllib.request
import time

urls = ['http://www.baidu.com', 'http://www.tencent.com','http://www.360.com','http://www.taobao.com','http://www.qiyi.com']
def get_responses():
    starttime = time.time()
    for url in urls:
        response = urllib.request.urlopen(url)
        print(url, response.getcode())
        
    #以下三句话等价
    #print('total time: {0}'.format(time.time() - starttime))
    #print('total time: %s', time.time() - starttime)
    print('total time: %s' % (time.time() - starttime))
          

if __name__ == '__main__':
    get_responses()
