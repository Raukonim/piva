# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:58:14 2015

@author: raukonim
"""

from pylab import *

close('all')
interactive(True)

# Lectura de la imatge original en double per tal de poder fer les
# operacions necessaries sense preocupar-nos de comes flotants i altres
im=double(imread("tormentadeespadas.jpg"))

# Creem tres imatges BN una amb cada capa
imr=im[:,:,0]
img=im[:,:,1]
imb=im[:,:,2]

# Generem la imatge luminància amb cada color correctament pesat
L=((.299)*imr)+((.587)*img)+((.114)*imb)


cmap=np.array([256,3])