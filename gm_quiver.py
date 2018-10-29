# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:36:07 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))

V_x = np.cos(X)*Y
V_y = np.sin(X)*X

fig1, ax1 = plt.subplots()
Q = ax1.quiver(X[::3, ::3], Y[::3, ::3], V_x[::3, ::3], V_y[::3, ::3], pivot='mid')
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("gm_quiver.png", dpi=300)