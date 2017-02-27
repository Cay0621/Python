#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@file: pdf.readpdf

@email: 412425870@qq.com

@author: Cay

@pythonVersion: Python3.5

@function: 

@version: 
'''
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

#打开pdf文档
fp = open('naacl06-shinyama.pdf', 'rb')
#创建与文档关联的解释器
parser = PDFParser(fp)
#pdf文档的对象
doc = PDFDocument()
#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize('')

#创建pdf资源管理器
rsrcmgr = PDFResourceManager()
#参数分析器
laparams = LAParams()
#创建聚合器
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#页面解释器
interpreter = PDFPageInterpreter(rsrcmgr, device)

#使用文档对象得到页面的集合
for page in doc.get_pages():
    #使用页面解释器来读取
    interpreter.process_page(page)
    #使用聚合器获取内容
    layout = device.get_result()
    
    for out in layout:
        if hasattr(out, 'get_text'):
            print(out.get_text())