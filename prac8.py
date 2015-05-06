# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:59:29 2015

@author: raukonim
"""
"""
derivades imatge

1D

f_i'=f_i+1-f_i

f_i''=-f_i+1+2f_i-f_i-1=-f_i o (-1,2,-1) (combolució)

2D
f_ij'=f_i+1j+fij+1-2fij

f''=-fij o (-1,2,-1)(-1,2,-1)^t=abs( -fij o [(0,-1,0),(-1,4,-1),(0,-1,0)])

"""

from pylab import *

from skimage.data import camera
from skimage.filter import canny

from scipy.misc import lena
from scipy.ndimage.filters import convolve


close("all")
interactive(True)

pic = camera()
dimen=shape(pic)

x,y = meshgrid(linspace(-1,1,dimen[0]), linspace(-1,1,dimen[1]))

uv=x*x+y*y

four_pic=fftshift(fft2(pic))

four_pic_uv=four_pic*uv

pic_uv=abs(ifft2(four_pic_uv))


k=[[0,-1,0],[-1,4,-1],[0,-1,0]]

pic_canny=canny(pic)
pic_lap=convolve(pic_canny, k)

pad=pad(k, ((254, 255), (254, 255)), 'constant')

four_pad=fftshift(fft2(pad))

subplot(2,2,1)
title('Original')
imshow(pic, cmap='gray')
subplot(2,2,2)
title('canny')
imshow(pic_canny, cmap='gray')
subplot(2,2,3)
title('parabol')
imshow(pic_uv, cmap='gray')
subplot(2,2,4)
title('Laplaciana')
imshow(pic_lap, cmap='gray')


figure()

imshow(abs(four_pad))

def circ_filt(R):
    x,y = meshgrid(linspace(-1,1,dimen[0]), linspace(-1,1,dimen[1]))
    circ=sqrt(x*x+y*y)<R
    return circ
    
def gauss_filt(a):
    x,y = meshgrid(linspace(-1,1,dimen[0]), linspace(-1,1,dimen[1]))
    gauss=exp(-a*(x*x+y*y))
    return gauss


soroll=50*rand(dimen[0], dimen[1])-0.5

pic_sor=pic+soroll

pic_sor_four=fftshift(fft2(pic_sor))

pic_sor_circ=abs(ifft2(pic_sor_four*circ_filt(0.5)))

pic_sor_gauss=abs(ifft2(pic_sor_four*gauss_filt(1.0)))

figure()
subplot(1,2,1)
title('Filtre Circular')
imshow(pic_sor_circ, cmap='gray')
subplot(1,2,2)
title('Filtre Gaussia')
imshow(pic_sor_gauss, cmap='gray')