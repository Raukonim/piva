# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:05:45 2015

@author: raukonim
"""

from pylab import *

from scipy.misc import lena, imresize


close('all')
interactive(True)

im=uint8(lena())

imsecreta=double(imread("eye.jpg"))/255

imr=imsecreta[:,:,0]
img=imsecreta[:,:,1]
imb=imsecreta[:,:,2]

# Generem la imatge luminància amb cada color correctament pesat
secreta_gran=((.299)*imr)+((.587)*img)+((.114)*imb)

size=shape(im)
secreta=imresize(secreta_gran, size)
secreta=secreta/16

esteg=(im-(im%16))+secreta


figure(0)
imshow(esteg, cmap="gray")
figure(1)
imshow(secreta, cmap="gray")
figure(2)
imshow(secreta_gran, cmap="gray")