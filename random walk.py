# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:17:40 2020

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    
    return vec

nsteps = 1000

lmda = 6 #mean free path


#initialise x and y
x = np.array([])
y = np.array([])
z = np.array([])
    
x, y, z = sample_spherical(nsteps)
r = -np.log(np.random.uniform(0, 1, size=nsteps))
x *= r
y *= r
z *= r


fig = plt.figure()
plt.title("randssp")
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(x, y, z)
plt.show()