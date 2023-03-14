#!/usr/bin/env python
# coding: utf-8

# In[51]:


import matplotlib.pyplot as plt

#function to approximate differences
def difference(x,y):
    yprime=[]
    for i in range(1):
        #forward difference formula
        yprime.append((y[1]-y[0])/(x[1]-x[0]))
    for i in range(1, n -1):
        #central difference formula
        yprime.append((y[i+1]-y[i-1])/(x[i+1]-x[i-1]))
    for i in range(n-1,n):
        #backward difference formula
        yprime.append((y[i]-y[i-1])/(x[i]-x[i-1]))
    return yprime
           
n = len(x)    
x = [805, 825, 845, 865, 885, 905, 925, 945, 965, 985]
y = [0.710, 0.763, 0.907, 1.336, 2.169, 1.598, 0.916, 0.672, 0.615, 0.606]

#compute the y'
derivative = difference(x,y)
print(derivative)
#plot 
plt.plot(x[0:n], derivative)
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




