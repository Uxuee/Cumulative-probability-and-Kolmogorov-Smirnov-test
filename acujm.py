# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:23:56 2019

@author: Ariadna
"""


def acumulative(Y):

    u=1 
    for i in Y:
        if len(Y)>u:
            Y[u]+=i
            u+=1
    return Y