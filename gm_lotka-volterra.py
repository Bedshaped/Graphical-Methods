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

a, b, c, d = [5, 3, 1, 6]
t_0 = 0
t_max = 10
n = 5000

# Constructing grids

x_size, y_size = [-1, 10]
X, Y = np.meshgrid(np.arange(x_size, y_size, 0.1), np.arange(x_size, y_size, 0.1))

# Finding isoclines

xiso = a/b
yiso = d/c
yiso_x1, yiso_y1 = np.full(2, yiso), [x_size, y_size]
yiso_x2, yiso_y2 = [x_size, y_size], [0, 0]
xiso_x1, xiso_y1 = [0, 0], [x_size, y_size]
xiso_x2, xiso_y2 = [x_size, y_size], np.full(2, xiso)

# Solving using RK45

res = solve_ivp(lambda t, val : coupled(t, val, [a, b, c, d]),
                [t_0, t_max],
                y0 = [a, b],
                method="RK45",
                rtol=1e-6,
                t_eval=np.linspace(t_0, t_max, n))

x = res.y[0]
v = res.y[1]
t = res.t
    

# Plotting the quiver/stream/isoclines

plt.figure(1, figsize=(9, 6))
plt.quiver(X[::5, ::5], Y[::5, ::5],
           U(0, [X, Y], [a, b])[::5, ::5], V(0, [X, Y], [c, d])[::5, ::5],
           scale=200,
           pivot='mid')
plt.streamplot(X, Y, U(0, [X, Y], [a, b]), V(0, [X, Y], [c, d]))
plt.xlabel("Rabbits (x)")
plt.ylabel("Foxes (y)")
plt.xlim(x_size, y_size)
plt.ylim(x_size, xiso*2)

plt.plot(yiso_x1, yiso_y1, color='b', linewidth = 3, label = "y-isocline")
plt.plot(yiso_x2, yiso_y2, color='b', linewidth = 3)
plt.plot(xiso_x1, xiso_y1, color='r', linewidth = 3, label = "x-isocline")
plt.plot(xiso_x2, xiso_y2, color='r', linewidth = 3)
plt.legend()
plt.savefig("gm_lv_isocline.png", dpi=300)

# Plotting our integral solution from RK45

textstr = '\n'.join((
    r'$a=%.2f$' % (a, ),
    r'$b=%.2f$' % (b, ),
    r'$c=%.2f$' % (c, ),
    r'$d=%.2f$' % (d, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

plt.figure(2, figsize=(9, 6))
plt.plot(t, x, label = "Rabbits")
plt.plot(t, v, label = "Foxes")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
ax = plt.gca()
ax.text(0.05, 0.25, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.savefig("gm_lv.png", dpi=300)

plt.figure(3, figsize=(9, 6))
plt.plot(x, v, 'k')
plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.savefig("gm_lv_phase.png", dpi=300)