#!/usr/bin/env python
# coding: utf-8

# In[4]:


from scipy.integrate import trapz
import numpy as np


a = 0
b = 1
n = 8
x = np.linspace(a, b, n+1)
print(x)
y = np.cos(x**2)
trapz(y, x)


# In[ ]:




