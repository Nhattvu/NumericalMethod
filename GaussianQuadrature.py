#!/usr/bin/env python
# coding: utf-8

# In[18]:


def gauss_points(n):
    if n == 2:
        c = [1,1]
        r = [0.5773502692, -0.5773502692]
        return (c,r)
    if n == 3:
        c = [0.555555556, 0.888888888, 0.555555556]
        r = [0.7745966692, 0, -0.7745966692]
        return (c,r)
    #add branches for n=4,5
    if n == 4:
        c = [0.34785485, 0.652145155, 0.652145155, 0.347854845]
        r = [0.8611363116, 0.3399810436, -0.3399810436, -0.8611363116]
        return (c,r)
    if n == 5:
        c = [0.2369278850, 0.4786286705, 0.5688888889, 0.4786286705, 0.236926885]
        r = [0.9061798459, 0.5384693101, 0, -0.5384693101, -0.9061798459]
        return (c,r)
    else:
        print('Value not supported.')
        
def f(x):
    #define function to be integrated on [a,b]
    return x**2
    
n = 5 

#define a and b
a = 0
b = 1
#Get the Gauss points
[c,r] = gauss_points(n)
area = 0 #initialize area
#Integrate with Gaussian Quadrature
for i in range(n):
    #besure to transform to[-1,1]
    #compute area
    area += c[i] + f(((b-a)*r[i]+b+a)/2)*((b-a)/2)
print("Area =", area)



