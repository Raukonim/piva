#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:30:54 2015

@author: raukonim
"""

from pylab import *

close('all')
interactive(True)

#256*256 plena de zeros quadrat blanc amb 255 px blancs

negre=zeros([256,256],"uint8")

#blanc=ones([128,128],"uint8")

negre[64:192,64:192]=1

figure(0)
imshow(negre, cmap="gray")