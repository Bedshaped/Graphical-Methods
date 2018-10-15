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
omega_0 = 0.9
b = 0.1

coords = np.linspace(-5, 5, n)
X,Y = np.meshgrid(coords[::5], coords[::5])


U = Y
V = -b*Y-(omega_0**2)*X


fig1, ax0 = plt.subplots()
ax0.quiver(X, Y, U, V)

seed_points = np.array([[-3], [2]])
ax0.streamplot(X, Y, U, V, color='b', 
               integration_direction='forward',
               start_points=seed_points.T)

plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')