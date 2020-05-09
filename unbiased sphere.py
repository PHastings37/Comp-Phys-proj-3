# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:54:10 2020

@author: Patrick
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    
    return vec

xi, yi, zi = sample_spherical(5000)
r = -np.log(np.random.uniform(0, 1, size=5000))
xi *= r
yi *= r
zi *= r


fig = plt.figure()
plt.title("randssp")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xi, yi, zi)
plt.show()