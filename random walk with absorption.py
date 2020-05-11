# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:07:35 2020

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def random_direction(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    
    return vec


absorb_xsec = 1.343704
scatter_xsec = 208.06 #power of 10^52 ignored for readability
abs_check = absorb_xsec / (absorb_xsec + scatter_xsec)

nneutrons = 100

lmda = 1
x = np.array([0])
y = np.array([0])
z = np.array([0])
transmitted = 0
absorbed = 0
reflected = 0

length = 0

for j in range(300):
    length += 0.1    
    for i in range(nneutrons):
        
        finished = 0
        
        x = [0]
        y = [0]
        z = [0]
        
        xi, yi, zi = random_direction(1)
        r = -lmda * np.exp(np.random.uniform(0, 1, 1))
        xi *= r
        yi *= r
        zi *= r
        xi = np.absolute(xi)
        
        x = np.append(x, xi)
        y = np.append(y, yi)
        z = np.append(z, zi)
        while finished== 0:
            xi, yi, zi = random_direction(1)
            r = -lmda * np.exp(np.random.uniform(0, 1, 1))
            xi *= r
            yi *= r
            zi *= r
            
            x = np.append(x, x[len(x) -1] + xi)
            y = np.append(y, yi)
            z = np.append(z, zi)
            
            u = np.random.uniform(size=1)
            if u < abs_check:
                finished = 1
                absorbed +=1
            elif x[len(x) - 1] > length:
                finished = 1
                transmitted += 1
            elif x[len(x) - 1] < 0:
                finished = 1
                reflected += 1
                
        """
        fig = plt.figure()
        plt.title("randssp")
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot(x, y, z)
        """
        
    
plt.show()
    