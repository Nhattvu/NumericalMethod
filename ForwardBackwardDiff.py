#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt

#generate x values in [0, 2pi]. step size h

h = 0.1
x = np.arange(0, 2*np.pi+h, h)
f = np.sin(x)
n = len(x)

#compute derivative
#fwd diff
diffArr = np.diff(f)

backDiff = (f[n - 1] - f[n - 2])
fprime = np.append(diffArr, backDiff)
fprime = fprime/h


plt.plot(x,f)
plt.plot(x,fprime)
plt.grid()
plt.show()


# In[ ]:




