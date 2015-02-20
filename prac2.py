# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 09:41:22 2015

@author: raukonim
"""

from pylab import *

close('all')
interactive(True)

# Lectura de la imatge original en double per tal de poder fer les
# operacions necessaries sense preocupar-nos de comes flotants i altres
im=double(imread("tormentadeespadas.jpg"))

# Creem tres imatges BN una amb cada capa
imr=im[:,:,0]
img=im[:,:,1]
imb=im[:,:,2]

# Generem la imatge luminància amb cada color correctament pesat
L=((.299)*imr)+((.587)*img)+((.114)*imb)
L=uint8(L)

# binarització
imbin=128 < L 

im=uint8(im)
imbin=255*uint8(imbin)


figure(0)
subplot(3,2,1)
imshow(imbin, cmap="gray")

# lineal
a=63
b=191
imlin=double(L)
imlin[imlin<a]=0
imlin[imlin>b]=255

Min=imlin[((imlin>a) * (imlin<b))].min()
#Min=main.min()
imlin[(imlin>a) * (imlin<b)] -= Min
imlin[(imlin>a) * (imlin<b)] *= 1/(b-a)

imlin=uint8(imlin)

#figure(1)
subplot(3,2,2)
imshow(imlin, cmap="gray")

# gamma
#gamma=uint8(im**2)

#figure(2)
#subplot(3,2,3)
#imshow(gamma)

# logaritmica


#figure(3)
#subplot(3,2,4)

#figure(4)
#subplot(3,2,6)
#imshow(im)



def binar (image, point):
    binaria=128 < image
    binaria=255*uint8(imbin)
    return binaria

def linear (imatge, minim, maxim):
    lineal=double(imatge)
    lineal[lineal<minim]=0
    lineal[lineal>maxim]=255
    Min=lineal[((lineal>minim) * (lineal<maxim))].min()
    lineal[(lineal>minim) * (lineal<maxim)] -= Min
    lineal[(v>minim) * (lineal<maxim)] *= 1/(maxim-minim)
    return lineal

def potencia (imatge, pot):
    gamma=uint8(imatge**pot)
    return gamma

#def log (imatge):