# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:01:31 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def coupled(t, val, params):
    a, b, c, d = params
    return np.array([U(t, val, [a, b]), V(t, val, [c, d])])

def U(t, val, params):
    a, b = params
    x, y = val
    return a*x - b*x*y

def V(t, val, params):
    c, d = params
    x, y = val
    return c*x*y - d*y

plt.close('all')

# Parameters

a, b, c, d = [4, 2, 3, 1]
t_0 = 0
t_max = 100
n = 100

# Constructing grids

X, Y = np.meshgrid(np.arange(-1, 4, 0.1), np.arange(-1, 4, 0.1))

# Finding isoclines

xiso = a/b
yiso = d/c
yiso_x1, yiso_y1 = np.full(2, yiso), [-0.5, 4]
yiso_x2, yiso_y2 = [-0.5, 4], [0, 0]
xiso_x1, xiso_y1 = [0, 0], [-0.5, 4]
xiso_x2, xiso_y2 = [-0.5, 4], np.full(2, xiso)

# Solving using RK45

res = solve_ivp(lambda t, val : coupled(t, val, [a, b, c, d]),
                [t_0, t_max],
                y0 = [a, b],
                method="RK45",
                t_eval=np.linspace(t_0, t_max, n))

x = res.y[0]
v = res.y[1]
t = res.t
    

# Plotting the quiver/stream/isoclines

plt.figure(1, figsize=(9, 6))
plt.quiver(X, Y, U(0, [X, Y], [a, b]), V(0, [X, Y], [c, d]), pivot='mid')
plt.streamplot(X, Y, U(0, [X, Y], [a, b]), V(0, [X, Y], [c, d]))
plt.xlabel("Rabbits (x)")
plt.ylabel("Foxes (y)")
plt.xlim(-0.5, yiso*3)
plt.ylim(-0.5, xiso*2)

plt.plot(yiso_x1, yiso_y1, color='b', linewidth = 3, label = "y-isocline")
plt.plot(yiso_x2, yiso_y2, color='b', linewidth = 3)
plt.plot(xiso_x1, xiso_y1, color='r', linewidth = 3, label = "x-isocline")
plt.plot(xiso_x2, xiso_y2, color='r', linewidth = 3)
plt.legend()

# Plotting our integral solution from RK45

plt.figure(2, figsize=(9, 6))
plt.plot(t, x)
plt.plot(t, v)