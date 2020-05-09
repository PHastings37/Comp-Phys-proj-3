# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:40:57 2020

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randssp(p,q):
    
    global m, a, c, x
        
    try: x
    except NameError:
        m = pow(2, 31)
        a = pow(2, 16) + 3
        c = 0
        x = 123456789
    
    try: p
    except NameError:
        p = 1
    try: q
    except NameError:
        q = p
    
    r = np.zeros([p,q])

    for l in range (0, q):
        for k in range (0, p):
            x = np.mod(a*x + c, m)
            r[k, l] = x/m
    return r




r = randssp(3,5000)

rand = np.random.uniform(0, 1, size=(3, 5000))

x = np.random.uniform(0, 1, size = 1000)
np.sort(x) 
lmda = 0.45
y = -lmda * np.log(x/lmda)
    
num_bins = 100
fig = plt.figure()
n, bins, patches = plt.hist(y, num_bins, facecolor='blue', alpha=0.5)
plt.show()

xs = np.polyfit(np.log(x), y, deg = 1, cov = False)


fig = plt.figure()
plt.title("randssp")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r[0], r[1], r[2])
plt.show()

fig = plt.figure()
plt.title("rand.uniform")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(rand[0], rand[1], rand[2])
plt.show()