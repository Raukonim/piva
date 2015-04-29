# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:37:42 2015

@author: raukonim
"""

from pylab import *

from scipy.misc import lena
from skimage.data import camera


close("all")
interactive(True)


imfourier=fftshift(fft2(lena()))
dimen=imfourier.shape

x,y=meshgrid(linspace(-1,1,dimen[0]), linspace(-1,1,dimen[1]))

filt=sqrt(x*x+y*y)

passhigh=filt>0.6

passlow=filt<0.15

passband=(passhigh+passlow)==0

result=zeros([dimen[0],dimen[1],3], "complex")

result[:,:,0]=passlow*imfourier
result[:,:,1]=passband*imfourier
result[:,:,2]=passhigh*imfourier

iresult=zeros([dimen[0],dimen[1],3], "complex")

iresult[:,:,0]=ifft2(result[:,:,0])
iresult[:,:,1]=ifft2(result[:,:,1])
iresult[:,:,2]=ifft2(result[:,:,2])

filtrada=abs(iresult)
filtrada[:,:,0]/=filtrada[:,:,0].max()
filtrada[:,:,1]/=filtrada[:,:,1].max()
filtrada[:,:,2]/=filtrada[:,:,2].max()

"""
figure()
imshow(, cmap='gray')
"""