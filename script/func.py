#!/usr/bin/env python

import math
import numpy as np
from scipy import special

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xi = np.linspace(-5,5,100)

omega = 1.0+0j
kappa0 = 0+1j 
#max_n = 10
max_n = 10

fig, ax = plt.subplots(1,1,figsize=(11.69,8.27)) 
ax.set_xlabel('x',fontsize=20)		
ax.set_ylabel('density',fontsize=20)

ims = []
for dt in np.arange(0,2*np.pi,2*np.pi/2**6):
	t = dt + 0j
	y = np.zeros(len(xi)).astype(complex)
	for n in range(max_n):
		yn = special.hermite(n)(xi)/math.factorial(n)
		yn *= np.exp(-xi**2/2.0)
		yn = yn.astype(complex)
		yn *= (kappa0 * np.exp(-(0+1j)*omega*t))**n
		y += yn 	

	plt.title('Hermite n=0..%d' % max_n)
	line, = plt.plot(np.real(xi),np.abs(y)**2,"r")
	ims.append([line])

outgif = 'func_maxn%d.gif' % max_n
ani = animation.ArtistAnimation(fig, ims)
ani.save(outgif,writer="imagemagick")