# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:07:35 2020

@author: Patrick
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.constants as sp

def random_direction(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    
    return vec


#water data
def water():
    sig_a = 0.6652 * 10**(-28)
    sig_s = 103 * 10**(-28)
    ro = 1000
    mol_mass = 18.02 * 1.661*10**(-27)
    n_den = ro/mol_mass
    Sig_a = n_den * sig_a
    Sig_s = n_den * sig_s
    Sig_total = n_den * (sig_a + sig_s)
    lmda = 1/Sig_total
    abs_check = Sig_a / (Sig_a + Sig_s)
    return(lmda, abs_check)


#lead data
def lead():
    sig_a = 0.158 * 10**(-28)
    sig_s = 11.221 * 10**(-28)
    ro = 11350
    mol_mass = 207.2 * 1.661*10**(-27)
    n_den = ro/mol_mass
    Sig_a = n_den * sig_a
    Sig_s = n_den * sig_s
    Sig_total = n_den * (sig_a + sig_s)
    lmda = 1/Sig_total
    abs_check = Sig_a / (Sig_a + Sig_s)
    return(lmda, abs_check)

#graphite data
def graphite():
    sig_a = 0.0045 * 10**(-28)
    sig_s = 4.74 * 10**(-28)
    ro = 1670
    mol_mass = 12 * 1.661*10**(-27)
    n_den = ro/mol_mass
    Sig_a = n_den * sig_a
    Sig_s = n_den * sig_s
    Sig_total = n_den * (sig_a + sig_s)
    lmda = 1/Sig_total
    abs_check = Sig_a / (Sig_a + Sig_s)
    return(lmda, abs_check)
    
nneutrons = 10000


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
lmda, abs_check = water()

for j in range(1):
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
        
        
        r = -lmda * np.log(np.random.uniform(0, 1, 1))
        xi = r
        yi = 0
        zi = 0
        xi = np.absolute(xi)
        
        x = np.append(x, xi)
        y = np.append(y, yi)
        z = np.append(z, zi)
        while finished== 0:
            xi, yi, zi = random_direction(1)
            r = -lmda * np.log(np.random.uniform(0, 1, 1))
            xi *= r
            yi *= r
            zi *= r
            
            x = np.append(x, x[len(x) -1] + xi)
            y = np.append(y, y[len(y) -1] + yi)
            z = np.append(z, z[len(z) -1] + zi)
            
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
trans_mean = np.sum(trans_total)/len(trans_total)


abs_std = np.std(abs_total)
trans_std = np.std(trans_total)
ref_std = np.std(ref_total)

print("percent reflected" , (ref_mean / nneutrons) * 100 , " +- " , (ref_std / nneutrons) * 100)
print("percent transmitted" , (trans_mean / nneutrons) * 100, " +- " , (trans_std / nneutrons) * 100)
print("percent absorbed" , (abs_mean / nneutrons) * 100 , " +- " , (abs_std / nneutrons) * 100)


#plt.show()
    