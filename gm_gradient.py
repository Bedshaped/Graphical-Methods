# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:55:13 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

coords = np.linspace(0, 2*np.pi, 101)

X, Y = np.meshgrid(coords[::5], coords[::5]) # coarse grid, every 5th point used

V_x = np.cos(X)*Y
V_y = np.sin(X)*X
Z = np.sqrt(V_x**2 + V_y**2)

x, y = np.meshgrid(coords, coords) # fine grid, every point used
v_x = np.cos(x)*y
v_y = np.sin(x)*x
z = np.sqrt(v_x**2 + v_y**2)

ds = coords[5]-coords[0] # coarse grid spacing
dX, dY = np.gradient(Z, ds) # Calculate the gradient on the coarse grid

plt.contourf(x,y,z) #plot a contour map using the fine grid
plt.set_cmap('coolwarm') # change color of map
plt.quiver(X,Y,dX,dY) # plot the gradient using the coarse grid.
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("gm_gradient.png", dpi=300)