# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:20:52 2019

@author: Ariadna
"""

from graf import grafi
from acujm import acumulative
import os

path = 'C:/Users/Ariadna/Desktop/paper/1'

files = {}

i=0

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.npy' in file:
            files[i]=os.path.join(r, file)
            i+=1
            
for u in range(i):
        U=acumulative(files[u])
        grafi(U)