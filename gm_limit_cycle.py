# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:36:41 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def coupled(t, y):
    x, v = y
    dxdt = v
    dvdt = -x + v*(1 - x**2)
    dydt = np.array([dxdt, dvdt])
    return dydt

plt.close('all')

# Parameters
    
t_0 = 0
t_max = 30
n = 500

# Initial values

params = [0.1, 1] # b, omega_0
y_0 = [-2, 2]

# Constructing grids

x_size, y_size = [0, t_max]
X, Y = np.meshgrid(np.arange(x_size, y_size, 0.1), np.arange(x_size, y_size, 0.1))




res = solve_ivp(lambda t, y : coupled(t, y), 
                [t_0, t_max], 
                y_0, 
                method="RK45", 
                t_eval=np.linspace(t_0, t_max, n))

x = res.y[0]
v = res.y[1]
t = res.t

plt.figure(1, figsize=(9, 6))
plt.quiver(X, Y, coupled(0, [X, Y])[0], coupled(0, [X, Y])[1], pivot='mid')
plt.streamplot(X, Y, coupled(0, [X, Y])[0], coupled(0, [X, Y])[1])

plt.figure(2, figsize=(9, 6))
plt.plot(t, x, label=r"$x , x_0 = %d$" % y_0[0])
plt.plot(t, v, label=r"$v , v_0 = %d$" % y_0[1])
plt.xlabel("Time")
plt.legend()

plt.figure(3, figsize=(9, 6))
plt.plot(x, v, 'k')
plt.axis('equal')
plt.xlabel(r"$x$")
plt.ylabel(r"$v$")