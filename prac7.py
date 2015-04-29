# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:37:15 2015

@author: raukonim
"""

from pylab import *

from scipy.misc import lena
from skimage.data import moon, chelsea


close("all")
interactive(True)

def fftamp(pic):
    
    amplitud=log10(abs(fftshift(fft2(pic)))+1)
    
    return amplitud
    
def ifftamp(pic):
    
    iamplitud=log10(abs(ifft2(ifftshift(pic)))+1)
    
    return iamplitud

def fftang(pic):
    
    fase=angle(fftshift(fft2(pic)))
    
    return fase

def ifftang(pic):
    
    ifase=angle(ifft2(pic))
    
    return ifase

lena_amp=fftamp(lena())

moon_amp=fftamp(moon())

lena_fase=fftang(lena())

moon_fase=fftang(moon())

mix1=lena_amp*exp(1j*(moon_fase))

mix2=moon_amp*exp(1j*(lena_fase))

mix1_four=abs(ifft2(mix1))

mix2_four=abs(ifft2(mix2))

moon_1fase=abs(ifft2(moon_fase))

lena_1fase=abs(ifft2(lena_fase))


test=zeros(lena().shape)

p=8.0
#0,31,63,95,127,159,191,224, 255 

x,y=meshgrid(linspace(0,1,512), linspace(0,1,512))
test = abs(sin(9*pi*x)<0)

test_amp=fftamp(test)
test_fase=fftang(test)
"""
figure()
subplot(2,1,1)
imshow(fftamp(lena()))
subplot(2,1,2)
plot(fftamp(lena()))
"""

figure()

subplot(3,2,1)
imshow(lena(), cmap="gray")

subplot(3,2,2)
imshow(moon(), cmap="gray")

subplot(3,2,3)
imshow(lena_amp, cmap="gray")

subplot(3,2,4)
imshow(moon_amp, cmap="gray")

subplot(3,2,5)
imshow(lena_fase, cmap="gray")

subplot(3,2,6)
imshow(moon_fase, cmap="gray")

figure()

subplot(3,2,1)
imshow(log10(abs(mix1)+1), cmap="gray")

subplot(3,2,2)
imshow(log10(abs(mix2)+1), cmap="gray")

subplot(3,2,3)
imshow(mix1_four, cmap="gray")

subplot(3,2,4)
imshow(mix2_four, cmap="gray")

subplot(3,2,5)
imshow(lena_1fase, cmap="gray")

subplot(3,2,6)
imshow(moon_1fase, cmap="gray")

figure()
imshow(test, cmap="gray")

figure()
plot(abs(test_amp[256,:]))

figure()
imshow(abs(ifft2(test_fase)), cmap='gray')