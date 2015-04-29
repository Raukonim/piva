# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 15:48:01 2015

@author: UB
"""

from pylab import *
from matplotlib.colors import LinearSegmentedColormap

def defmapalineal(a,b):
    mapa = {'red':  ((0.0,0.0,0.0),
                     (a,  0.0,0.0),
                     (b,  1.0,1.0),
                     (1.0,1.0,1.0)),
            'green':((0.0,0.0, 0.0),
                     (a,  0.0, 0.0),
                     (b,  1.0, 1.0),
                     (1.0,1.0,1.0)),
            'blue': ((0.0,0.0, 0.0),
                     (a,  0.0, 0.0),
                     (b,  1.0, 1.0),
                     (1.0,1.0, 1.0))}               
    return LinearSegmentedColormap('MapaLineal',mapa)


                   
close('all')
interactive(True)

im=imread("tormentadeespadas.jpg")
dimen=im.shape

mapa_lineal=defmapalineal(0.25,0.45)

figure() 
imshow(im[:,:,1],cmap=mapa_lineal)


