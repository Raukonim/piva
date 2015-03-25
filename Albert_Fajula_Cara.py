# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:33:28 2015

@author: Albert Fajula Cara

"""


from pylab import *

from scipy.signal import medfilt
from scipy.misc import lena
from skimage.measure import structural_similarity as ssim

close('all')
interactive(True)

# Obtenim la imatge original de lena que hem importat de scipy.misc
Orig=double(lena())

# Binaritzem lena emprant el mètode de les passades pràctiques
I=medfilt(Orig,9)>Orig
I=abs(1-I)

# Prenem la mida de la imatge original que ens servirà com a patró 
# per la resta d'imatges
size=shape(I)

""" Generem una matriu aleatòria mitjançant la funció rand de numpy
Aquesta funció genera nombres aleatòris tals [0, 1), per tant haurem
de binaritzar-la tal com hem fet amb la imatge original
"""
A1=rand(size[0], size[1])
A1=medfilt(A1,9)>A1
A1=abs(1-A1)


"""
Sabem que A1 XOR A2 ens ha de proporcionar la imatge original,
tota la informació que tenim és I i A1, per tant hem de realitzar
un XOR invers entre I i A1, aquesta funció resulta ser XOR i per
tant només cal fer I XOR A1.
"""
A2=I^A1

"""
Reconstruim la imatge original mitjançant el XOR que teniem com a condició
a complir per part de A1 i A2
"""

I2=A1^A2

"""
Comprovem que es tracta de la mateixa imatge mitjançant la 
structural similarity
"""
sim_est=ssim(uint8(I), uint8(I2), win_size=9)
print "Structural similarity de I i I2 ="+ str(sim_est)
# Mostrem les 4 imatges demanades

figure(0)

subplot(2,2,1)
imshow(I, cmap="gray")
xlabel("I")

subplot(2,2,2)
imshow(A1, cmap="gray")
xlabel("A1")

subplot(2,2,3)
imshow(A2, cmap="gray")
xlabel("A2")

subplot(2,2,4)
imshow(I2, cmap="gray")
xlabel("I2")


"""
Per realitzar aquesta encriptació en una imatge de 8 bits faria el tractament 
a cada bit per separat i després tornaria a ajuntar els 8 bits per reconstruir
les imatges de 8 bits.

-> Separar bits, array de 8 capes binaries
-> Generar 8 capes aleatòries
-> Binaritzar-les
-> Fer el XOR entre les 2 arrays binàries de 8 capes
-> Tornar a reconstruir les 3 imatges a partir de les arrays de 8 capes

Per poder obtenir la imatge original a partir de A1 i A2 hauriem de separar-les
en 8 capes, realitzar el XOR i tornar a reconstruir la imatge
a partir de les 8 capes
"""


I8=zeros([size[0],size[1], 8])

I8[:,:,0]=(Orig%2)/2
I8[:,:,1]=(Orig%4-I8[:,:,0])/4
I8[:,:,2]=(Orig%8-I8[:,:,1]-I8[:,:,0])/8
I8[:,:,3]=(Orig%16-I8[:,:,2]-I8[:,:,1]-I8[:,:,0])/16
I8[:,:,4]=(Orig%32-I8[:,:,3]-I8[:,:,2]-I8[:,:,1]-I8[:,:,0])/32
I8[:,:,5]=(Orig%64-I8[:,:,4]-I8[:,:,3]-I8[:,:,2]-I8[:,:,1]-I8[:,:,0])/64
I8[:,:,6]=(Orig%128-I8[:,:,5]-I8[:,:,4]-I8[:,:,3]-I8[:,:,2]-I8[:,:,1]-I8[:,:,0])/128
I8[:,:,7]=(Orig%256-I8[:,:,6]-I8[:,:,5]-I8[:,:,4]-I8[:,:,3]-I8[:,:,2]-I8[:,:,1]-I8[:,:,0])/256

I8=medfilt(I8,3)>I8
I8=abs(1-I8)

A18=rand(size[0], size[1], 8)
A18=uint8((255*A18) > 128)

A18b=A18[:,:,0]
A18b+=A18[:,:,1]*2
A18b+=A18[:,:,2]*4
A18b+=A18[:,:,3]*8
A18b+=A18[:,:,4]*16
A18b+=A18[:,:,5]*32
A18b+=A18[:,:,6]*64
A18b+=A18[:,:,7]*128

A28=uint8((I8 != 0)^A18)


A28b=A28[:,:,0]
A28b+=A28[:,:,1]*2
A28b+=A28[:,:,2]*4
A28b+=A28[:,:,3]*8
A28b+=A28[:,:,4]*16
A28b+=A28[:,:,5]*32
A28b+=A28[:,:,6]*64
A28b+=A28[:,:,7]*128

I28=A18^A28

I28b=I28[:,:,0]
I28b+=I28[:,:,1]*2
I28b+=I28[:,:,2]*4
I28b+=I28[:,:,3]*8
I28b+=I28[:,:,4]*16
I28b+=I28[:,:,5]*32
I28b+=I28[:,:,6]*64
I28b+=I28[:,:,7]*128

sim_est2=ssim(uint8(I), uint8(I28b), win_size=9)
print "Structural similarity de I i I28b ="+ str(sim_est2)

figure(1)
subplot(2,2,1)
imshow(Orig, cmap="gray")
xlabel("I")

subplot(2,2,2)
imshow(A18b, cmap="gray")
xlabel("A18b")

subplot(2,2,3)
imshow(A28b, cmap="gray")
xlabel("A28b")

subplot(2,2,4)
imshow(I28b, cmap="gray")
xlabel("I28b")