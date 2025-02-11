# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:18:45 2025

@author: dbtx
"""
import numpy as np
import scipy as sp

def SVD(M):
    Mct = np.conj(M.T)
    vals1, U = sp.linalg.eig(M@Mct)
    vals2, V = sp.linalg.eig(Mct@M)
    if len(vals1) < len(vals2):
        L = vals1
        height = len(vals1)
        length = len(vals2)
    else:
        L = vals2    
        height = len(vals2)
        length = len(vals1)
    D = np.zeros([height, length,]).astype(complex)
    for i in range(len(L)):
        D[i][i] = np.sqrt(L[i])
    return U, D, V     
M = np.array([[1/np.sqrt(6), 1j/np.sqrt(6),1/np.sqrt(3)], [1/np.sqrt(3),0,0]]).astype(complex)    
U, D, V = SVD(M)
print(U@D@np.conj(V.T))
'''print(np.conj(V.T))
print(D)
print(U)

print(U@D@(np.conj(V.T)))'''
print(M)
#print(D)
print(U)
print(V)

    

