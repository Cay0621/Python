#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Cay

@file: src.ini_manager

@email: 412425870@qq.com
'''
from src import filemanager
from configparser import ConfigParser


class ini_info(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.cfg = ConfigParser()
    
    def load(self):
        self.cfg.read(self.filename)
        
    def getall(self):
        se_list = self.cfg.sections()
        for section in se_list:
            print(section)
            print(self.cfg.items(section))

    def getbysections(self, section):
        return self.cfg.items(section)
    
    def getbyoptions(self, section, option):
        self.cfg.get(section, option)
    
    def add_section(self, section):
        self.cfg.add_section(section)
    
    def set_item(self, section, option, value):
        self.cfg.set(section, option, value)
    
    def delete_section(self, section):
        self.cfg.remove_section(section)

    def delete_option(self, section, option):
        self.cfg.remove_option(section, option)
        
    def has_section(self, section):
        return self.cfg.has_section(section)
    
    def has_option(self, section, option):
        return self.cfg.has_option(section, option)
    
    def save(self):
        fp = open(self.filename, 'w')
        self.cfg.write(fp)
        fp.close()
        pass

if __name__ == '__main__':
    filename = 'tmp.ini'
    fileManager = filemanager.FileManager()
    fileManager.createFile(filename) # write ini
    
    info = ini_info(filename)
    info.load() #load
    info.getall()
    
    books = info.getbysections('books')
    for book in books:
        print(book)
    
    if info.has_section('price') is False:
        info.add_section('price')
        info.set_item('price', 'C++', '79')
        info.set_item('price', 'Java', '50')
        info.set_item('price', 'PHP', '20')
    
    print(info.has_section('books'))
    print(info.has_option('books', 'book3'))
    info.delete_option('books', 'book4')
    #info.delete_section('price')
    info.save()
    