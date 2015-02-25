# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 09:41:22 2015

@author: raukonim
"""

from pylab import *
from scipy.ndimage.measurements import histogram

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

#L=uint8(L)

# binarització
imbin=128 < uint8(L)

im=uint8(im)
imbin=255*uint8(imbin)


figure(0)

#figure(4)
subplot(3,3,1)
imshow(im)

subplot(3,3,2)
#L=uint8(L)
imshow(uint8(L), cmap="gray")

subplot(3,3,3)
imshow(imbin, cmap="gray")

# lineal
a=129
b=197
imlin=uint8(L)
imlin[imlin<a]=0
imlin[imlin>b]=255

Min=imlin[((imlin>a) * (imlin<b))].min()
#Min=main.min()
imlin[(imlin>a) * (imlin<b)] -= Min
imlin[(imlin>a) * (imlin<b)] *= 1/(b-a)

imlin=uint8(imlin)

#figure(1)
subplot(3,3,4)
imshow(imlin, cmap="gray")

# gamma
gamma=(L**1.3)
gamma /= gamma.max()

#figure(2)
subplot(3,3,5)
imshow(gamma, cmap="gray")

# logaritmica

imlog =((log10(L+1)))
imlog /= imlog.max() 

#figure(3)
subplot(3,3,6)
imshow(imlog, cmap="gray")

# periodica

imper=(L/L.max())
#imper/=imper.max()

subplot(3,3,7)
imshow(imper, cmap="gray")


# histograma

#suma = L.cumsum()
hist=histogram(L, L.min(), L.max(),256)
suma=hist.cumsum()
eq=suma[uint8(L)]/255


subplot(3,3,8)
imshow(eq, cmap="gray")

figure(7)
#subplot(3,3,8)
plt.plot(hist)

figure(8)
plt.plot(suma)

hist2=histogram(eq, eq.min(), eq.max(),256)
figure(10)

plt.plot(hist2)

figure(11)
plt.plot(hist2.cumsum())

eye=double(imread("eye.jpg"))

# Creem tres imatges BN una amb cada capa
eyer=eye[:,:,0]
eyeg=eye[:,:,1]
eyeb=eye[:,:,2]


histr=histogram(eyer,eyer.min(), eyer.max(), 256)
histg=histogram(eyeg,eyeg.min(), eyeg.max(), 256)
histb=histogram(eyeb,eyeb.min(), eyeb.max(), 256)

sumr=histr.cumsum()
sumg=histg.cumsum()
sumb=histb.cumsum()

eqr=sumr[uint8(eyer)]
eqg=sumg[uint8(eyeg)]
eqb=sumb[uint8(eyeb)]

dimen=eye.shape
eqc=zeros([dimen[0], dime[1], dimen[2]])

eqc[:,:,0]=uint8(eqr)
eqc[:,:,1]=uint8(eqg)
eqc[:,:,2]=uint8(eqb)

figure(12)
imshow(eqc)

hist3=histogram(eqc, eqc.min(), eqc.max(),255)
figure(13)

plt.plot(hist3)

figure(14)
plt.plot(hist3.cumsum())

#################################################################
def binar (image, point):
    binaria=128 < image
    binaria=255*uint8(imbin)
    return binaria

def linear (imatge, minim, maxim):
    lineal=double(imatge)
    lineal[lineal<minim]=0
    lineal[lineal>maxim]=255
    Min=lineal[((lineal>minim) * (lineal<maxim))].min()
    lineal[(lineal>minim) * (lineal<maxim)] -= Min
    lineal[(v>minim) * (lineal<maxim)] *= 1/(maxim-minim)
    return lineal

def potencia (imatge, pot):
    gamma=uint8(imatge**pot)
    return gamma

#def log (imatge):