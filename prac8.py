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

from skimage.data import camera, moon
from skimage.filter import canny

from scipy.misc import lena
from scipy.ndimage.filters import convolve


close("all")
interactive(True)

pic = uint8(lena())
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

"""
figure()

imshow(abs(four_pad))
"""

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



pic_soroll_50=zeros([dimen[0], dimen[1], 50])

for i in range(0,50):
    pic_soroll_50[:,:,i]=pic+(50*rand(dimen[0], dimen[1])-0.5)
    #subplot(5,10,i+1)
    #imshow(pic_soroll_50[:,:,i], cmap="gray")

suma=zeros([dimen[0], dimen[1], 51])
a=0
figure()
for n in [2,5,10,50]:
    a+=1
    for l in range(0,n):
        suma[:,:,n]+=pic_soroll_50[:,:,l]
        
    suma[:,:,n]/=n
    
    subplot(2,2,a)
    imshow(suma[:,:,n], cmap='gray')

rectangular=[[1,1,1],[1,1,1],[1,1,1]]
triangular=[[1,1,1],[1,2,1],[1,1,1]]
gaussia=[[1,2,1],[2,4,2],[1,2,1]]
laplacia=[[0,-1,0],[-1,4,-1],[0,-1,0]]
alt1=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
alt2=[[1,-2,1],[-2,4,-2],[1,-2,1]]
nord=[[1,1,1],[1,-2,1],[-1,-1,-1]]
opcio1=[[0,-1,0],[-1,5,-1],[0,-1,0]]
opcio2=[[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
opcio3=[[1,-2,1],[-2,5,-2],[1,-2,1]]

pic2=lena()

pic_conv_rect=convolve(pic2, rectangular)
pic_conv_tri=convolve(pic2, triangular)
pic_conv_gaus=convolve(pic2, gaussia)

pic_conv_lap=convolve(pic2, laplacia)
pic_conv_alt1=convolve(pic2, alt1)
pic_conv_alt2=convolve(pic2, alt2)
pic_conv_nord=convolve(pic2, nord)

pic_conv_op1=convolve(pic2, opcio1)
pic_conv_op2=convolve(pic2, opcio2)
pic_conv_op3=convolve(pic2, opcio3)


figure()
subplot(1,3,1)
title("Rectangular")
imshow(pic_conv_rect, cmap='gray')
subplot(1,3,2)
title("Triangular")
imshow(pic_conv_tri, cmap='gray')
subplot(1,3,3)
title("Gaussia")
imshow(pic_conv_gaus, cmap='gray')


figure()
subplot(2,2,1)
title("Laplacia")
imshow(pic_conv_lap, cmap='gray')
subplot(2,2,2)
title("Alt1")
imshow(pic_conv_alt1, cmap='gray')
subplot(2,2,3)
title("Alt2")
imshow(pic_conv_alt2, cmap='gray')
subplot(2,2,4)
title("Nord")
imshow(pic_conv_nord, cmap='gray')

figure()
subplot(1,3,1)
title("opcio1")
imshow(pic_conv_op1, cmap='gray')
subplot(1,3,2)
title("opcio2")
imshow(pic_conv_op2, cmap='gray')
subplot(1,3,3)
title("opcio3")
imshow(pic_conv_op3, cmap='gray')



L1=convolve(pic2, [[-1,0,1],[-2,0,2],[-1,0,1]])
L2=convolve(pic2, [[1,2,1],[0,0,0],[-1,-2,-1]])
sobel=sqrt(L1*L1+L2*L2)
figure()
imshow(sobel, cmap='gray')


R1=convolve(pic2, [[1,0],[0,-1]])
R2=convolve(pic2, [[0,1],[-1,0]])
roberts
