#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np

def jacobi(A,b,x):
    maxIt = 1000
    n = len(b)
    tol = 10**(-2)
    Dinv = np.zeros((n,n))
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j: #on diagonal
                Dinv[i,j] = 1/A[i,j]
            elif i < j: #upper triangle
                L[i,j] = -A[i,j]
            elif i > j: #lower triangle
                U[i,j] = -A[i,j]
    T = np.matmul(Dinv,L+U)
    c = np.matmul(Dinv,b)
    
    for i in range(maxIt):
        xnew = np.matmul(T,x) + c 
        err = max(abs(xnew - x))
        if err <= tol:
            print('[F1 F2 F3 f1 f2 f3 f4 f5] = ', xnew, 'after ', i+1, 'iteration')
            return xnew
        elif i == maxIt - 1:
            print('System did not converge')
            return []
        else:
            x = xnew
    print(xnew)

A = np.array(([-1,0,0,np.sqrt(2)/2,1,0,0,0],[0,-1,0,np.sqrt(2)/2,0,0,0,0],[0,0,-1,0,0,0,0.5,0],[0,0,0,-np.sqrt(2)/2,0,-1,-1/2,0],[0,0,0,0,-1,0,0,1],[0,0,0,0,0,1,0,0],[0,0,0,-np.sqrt(2)/2,0,0,np.sqrt(3)/2,0],[0,0,0,0,0,0,-np.sqrt(3)/2,-1]))
b = np.array([0,0,0,0,0,10000,0,0])
n = len(b)
x = np.array([1,1,1,1,1,1,1,1])
soln = jacobi(A,b,x)


# In[ ]:





# In[ ]:




