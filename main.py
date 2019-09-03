# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:28:14 2019

@author: Ariadna
"""
from acujm import acumulative
import os
import matplotlib.pyplot as plt
import numpy as np
#from norm import norma
from data import databox
fig = plt.figure()
ax = fig.add_subplot(111)



path = 'C:/Users/Ariadna/Desktop/paper/1'
i=0

colors=['b','g','r']

all=[]

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        
        if '.npy' in file:
            array=np.load(file)
#            print(file)
            X = array[:,0]

            Y = array[:,1]
            
#            V =            norma(Y)
            
#            all.append(W)

             
            W=acumulative(Y) #V
            plt.plot(X,Y,colors[i])
            i+=1
        
            
#            print(X)
#            print(Y)
            
#            plt.ylim(0, 1)
            plt.xlim(0, 2200)
            all.append(W)
            
O,P,Q=databox(all)

#A="D12= "+str(round(O[0],2))+"\np12= "+str(round(O[1]))
A="D12= "+"{:.2e}".format(O[0])+"\np12= "+"{:.2e}".format(O[1])
B ='D23= '+"{:.2e}".format(P[0])+'\np23= '+"{:.2e}".format(P[1])
C ='D13= '+"{:.2e}".format(Q[0])+'\np13= '+"{:.2e}".format(Q[1])

M=A+"\n"+B+"\n"+C

E="90Sr (1)"

D="Muon background (3)"

F="137Cs (2)\n\n"+M

plt.legend((E,D,F),
           shadow=False, loc=(0.7, 0.1), handlelength=1.5, fontsize=10)
ax.set_xlabel('Generated Optical Photons')
ax.set_ylabel('Cumulative probability')

            
plt.show()
