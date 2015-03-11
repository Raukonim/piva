# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:36:26 2015

@author: raukonim
"""

from pylab import *

from scipy.misc import lena, imresize
from numpy.random import rand, seed


close('all')
interactive(True)

im=double(imread("eye.jpg"))

esteg_color=im-(im%4)

size=shape(im)
secreta=imresize(double(lena()/64), size)
#secreta/=4

dimen=im.shape
secreta_col=zeros([dimen[0], dimen[1], dimen[2]])
secreta_2=(secreta%4)
secreta_4=(secreta%16)/4
secreta_6=(secreta%64)/16

secreta_col[:,:,0]=secreta_2
secreta_col[:,:,1]=secreta_4
secreta_col[:,:,2]=secreta_6
secreta_col/=3


show=
