
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylab import *

close('all')
interactive(True)

im=imread("tormentadeespadas.jpg")
dimen=im.shape

imrc=zeros([dimen[0],dimen[1], dimen[2]],"uint8")
imrc[:,:,0]=im[:,:,0]


imr=im[:,:,0]
img=im[:,:,1]
imb=im[:,:,2]

figure("original")
imshow(im)

figure(1)
imshow(imr)

figure(2)
imshow(imrc)

imsave("fig1.png",imr)
imsave("fig2.png",imrc)