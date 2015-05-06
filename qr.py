# -*- coding: utf-8 -*-
"""
Created on Tue May 05 09:12:14 2015

@author: afajula
"""

from pylab import *


s="HELLO WORLD"



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
        
        

    def car_count_calc(self, self.version)
        
        
        self.pad_len=self.bin_len.zfill(car_count)
    
    def define_encoding(self, enc):
        self.encoding=enc
        
    def define_correction(self, corr):
        self.correction=corr
        
    def matrix_init(self):
        self.qr_matrix=zeros([21+(4*(self.version-1))], [21+(4*(self.version-1))])
    
    #def caracter_count_indicator(self, version, encoding):
    #    car_count=9
    
    
hello=qrcode(s)