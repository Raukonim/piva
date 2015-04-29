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

four_camera=fftshift(fft2(pic))

four_camera_uv=four_camera*uv

camera_uv=abs(ifft2(four_camera_uv))


k=[[0,-1,0],[-1,4,-1],[0,-1,0]]

pic_canny=canny(pic)
camera_lap=convolve(pic_canny, k)

pad=pad(k, ((254, 255), (254, 255)), 'constant')

four_pad=fftshift(fft2(pad))

def circ_filt(R):
    x,y = meshgrid(linspace(-1,1,dimen[0]), linspace(-1,1,dimen[1]))
    circ=sqrt(x*x+y*y)/R
    return circ
    
def gauss_filt(a):
    gauss=exp(-a(x*x+y*y))
    return gauss




subplot(2,2,1)
imshow(pic, cmap='gray')
subplot(2,2,2)
imshow(canny(pic), cmap='gray')
subplot(2,2,3)
imshow(camera_uv, cmap='gray')
subplot(2,2,4)
imshow(camera_lap, cmap='gray')

figure()

imshow(abs(four_pad))