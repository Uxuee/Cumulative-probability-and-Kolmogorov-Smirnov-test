# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:54:07 2019

@author: Ariadna
"""

from scipy import stats


def databox(u):
    D=stats.ks_2samp(u[0], u[1])
    E=stats.ks_2samp(u[0], u[2])
    F=stats.ks_2samp(u[1], u[2])
    
    print("D12= "+str(D[0])+" , p12="+str(D[1]))
    print("D13= "+str(E[0])+" , p13="+str(E[1]))
    print("D23= "+str(F[0])+" , p23="+str(F[1]))

    return D,E,F    
 
