# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:17:40 2020

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt


nsteps = 10
#starting x and y pos



x = np.array([1])
y = np.array([1])
x[0] = 0
y[0] = 0


for i in range(nsteps):
    theta = 2* np.pi*np.random.uniform(0, 1, size=1)
    r = 1
    
    dx = r*np.cos(theta)
    dy = r*np.sin(theta)
    
    x = np.append(x, x[i] + dx)
    y = np.append(y, y[i] + dy)
    


plt.figure()
plt.plot(x, y)
plt.show()