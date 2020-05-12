# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:34:13 2020

@author: Patrick
"""

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
    return(lmda, abs_check, "water")


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
    return(lmda, abs_check, "lead")

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
    return(lmda, abs_check, "graphite")
    
def random_walk(finished, abs_check):
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
            result = 0
         elif x[len(x) - 1] > length:
            finished = 1
            result = 1
         elif x[len(x) - 1] < 0:
            finished = 1
            result = 2
            
            
     return(result)

nneutrons = 1000

for i in range(1):
    
    lmda = 0
    abs_check = 0
    length = 0
    ref_percent = np.array([])
    abs_percent = np.array([])
    trans_percent = np.array([])
    abs_tot = np.array([])
    ref_tot = np.array([])
    trans_tot = np.array([])
    transi_tot = np.array([])
    transi_err = np.array([])

    
    if i == 0:
        lmda, abs_check, material = water()
    elif i == 1:
        lmda, abs_check, material = lead()
    else:
        lmda, abs_check, material = graphite()
    print(material)
    for k in range(30):
        length += 0.01
        abs_total = np.array([])
        ref_total = np.array([])
        trans_total = np.array([])
        
        transmitted = 0
        absorbed = 0
        reflected = 0
        
        for i in range(nneutrons):
                
            result = random_walk(0, abs_check)
            if result == 0:
                absorbed += 1
            elif result == 1:
                transmitted += 1
            else:
                reflected += 1                           
        
        ref_percent = np.append(ref_percent, (reflected/nneutrons))
        abs_percent = np.append(abs_percent, (absorbed/nneutrons))
        trans_percent = np.append(trans_percent, (transmitted/nneutrons))
        
        ref_tot = np.append(ref_tot, reflected)
        abs_tot = np.append(abs_tot, absorbed)
        trans_tot = np.append(trans_tot, transmitted)
        
        ref_err = np.sqrt(nneutrons * ref_percent * (1 - ref_percent))
        abs_err = np.sqrt(nneutrons * abs_percent * (1 - abs_percent))
        trans_err = np.sqrt(nneutrons * trans_percent * (1 - trans_percent))
        length_array = np.linspace(0.01, 0.3, 30)
        tran_len = np.array([])
        trans_log_err = np.array([])
        
        
        
    for i in range(len(trans_tot)):
       if trans_tot[i] != 0:
           transi_tot = np.append(transi_tot, trans_tot[i])
           tran_len = np.append(tran_len, length_array[i]) 
           transi_err = np.append(transi_err, trans_err[i])
           
           
           
   
    trans_log = np.log(transi_tot)
    for i in range(len(transi_tot)):#
        if transi_tot[i] == 1:
            trans_log_err = np.append(trans_log_err, transi_err[i])
            #look at y = ln(x) for cas x =1
        else:
            trans_log_err = np.append(trans_log_err, (transi_err[i]/transi_tot[i]) * trans_log[i])
    
    #print("percent reflected" , ref_percent , " +- " , ref_err)
    #print("percent transmitted" , abs_percent, " +- " , abs_err)
    #print("percent absorbed" , trans_percent, " +- " , trans_err)
    
    fig = plt.figure()
    plt.title("raw")
    plt.scatter(length_array, abs_tot, color='b', label='abs')
    plt.errorbar(length_array, abs_tot, yerr=abs_err, color='b', linestyle='None')
    plt.legend()
    plt.show()   
    
    fig = plt.figure()
    plt.title(material)
    plt.scatter(length_array, trans_tot, color='g', label='trans')
    plt.errorbar(length_array, trans_tot, yerr=trans_err , color='g', linestyle='None')
    plt.legend()
    plt.show()
    
    fig = plt.figure()
    plt.title(material)
    plt.scatter(length_array, ref_tot, color='r', label='ref')
    plt.errorbar(length_array, ref_tot, yerr=ref_err, color='r', linestyle='None')
    plt.legend()
    plt.show()
    
    fit, cov = np.polyfit(tran_len, trans_log, deg=1, w=1/trans_log_err, cov=True)
    err_grad = np.sqrt(1/cov[0,0])
    
    print("Attenuation length for ",material,"is",-1/fit[0],"+-",err_grad)
    
    
    xt = np.linspace(0.01, 0.3, 30)
    fig = plt.figure()
    plt.title(material)
    plt.scatter(tran_len, trans_log, color='g', label='trans')
    plt.plot(xt, fit[0] * xt + fit[1])
    plt.errorbar(tran_len, trans_log, yerr=trans_log_err, color='g', linestyle='None')
    plt.legend()
    plt.show() 
    
    
   
    
    
    
    
 