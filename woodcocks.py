# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:35:19 2020

@author: Patrick

Woodcocks Method
"""

import numpy as np

nneutrons = 100000


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
    return(lmda, abs_check, "water", Sig_total)


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
    return(lmda, abs_check, "lead", Sig_total)

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
    return(lmda, abs_check, "graphite", Sig_total)
    
def random_direction(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    vec = np.reshape(vec, 3)
    return vec

def absorbed_check(prob):
    u = np.random.uniform(0, 1, size = 1)
    if u < prob:
        return(True)
    else:
        return(False)

lmda = 0
abs_check = 0
lmda, abs_check, material, Sig_total = water()
lmda2, abs_check2, material2, Sig_total2 = graphite()

maj_xsec = max(Sig_total, Sig_total2)

trans_tot = 0
abs_tot = 0
ref_tot = 0



for j in range(nneutrons):
     origin = np.array([0, 0, 0]) 
     position = np.array([0, 0, 0])
     direction = np.array([1, 0, 0])
         
     absorbed, transmitted, reflected = [False]*3
     
     while not absorbed and not transmitted and not reflected:
        if maj_xsec == Sig_total:
            r = -lmda * np.log(np.random.uniform())
        else:
            r = -lmda2 * np.log(np.random.uniform())
            
        if position[0] < 0.1:
             x_sec = Sig_total
        else:
             x_sec = Sig_total2
             
        fict_prob = 1 - (x_sec / maj_xsec)
        
        if np.random.uniform() > fict_prob:
            fict_step = False
        else:
            fict_step = True
            
            
        if fict_step or (origin == position).all():
            step_size = r 
            step = step_size * direction
            position = position + step
            
        else:
            step = r* random_direction(1)
            position = position + step        
            direction = step / np.linalg.norm(step)
            
            if x_sec == Sig_total:
                absorbed = absorbed_check(abs_check)
            else:
                absorbed = absorbed_check(abs_check2)
                
            if absorbed == True:
                abs_tot += 1
            
        if position[0] > 0.2:
            trans_tot += 1
            transmitted = True
        elif position[0 ] < 0:
            ref_tot += 1
            reflected = True
            
            
            
trans_percent = (trans_tot / nneutrons)

trans_err = np.sqrt(nneutrons * trans_percent*(1 - trans_percent))

trans_per_err = trans_err / nneutrons

print(trans_percent,"pm",trans_per_err)





                

















