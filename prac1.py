#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:10:54 2015

@author: raukonim
"""

from pylab import *

close('all')
interactive(True)

# Lectura de la imatge original en double per tal de poder fer les
# operacions necessaries sense preocupar-nos de comes flotants i altres
im=double(imread("tormentadeespadas.jpg"))
# Prenem la mida a la imatge per si necessitem emprarles per generar-ne altres
dimen=im.shape

"""
Creem tres imatges a color amb cadascuna de les capes de la imatge original.
Per poder-ho fer necessitem la mida original, dimen, i les hem d'omplir
de zeros ja que sols emprarem 1 capa de color mentre les altrs son zero. 
"""
imrc=zeros([dimen[0],dimen[1], dimen[2]])#,"uint8")
imrc[:,:,0]=im[:,:,0]
imgc=zeros([dimen[0],dimen[1], dimen[2]])#,"uint8")
imgc[:,:,1]=im[:,:,1]
imbc=zeros([dimen[0],dimen[1], dimen[2]])#,"uint8")
imbc[:,:,2]=im[:,:,2]

# Creem tres imatges BN una amb cada capa
imr=im[:,:,0]
img=im[:,:,1]
imb=im[:,:,2]

# Generem una imatge BN mitjana
ng=0.333*(imr+img+imb)
ng=uint8(ng)

# Generem la imatge luminància amb cada color correctament pesat
L=((.299)*imr)+((.587)*img)+((.114)*imb)
L=uint8(L)

# Generem la imatge diferència
D=L-ng

# Convertim totes les imatges a enters de 8 bits
im=uint8(im)
imr=uint8(imr)
img=uint8(img)
imb=uint8(imb)
imrc=uint8(imrc)
imgc=uint8(imgc)
imbc=uint8(imbc)

# Mostres totes les figures per pantalla
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

# Guardem les imatges
imsave("fig1_imrc.png", imrc)
imsave("fig2_imgc.png", imgc)
imsave("fig3_imbc.png", imbc)
imsave("fig4_ng.png", ng, cmap="gray")
imsave("fig5_L.png", L, cmap="gray")
imsave("fig6_D.png", D, cmap="jet")
