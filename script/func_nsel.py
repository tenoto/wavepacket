#!/usr/bin/env python

import math
import numpy as np
from scipy import special

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xi = np.linspace(-8,8,200)

omega = 1.0+0j
kappa0 = 0+1j 
#used_n = [9,10,11]
used_n = [8,9,10,11,12]

fig, ax = plt.subplots(1,1,figsize=(11.69,8.27)) 
plt.rcParams["mathtext.fontset"] = "dejavuserif"	
plt.rcParams["font.size"] = 18
plt.rcParams["font.family"] = "serif"
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
ax.set_xlabel('X',fontsize=20)		
ax.set_ylabel('Probability Density',fontsize=20)

ims = []
for dt in np.arange(0,2*np.pi,2*np.pi/2**6):
	t = dt + 0j
	y = np.zeros(len(xi)).astype(complex)
	for n in used_n:
		yn = special.hermite(n)(xi)/math.factorial(n)
		yn *= np.exp(-xi**2/2.0)
		yn = yn.astype(complex)
		yn *= (kappa0 * np.exp(-(0+1j)*omega*t))**n
		y += yn 	

	plt.tick_params(axis="both", which='major', direction='in', length=8)
	plt.tick_params(axis="both", which='minor', direction='in', length=5)
	plt.grid(True,which='major',linestyle='-')
	plt.grid(True,which='minor',linestyle='-.')
	plt.minorticks_on()
	plt.tight_layout(pad=2)
	plt.title('Hermite n = %s' % used_n)
	line, = plt.plot(np.real(xi),np.abs(y)**2,"r")
	ims.append([line])

outgif = 'wave' 
for n in used_n:
	outgif += '_%d' % n
outgif += '.gif'	
ani = animation.ArtistAnimation(fig, ims)
ani.save(outgif,writer="imagemagick")