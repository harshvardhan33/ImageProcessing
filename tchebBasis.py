# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:02:20 2020

@author: harshvardhan
"""

import numpy as np 
import math as mt
import pylab as p_
import matplotlib.cm as cm


N = 8
order = N-1
t_hat = np.zeros((N+1,N+1))

for x in range(0,(N//2)):
    t_hat[1][x+1] = 1/mt.sqrt(N)
    t_hat[2][x+1] = (2*x+1-N)*mt.sqrt(3/(N*(N**2-1)))
    for n in range(2):
        t_hat[n+1][N-x] = (-1)**n*t_hat[n+1][x+1]

for n in range(2,order+1):
    t_hat[n+1][1] = (-mt.sqrt(((N-n)*(2*n+1))/((N+n)*(2*n-1))))*(t_hat[n][1])
    t_hat[n+1][2] = (1+n*(1+n)/(1-N))*t_hat[n+1][1]
    for x in range(2):
        t_hat[n+1][N-x] = (-1)**n*t_hat[n+1][x+1]
    for x in range(2,N//2):
        y1 = (-n*(n+1)-(2*x-1)*(x-N-1)-x)/(x*(N-x))
        y2 = (x-1)*(x-N-1)/(x*(N-x))
        t_hat[n+1][x+1] = y1*t_hat[n+1][x]+y2*t_hat[n+1][x-1];
        t_hat[n+1][N-x] = (-1)**n*t_hat[n+1][x+1]
t_hat = np.delete(t_hat,0,0)
t_hat = np.delete(t_hat,0,1)

tp = t_hat.copy()
tq = t_hat.copy()

res=[]
for i in range(8):
    for j in range(8):
        row = tp[i,:].reshape(1,8)
        col = tq[j,:].reshape(1,8)
        res.append(np.dot(np.transpose(row),col))
    
        
p_.figure("DCT")
n = 8
for i in range(0, len(res)):
    p_.subplot(n, n, i+1)
    p_.axis('off')
    p_.imshow(res[i],cmap = cm.Greys_r)
p_.show()
    