# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:56:25 2020

@author: Patrick
"""

import numpy  as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.random.uniform(0, 1, size =5000)

lmda = 0.45
y = -lmda * np.log(x)
    
num_bins = 100
fig = plt.figure()
plt.hist(y, num_bins, facecolor='blue', alpha=0.5)
plt.show()

[n, xs] = np.histogram(y, num_bins)
xs = xs[:-1]



ni = np.array([])
xi = np.array([])

for i in range(len(n)):
    if n[i] != 0:
        ni = np.append(ni, n[i])
        xi = np.append(xi, xs[i])

err_n = np.sqrt(len(ni) * (1 - len(ni)/len(x))) / len(ni)
err_logn = err_n * np.log(ni)
fit = np.polyfit(xi, np.log(ni), deg=1, w=err_logn, cov=False)

plt.figure()
plt.errorbar(xi, np.log(ni), yerr=err_logn, linestyle='None')
plt.scatter(xi, np.log(ni), marker='x')
plt.show()

print(-1/fit[0])