# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:56:25 2020

@author: Patrick
"""

import numpy  as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.random.uniform(0, 1, size =5000)

y = -np.log(x)
    
num_bins = 40
fig = plt.figure()
n, bins, patches = plt.hist(y, num_bins, facecolor='blue', alpha=0.5)
plt.show()

fit = np.polyfit(x, np.log(y), deg=1, cov=False)
plt.figure()
plt.scatter(x, fit[0] * x + fit[1])
plt.show()