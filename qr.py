# -*- coding: utf-8 -*-
"""
Created on Tue May 05 09:12:14 2015

@author: afajula
"""

from pylab import *


s="HELLO WORLD"

alfanumeric_table={
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,
    'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
    'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,' ':36,
    '$':37,'%':38,'*':39,'+':40,'-':41,'.':42,'/':43,':':44}

#s=zfill(9)

class qrcode:
    def __init__ (self, data, encoding="0010", version=1, correction="L" ):
        self.data = data
        self.encoding = encoding
        self.version = version
        self.correction = correction
        self.length = len(self.data)
        self.bin_len = bin(self.length)[2:]
        self.qr_matrix = [[0],[0]]
        self.pad_len=0
        self.car_count=9
        
        
    #def caracter_count_indicator(self, version, encoding):
    #    self.car_count=9

    def car_count_calc(self):
        self.pad_len=self.bin_len.zfill(self.car_count)
    
    def define_encoding(self, enc):
        self.encoding=enc
        
    def define_correction(self, corr):
        self.correction=corr
        
    def matrix_init(self):
        self.qr_matrix=zeros([21+(4*(self.version-1))], [21+(4*(self.version-1))])
    
    def alphanumeric_encoding(self):
        z=''
        for i in range(0,self.length,2):
            x=''
            x=self.data[i:i+2]
            print x
            if len(x)==1:
                y=bin(alfanumeric_table[x])[2:]
                y=y.zfill(6)
            else:
                y=bin((45*alfanumeric_table[x[0]])+alfanumeric_table[x[1]])[2:]
                y=y.zfill(11)
            print y
            z+=y
        print z
    
    
hello=qrcode(s)

hello.car_count_calc()

hello.alphanumeric_encoding()
