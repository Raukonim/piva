# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:18:54 2015

@author: raukonim
"""

from pylab import *

from scipy.misc import lena, imresize
from numpy.random import rand, seed

lorem=open("Lorem", "r")
lectura=lorem.read()

eye=double(imread("eye.jpg"))
size=shape(eye)



ascii=[ord(i) for i in lectura]


asciiarr=asarray(ascii, dtype="uint8")
fill=zeros(size[0]*size[1]-len(asciiarr))
ascimat=concatenate([asciiarr], [fill])
