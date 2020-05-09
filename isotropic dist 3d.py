# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:44:02 2020

@author: Patrick
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


npoints = 1000

lmda = 6 #mean free path


#initialise x and y
x = np.array([])
y = np.array([])
z = np.array([])





for i in range(npoints + 1):
    theta = np.pi * np.random.uniform(0, 1, size=1)
    phi = 2 * np.pi * np.random.uniform(0, 1, size=1)
    #r= -lmda * np.log(np.random.uniform(0,1,size=1))
    r = 1   
    
    x = np.append(x, r * np.sin(theta) * np.cos(phi))
    y = np.append(y, r * np.sin(theta) * np.sin(phi))
    z = np.append(z, r * np.cos(theta))
    

    


fig = plt.figure()
plt.title("randssp")
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()