# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:57:16 2015

@author: Albert Fajula Cara

Copyright (C) 2015  Albert Fajula Cara

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
"""

from pylab import *
from skimage.data import camera, chelsea
from scipy.ndimage.measurements import histogram
from skimage.filters import threshold_isodata

interactive(True)
close('all')

im=double(camera())


# Histograma

hist=histogram(im, im.min(), im.max(),256)

# Ridler-Calvard

T_rc=threshold_isodata(im, nbins=256)

rc=T_rc < uint8(im)


# Bimodal
a=0
b=256
suma_T0=0
suma_T0_1=1


for i in range(1000):
    T0=(a+b)/2
    suma_T0=hist[a:T0].cumsum().max()
    suma_T0_1=hist[T0+1:b].cumsum().max()
    
    #print a, T0, b, suma_T0, suma_T0_1

    if suma_T0 > suma_T0_1:
        a+=1
    elif suma_T0 < suma_T0_1:
        b-=1
    elif suma_T0 == suma_T0_1:
        break
    
bimodal=T0 < uint8(im)

# Impressió de les figures demanades en l'exercici
figure()
subplot(1,3,1)
title("Histograma")
plt.plot(hist)

subplot(1,3,2)
title("Isodata, llindar: " + str(T_rc)[:2])
imshow(rc, cmap='gray')

subplot(1,3,3)
title("Bimodal, llindar: " + str(T0))
imshow(bimodal, cmap='gray')




# Problema 2


chel_col=double(chelsea())

# Transformació de la imatgen en blanc i negre emprant la luminància

chel=((.299)*chel_col[:,:,0])+((.587)*chel_col[:,:,1])+((.114)*chel_col[:,:,2])
dimen=shape(chel)

# funció que genera el filtre de Butterworth
def Butterworth(n):
    x,y = meshgrid(linspace(0,2,dimen[1]), linspace(0,2,dimen[0]))
    G=sqrt(1/(1+(sqrt(x*x+y*y)**(2*n))))
    return G

# Generem els filtres passa alt i passabaig
Alt=1-Butterworth(3)
Baix=Butterworth(5)

# Transformem la imatge a l'espai de Fourier
chel_four=fftshift(fft2(chel))

# Apliquem els filtres a la imatge i tornem de l'espai de Fourier a l'espai Real
chel_alt=zeros(dimen)
chel_baix=zeros(dimen)

chel_alt=abs(ifft2(chel_four*Alt))
chel_baix=abs(ifft2(chel_four*Baix))

# Impressió de les figures demanades en l'exercici
figure()
subplot(2,2,1)
title("Passa alt")
imshow(chel_alt, cmap='gray')
subplot(2,2,2)
title("Passa baix")
imshow(chel_baix, cmap='gray')
subplot(2,2,3)
title("G(w) Passa alt")
plt.plot(Alt[1,:])
subplot(2,2,4)
title("G(w) Passa baix")
plt.plot(Baix[1,:])

