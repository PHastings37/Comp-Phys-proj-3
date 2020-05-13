# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:56:25 2020

@author: Patrick

The below code is for calculating the attenuation length in water given there 
is no scattering affects
"""

import numpy  as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#generates a random distribution of numbers according to the exp distribution
x = np.random.uniform(0, 1, size =1000000)
lmda = 0.45
y = -lmda * np.log(x)
    
#seperates the distribution above into 1000 bins and plots it on a histogram
num_bins = 1000
fig = plt.figure()
plt.hist(y, num_bins, facecolor='blue', alpha=0.5)
plt.show()
[n, xs] = np.histogram(y, num_bins)
xs = xs[:-1]

#removes the zeros from the histogram data
ni = np.array([])
xi = np.array([])
for i in range(len(n)):
    if n[i] != 0:
        ni = np.append(ni, n[i])
        xi = np.append(xi, xs[i])

#calculates the error in the number of neutrons
err_n = np.sqrt(ni * (1 - ni/len(x)))
err_logn = (err_n / ni)

#uses polyfit to obtain the slope and error
fit, cov = np.polyfit(xi, np.log(ni), deg=1, w=1/err_logn, cov=True)
blank1, residuals, blank2, blank3, blank4 = np.polyfit(xi, np.log(ni), deg=1, full=True, w=1/err_logn)
err_grad = np.sqrt(cov[0,0])
err_mfp = np.absolute(-1/(fit[0])**2) * err_grad

#plots the scatter of the log of the number of neutrons against bin depth
xt = np.linspace(0, 4.2, 20)
plt.figure()
plt.errorbar(xi, np.log(ni), yerr=err_logn, linestyle='None')
plt.plot(xt, fit[0] * xt + fit[1], color='r')
plt.scatter(xi, np.log(ni), marker='x')
plt.show()

print("mfp is ",-1/fit[0],"+-",err_mfp)
print(residuals/(len(xi) -2))