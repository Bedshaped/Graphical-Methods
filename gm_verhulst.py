# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:07:43 2018

@author: moreaua2
"""

import numpy as np
from matplotlib import pyplot as plt 

def func(x, r, K):
   return r*x*(1 - x / K)

plt.close('all')

r = 0.5
K = 3

coeff = [-r/K, r, 0]

x = np.linspace(-2, K+1, 100)
dxdt = func(x, r, K)

x1, y1 = np.full(2, np.roots(coeff)[0]), [np.min(dxdt), np.max(dxdt)]
x2, y2 = np.full(2, np.roots(coeff)[1]), [np.min(dxdt), np.max(dxdt)]

plt.plot(x, func(x, r, K), label = r"$\dot{x}$ vs. x")
plt.plot(x1, y1, linestyle = '--', label = "Stable @ $x =%d$" % np.roots(coeff)[0])
plt.plot(x2, y2, linestyle = '--', label = "Unstable @ $x =%d$" % np.roots(coeff)[1])

plt.xlabel("x")
plt.ylabel(r"$\dot{x}$")
plt.grid()
plt.legend()