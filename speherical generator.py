# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:24:04 2020

@author: Patrick

generates a sphere with bias towards the poles
"""


import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d


"""
effectively the program selects a latitude and then picks a point around the 
circumference of that latitude, so at the poles when the circumference is smaller
there is still the same number of points so they 'bunch up' and are spread over a 
smaller area.
"""
pi = np.pi
phi = np.random.uniform(0, 2 * pi, size=1000)
theta = np.random.uniform(0, pi, size=1000)
#r = np.random.uniform(0, 1, size=1000)
r=1

x = r * np.sin( theta) * np.cos( phi )
y = r * np.sin( theta) * np.sin( phi )
z = r * np.cos( theta )


phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 40)
x_outer = np.outer(np.sin(theta), np.cos(phi))
y_outer = np.outer(np.sin(theta), np.sin(phi))
z_outer = np.outer(np.cos(theta), np.ones_like(phi))

fig = plt.figure()
plt.title("randssp")
ax = fig.add_subplot(111, projection='3d')
#ax.plot_wireframe(x_outer, y_outer, z_outer, color='k', rstride=1, cstride=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter(x, y, z)
plt.show()