# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:07:43 2018

@author: moreaua2
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

def func(t, y, params):
    r, K = params
    return r*y*(1 - y / K)

plt.close('all')

# Parameters

r = 0.5
K = 3
t_0 = -2
t_max = K+1
n = 100

# Initial values

x0 = [-0.25, 0.25, 1, 2, 2.5, 3.5, 5]

# Calculating the fixed points

coeff = [-r/K, r, 0]

x = np.linspace(t_0, t_max, n)
dxdt = func(0, x, [r, K])

x1, y1 = np.full(2, np.roots(coeff)[0]), [np.min(dxdt), np.max(dxdt)]
x2, y2 = np.full(2, np.roots(coeff)[1]), [np.min(dxdt), np.max(dxdt)]

# Plotting fixed point equation

plt.figure(1, figsize=(9, 6))
plt.plot(x, dxdt, label = r"$\dot{x}$ vs. x")
plt.plot(x1, y1, linestyle = '--', label = "Stable @ $x =%d$" % np.roots(coeff)[0])
plt.plot(x2, y2, linestyle = '--', label = "Unstable @ $x =%d$" % np.roots(coeff)[1])
plt.xlabel("x")
plt.ylabel(r"$\dot{x}$")
plt.grid()
plt.legend()

# RK45 solution iterated for many x0

for i in range(len(x0)):
    y0 = [x0[i]]
    res = solve_ivp(lambda t, y : func(t, y, [r, K]),
                   [t_0, t_max*3],
                   y0,
                   method="RK45",
                   t_eval=np.linspace(t_0, t_max*3, n))
    
    x_rk = res.y[0]
    t_rk = res.t
    
    
    # Plotting iterated IVP solution
    
    plt.figure(2, figsize=(9, 6))
    plt.plot(t_rk, x_rk, label = r"x @ $x_0 = %5.2f$" % y0[0])
plt.xlabel("t")
plt.ylabel("x")
plt.ylim(-5, max(x0))
plt.grid()
plt.legend()

