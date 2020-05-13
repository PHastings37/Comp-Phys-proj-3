# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:54:10 2020

@author: Patrick

Plots a sphere with no bias to the poles
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def sample_spherical(npoints, ndim=3): 
"""
generates a random vector with no bias towards poles and normalises it for a 
magnitude of 1. found at    https://stackoverflow.com/questions/33976911/
generate-a-random-sample-of-points-distributed-on-the-surface-of-a-unit-sphere
"""
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    
    return vec

xi, yi, zi = sample_spherical(1000)
r = -np.log(np.random.uniform(0, 1, size=1000))# generates an isotropic dist 
#logarithmically
#r = #used for a unit sphere
xi *= r
yi *= r
zi *= r


fig = plt.figure()
plt.title("randssp")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xi, yi, zi)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()