#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylab import *

close('all')
interactive(True)

im=double(imread("tormentadeespadas.jpg"))
dimen=im.shape

imrc=zeros([dimen[0],dimen[1], dimen[2]])#,"uint8")
imrc[:,:,0]=im[:,:,0]
imgc=zeros([dimen[0],dimen[1], dimen[2]])#,"uint8")
imgc[:,:,1]=im[:,:,1]
imbc=zeros([dimen[0],dimen[1], dimen[2]])#,"uint8")
imbc[:,:,2]=im[:,:,2]

imr=im[:,:,0]
img=im[:,:,1]
imb=im[:,:,2]

ng=0.333*(imr+img+imb)
ng=uint8(ng)

L=((.299)*imr)+((.587)*img)+((.114)*imb)
L=uint8(L)

D=L-ng

im=uint8(im)
imr=uint8(imr)
img=uint8(img)
imb=uint8(imb)
imrc=uint8(imrc)
imgc=uint8(imgc)
imbc=uint8(imbc)

"""
figure(0)
imshow(im)

figure(1)
imshow(imr, cmap="gray")

figure(2)
imshow(img, tcmap="gray")

figure(3)
imshow(imb, cmap="gray")

figure(4)
imshow(imrc)

figure(5)
imshow(imgc)

figure(6)
imshow(imbc)

figure(7)
imshow(ng, cmap="gray")

figure(8)
imshow(L, cmap="gray")

figure(9)
imshow(D, cmap="jet")"""

imsave("fig1_imrc.png", imrc)
imsave("fig2_imgc.png", imgc)
imsave("fig3_imbc.png", imbc)
imsave("fig4_ng.png", ng, cmap="gray")
imsave("fig5_L.png", L, cmap="gray")
imsave("fig6_D.png", D, cmap="jet")