# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:31:04 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt


plt.close('all')

# Parameters

n = 101
omega_0 = 1.1
b = 0.1

coords = np.linspace(-5, 5, n)
X,Y = np.meshgrid(coords[::5], coords[::5])


U = Y
V = -b*Y-(omega_0**2)*X


textstr = '\n'.join((
    r'$b=%.2f$' % (b, ),
    r'$\omega_0=%.2f$' % (omega_0, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

fig1, ax0 = plt.subplots()
ax0.quiver(X, Y, U, V)

seed_points = np.array([[-3], [2]])
ax0.streamplot(X, Y, U, V, color='b', 
               integration_direction='forward',
               start_points=seed_points.T)

plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
ax = plt.gca()
ax.text(0.05, 0.25, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.savefig("gm_dho.png", dpi=300)