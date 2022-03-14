#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fontsize = 18 

omega = 0.1 
xi = np.linspace(-5,5,100).astype(complex)

fig, ax = plt.subplots(1,1,figsize=(11.69,8.27)) 
ax.set_xlabel('x',fontsize=fontsize)		
ax.set_ylabel('density',fontsize=fontsize)

ims = []
for t in np.arange(0,100,1):
	yi = np.exp(-(xi-np.sin(omega*t))**2)
	line, = plt.plot(np.real(xi), np.real(yi), "r")
	ims.append([line])

ani = animation.ArtistAnimation(fig, ims)
ani.save('wavepacket.gif', writer="imagemagick")
