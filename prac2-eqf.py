#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 09:47:01 2015

@author: artur

Practica 2. Equalitzacio histograma imatge com a funció
http://en.wikipedia.org/wiki/Histogram_equalization

Atenció no fer servir numpy.lib.function_module.histogram 
"""

from pylab import *
from scipy.ndimage.measurements import histogram



def equhistim(imatge):
    histo=histogram(imatge,0, 255, bins=256)
    histoac=histo.cumsum()
    imatge_eq=uint8(255.*histoac[imatge]/histoac.max())
    histo_eq=histogram(imatge_eq,0, 255, bins=256)
    return imatge_eq, histo, histo_eq
    
close('all')
interactive(True)

im=imread("muntanya.jpg")
dimen=im.shape

ime,his_im,his_ime=equhistim(im[:,:,1])
#his_ime.cumsum().max() = 126900
#dimen[0]*dimen[1] = 126900

figure() 
subplot(3,2,1)
imshow(im[:,:,1])
gray()

subplot(3,2,2)
imshow(ime,cmap='gray')
subplot(3,2,3)
plot(his_im)
subplot(3,2,4)
plot(his_im.cumsum())
subplot(3,2,5)
plot(his_ime)
subplot(3,2,6)
plot(his_ime.cumsum())