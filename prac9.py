# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:01:24 2015

@author: raukonim
"""

from pylab import *

from scipy.misc import lena

close('all')
interactive(True)

def circ_filt(R):
    x,y = meshgrid(linspace(-1,1,dimen[0]), linspace(-1,1,dimen[1]))
    circ=sqrt(x*x+y*y)<R
    return circ
    
def desenfoc_geometric(imatge_original, radi_cercle, nom_arxiu):
    
    disc=circ_filt(radi_cercle)
    
    disc_four=fftshift(fft2(disc))
    
    pic_four=fftshift(fft2(imatge_original))
    
    pic_desen_four=disc_four*pic_four
    pic_desen=abs(ifft2(pic_desen_four))
    pic_desen/=pic_desen.max()
    pic_desen*=255
    pic_desen=uint8(pic_desen)
    imsave(nom_arxiu, pic_desen, cmap='gray')
    
    return pic_desen
    
def filtre_invers(imatge_desenfocada, radi_cercle, constant_k):
    disc=circ_filt(radi_cercle)
    disc_four=fftshift(fft2(disc))
    
    
    pic_four=pic_four=fftshift(fft2(imatge_desenfocada))
    pic_enfoc=abs(ifft2(pic_four/(abs(disc_four)+constant_k)))
    pic_enfoc/=pic_enfoc.max()
    pic_enfoc*=255
    pic_enfoc=(pic_enfoc)
    
    
    return pic_enfoc

pic=lena()
dimen=shape(pic)

desenfocada=desenfoc_geometric(pic, 0.2, "desenfoc_geometric.jpeg")

#imshow(desenfocada, cmap='gray')

enfocada=filtre_invers(desenfocada, 0.2, 1)

imshow(enfocada, cmap='gray')