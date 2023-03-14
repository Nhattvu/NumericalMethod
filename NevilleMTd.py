#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np #numerical python

def neville(x, y, xr):
    #Function for neville's method
    #initialize 
    n = len(x)
    Q = np.zeros([n,n]) #pass single arg of list
    Q[:,0] = y #first col, all rows = y values
    for i in range(1,n):
        for j in range(1,i+1):
            Q[i,j] = ((xr - x[i-j]) * Q[i,j-1] - (xr - x[i]) * Q[i-1, j-1]) / (x[i] - x[i-j]) 
            
        
    print(Q)
    return Q

xr = 8.4
x = [8.1, 8.3, 8.6, 8.7]
y = [16.9, 17.6, 18.5, 18.8]
Q = neville(x, y, xr)


# In[ ]:





# In[ ]:




