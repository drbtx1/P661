# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:53:11 2025

@author: dabuch
"""
import numpy as np
#import random
lenA = 2
lenB = 2

psiA = np.empty([lenA,1]).astype(complex)
psiB = np.empty([lenB,1]).astype(complex)


#populate with random integers
sqtermsA = 0
for element in range(len(psiA)):
    value = np.random.randint(-10,10)
    imag = np.random.randint(-10,10)
    psiA[element] = value + imag*1j
    sqtermsA += (value**2 + imag*np.conj(imag))
#normalize   
psiA = psiA/np.sqrt(sqtermsA)    
    
sqtermsB = 0
for element in range(len(psiB)):
    value = np.random.randint(-10,10)
    imag = np.random.randint(-10,10)
    psiB[element] = value + imag*1j
    sqtermsB += (value**2 + imag*np.conj(imag))
psiB = psiB/np.sqrt(sqtermsB)

rhoA = psiA@(np.conj(psiA.T))  
rhoB = psiB@(np.conj(psiB.T))      

print(psiA)    
print(rhoA)
print(psiB)    
print(rhoB)
M = np.kron(rhoA,rhoB)
print(M)
psi = np.kron(psiA,psiB)
#print(psi@np.conj(psi.T))

def partialtraceA(M,a,b):
    reduced = np.empty((a,a)).astype(complex)
    for i in range(a):
        for j in range(a):
            sum = 0
            for counter in range(b):
                sum += M[b*i + counter][b*j + counter]
            reduced[i][j] = sum
    return reduced

print("reduced density matrix A:\n" + str(partialtraceA(M,lenA,lenB)))  

def partialtraceB(M,a,b):
    reduced = np.empty((b,b)).astype(complex)
    for i in range(b):
        for j in range(b):
            sum = 0
            for k in range(a):
                sum += M[i + b*k][j + b*k]
                reduced[i][j] = sum   
            
    return reduced   
print("reduced density matrix B:\n" + str(partialtraceB(M,lenA,lenB))) 
    
    
    