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
    pic_enfoc_four=(pic_four)/((disc_four)+constant_k)
    pic_enfoc=abs(ifft2(pic_enfoc_four))
    pic_enfoc/=pic_enfoc.max()
    pic_enfoc*=255
    pic_enfoc=uint8(pic_enfoc)
    
    
    return pic_enfoc

pic=lena()
dimen=shape(pic)

desenfocada=desenfoc_geometric(pic, 0.05, "desenfoc_geometric.jpeg")

#imshow(desenfocada, cmap='gray')

#for i in range(50):
enfocada=filtre_invers(desenfocada, 0.05, 25)
'''    figure()
    imshow(enfocada, cmap='gray')
'''

desenfocada_sor=desenfocada*(50*(rand(dimen[0], dimen[1])-0.5))

enfocada_sor=filtre_invers(desenfocada, 0.05, 25)

def wiener(imatge_desenfocada, R, k, sigma2):
    D=fftshift(fft2(circ_filt(R)))
    Dc=D.conjugate()
    hw=Dc/(abs(D*Dc)+(k*sigma2))
    im_four=fftshift(fft2(imatge_desenfocada))
    filt_four=im_four*hw
    filt=abs(ifft2(filt_four))
    filt/=filt.max()
    filt*=255    
    imshow(filt, cmap='gray')
    return filt

enfocada_w=wiener(desenfocada_sor,0.05, 80, 1)

#*(50*(rand(dimen[0], dimen[1])-0.5))