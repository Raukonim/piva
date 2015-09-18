# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:05:38 2015

@author: raukonim
"""

from pylab import *

from scipy.signal import medfilt, order_filter
from scipy.misc import lena

from skimage.measure import structural_similarity as ssim

close('all')
interactive(True)

# Lectura de la imatge original en double per tal de poder fer les
# operacions necessaries sense preocupar-nos de comes flotants i altres
#im=double(imread("eye.jpg"))
im=double(imread("text.gif"))
#im=double(lena())
im=im/255

imr=im[:,:,0]
img=im[:,:,1]
imb=im[:,:,2]

# Generem la imatge luminància amb cada color correctament pesat
L=((.299)*imr)+((.587)*img)+((.114)*imb)


#array de 3x3

#binar=L
binar=medfilt(L,9)>L
binar=abs(1-binar)
figure(0)
imshow(uint8(binar), cmap="gray")


#binar=medfilt(L,i)>L
#figure(i)
#imshow
print ssim(uint8(L), uint8(binar))