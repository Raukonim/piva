# -*- coding: utf-8 -*-
"""
Created on Tue May 05 09:12:14 2015

@author: afajula
"""

from pylab import *


s="HELLO WORLD"
alphanumeric_table2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
numeric_table ="0123456789"
alphanumeric_table={
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,
    'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
    'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,' ':36,
    '$':37,'%':38,'*':39,'+':40,'-':41,'.':42,'/':43,':':44}

#s=zfill(9)

class qrcode:
    def __init__ (self, data, version=1, correction="L" ):
        
                
        self.data = data.decode('utf-8') #Convertim tot a Unicode
        self.comp_dades()        
        self.mode = self.define_mode()
        self.version = version
        self.correction = correction
        self.length = len(self.data)
        self.bin_len = bin(self.length)[2:]
        self.qr_matrix = [[0],[0]]
        self.car_count=9
        self.pad_len=self.car_count_calc()
        self.check_len()
        
    #def caracter_count_indicator(self, version, encoding):
    #    self.car_count=9
        """
        Numeric	7089 characters
        Alphanumeric	4296 characters
        Byte	2953 characters
        Kanji	1817 characters
        """
    def check_len(self):
        a={'0001':7089,'0010':4296,'0100':2953}
        print a['0010']
        if (self.length>a[self.mode]):
            print 'ERROR'
            #exit()
            

    def car_count_calc(self):
        self.pad_len=self.bin_len.zfill(self.car_count)
    
    def comp_dades(self):
        for c in self.data:
            try:
                c.encode('latin1')
            except UnicodeEncodeError:
                print "ERROR!"
                
    def define_mode(self):
        numeric =[x in numeric_table for x in self.data]
        alpha = [x in alphanumeric_table2 for x in self.data]
        if False in numeric:
            if False in alpha:
                 self.mode = '0100' #Byte
            else:
                self.mode = '0010' #Alpha
        else:
            self.mode = '0001'#Numeric
    
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
                y=bin(alphanumeric_table[x])[2:]
                y=y.zfill(6)
            else:
                y=bin((45*alphanumeric_table[x[0]])+alphanumeric_table[x[1]])[2:]
                y=y.zfill(11)
            print y
            z+=y
        print z
    
    
hello=qrcode(s)

hello.car_count_calc()

hello.alphanumeric_encoding()
hello.comp_dades()
hello.define_mode()