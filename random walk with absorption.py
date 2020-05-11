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

"""
#water data
absorb_xsec = 2.225
scatter_xsec = 344.741 
lmda = 1/(absorb_xsec + scatter_xsec)
"""
"""
#lead data
absorb_xsec = 0.521
scatter_xsec = 37.0067 
lmda = 1/(absorb_xsec + scatter_xsec)

"""
#graphite data
absorb_xsec = 0.0377
scatter_xsec = 39.6738
lmda = 1/(absorb_xsec + scatter_xsec)

abs_check = absorb_xsec / (absorb_xsec + scatter_xsec)

nneutrons = 100000


x = np.array([0])
y = np.array([0])
z = np.array([0])
transmitted = 0
absorbed = 0
reflected = 0
abs_total = np.array([])
ref_total = np.array([])
trans_total = np.array([])

length = 0.1

for j in range(10):
    #length += 0.1   
    """
    fig = plt.figure()
    plt.title("randssp")
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    """
    transmitted = 0
    absorbed = 0
    reflected = 0

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
                
        #ax.plot(x, y, z)
    abs_total = np.append(abs_total, absorbed)
    ref_total = np.append(ref_total, reflected)
    trans_total = np.append(trans_total, transmitted)



abs_mean = np.sum(abs_total)/len(abs_total)
ref_mean = np.sum(ref_total)/len(ref_total)
trans_mean = np.sum(trans_mean)/len(trans_mean)


abs_std = np.std(abs_total)
trans_std = np.std(trans_total)
ref_std = np.std(ref_total)


#plt.show()
    