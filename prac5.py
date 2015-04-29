# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:32:10 2015

@author: raukonim
"""

from pylab import *
from scipy.misc import lena
from numpy import binary_repr
from skimage.data import moon


def pcb(imatge):

    """
    _____________________________
    |7   |6   |5   |4   |3   |2   |1   |0   |
    |____|____|___________________|
    |128 |64  |32  |16  |8   |4   |2   |1   |
    |_____________________________|
    |R   |G   |B   |R   |B   |G   |B   |G   |
    |_____________________________|    
    """    
    R1 =(100,0,0)
    R2 =(200,0,0)
    G1 =(0,100,0)
    G2 =(0,200,0)
    G3 =(0,255,0)
    B1 =(0,0,100)
    B2 =(0,0,200)
    B3 =(0,0,255)
    
    dim=imatge.shape
    binaris=reshape(imatge, dim[0]*dim[1])
    binaris=[binary_repr(i, width=8) for i in binaris]    
    
    binaris=resize(binaris, [dim[0], dim[1]])
    
    return binaris

im=uint8(moon())

imatge_rgb=pcb(im)

