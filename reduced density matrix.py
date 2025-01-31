# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:53:11 2025

@author: dabuch
"""
import numpy as np
#import random
lenA = 2
lenB = 4

psiA = np.zeros((lenA,1))
psiB = np.zeros((lenB,1))


#populate with random integers
sqtermsA = 0
for element in range(len(psiA)):
    value = np.random.randint(-10,10)
    psiA[element] = value
    sqtermsA += value**2
#normalize   
psiA = psiA/np.sqrt(sqtermsA)    
    
sqtermsB = 0
for element in range(len(psiB)):
    value = np.random.randint(-10,10)
    psiB[element] = value
    sqtermsB += value**2
psiB = psiB/np.sqrt(sqtermsB)

rhoA = psiA@(np.conj(psiA.T))  
rhoB = psiB@(np.conj(psiB.T))      

print(psiA)    
print(rhoA)
print(psiB)    
print(rhoB)
M = np.kron(rhoA,rhoB)
print(M)

def partialtraceA(M,a,b):
    reduced = np.zeros((a,a))
    for i in range(a):
        for j in range(a):
            sum = 0
            for counter in range(b):
                sum += M[b*i + counter][b*j + counter]
            reduced[i][j] = sum
    return reduced

print("reduced density matrix A:\n" + str(partialtraceA(M,lenA,lenB)))  

def partialtraceB(M,a,b):
    reduced = np.zeros((b,b))
    for i in range(b):
        for j in range(b):
            sum = 0
            for k in range(a):
                sum += M[i + b*k][j + b*k]
                reduced[i][j] = sum   
            
    return reduced   
print("reduced density matrix B:\n" + str(partialtraceB(M,lenA,lenB))) 
    
    
    