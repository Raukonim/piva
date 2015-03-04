# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:28:38 2015

@author: raukonim
"""

from pylab import *
from scipy.ndimage.measurements import histogram

close('all')
interactive(True)

eye=imread("eye.jpg")

# Creem tres imatges BN una amb cada capa
eyer=eye[:,:,0]
eyeg=eye[:,:,1]
eyeb=eye[:,:,2]

eyer=uint8(eyer)
eyeg=uint8(eyeg)
eyeb=uint8(eyeb)


histr=histogram(eyer ,eyer.min(), eyer.max(), 256)
histg=histogram(eyeg ,eyeg.min(), eyeg.max(), 256)
histb=histogram(eyeb ,eyeb.min(), eyeb.max(), 256)

sumr=histr.cumsum()
sumg=histg.cumsum()
sumb=histb.cumsum()

eqr=255*(double(sumr[eyer])/double(sumr[eyer]).max())
eqg=255*(double(sumg[eyeg])/double(sumg[eyeg]).max())
eqb=255*(double(sumb[eyeb])/double(sumb[eyeb]).max())


dimen=eye.shape
eqc=zeros([dimen[0], dimen[1], dimen[2]], uint8)

eqc[:,:,0]=uint8(eqr)
eqc[:,:,1]=uint8(eqg)
eqc[:,:,2]=uint8(eqb)

figure(0)
imshow(uint8(eye))

figure(1)
imshow(uint8(eqc))
eqc=uint8(eqc)
hist3=histogram(eqc, eqc.min(), eqc.max(),256)
figure(2)

plt.plot(histr, color="red")
plt.plot(histg, color="green")
plt.plot(histb, color="blue")
plt.plot(hist3, color="black")

"""
figure(3)
plt.plot(histr.cumsum(), color="red")
plt.plot(histg.cumsum(), color="green")
plt.plot(histb.cumsum(), color="blue")
"""
histr2=histogram(eqr ,eqr.min(), eqr.max(), 256)
histg2=histogram(eqg ,eqg.min(), eqg.max(), 256)
histb2=histogram(eqb ,eqb.min(), eqb.max(), 256)
"""
figure(4)

plt.plot(histr2, color="red")
plt.plot(histg2, color="green")
plt.plot(histb2, color="blue")
plt.plot(hist3, color="black")
"""
figure(5)
plt.plot(histr2.cumsum(), color="red")
plt.plot(histg2.cumsum(), color="green")
plt.plot(histb2.cumsum(), color="blue")
plt.plot(hist3.cumsum(), color="black")