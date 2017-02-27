#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: src.writefile

@email: 412425870@qq.com
'''
import os

class FileManager(object):

    def createFile(self, inifile):
        fd = os.open(inifile, os.O_TRUNC| os.O_CREAT | os.O_WRONLY)
        os.write(fd, b'[books]\n')
        os.write(fd, b'book1 = C++\n')
        os.write(fd, b'book2 = Java\n')
        os.write(fd, b'book3 = PHP\n')
        os.write(fd, b'book4 = IOS\n')
        os.write(fd, b'book5 = Android\n')
        os.close(fd)