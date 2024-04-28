from math import sqrt

def f(x):
    return x**2 - 2 
"""
    this is 
    f(x) = x**2 - 2 
    0 = x**2 -2 
    x^2 = 2 
    x  = root(2)

so we will find solution for root(2) here ,
"""



def bisection_method(xpos, xneg , eps = 1e-15): # making more precise  , it might take longer time 
    middlepoint = 0 
    
    while abs(xpos - xneg ) >  eps:
        middlepoint = (xpos + xneg ) /   2 

        if f(middlepoint) > 0 :
            xpos = middlepoint
        else :
            xneg = middlepoint

    return middlepoint



print(bisection_method(2, -2))
print(sqrt(2))

assert abs(sqrt(2) - bisection_method(2  , -2 ))== 0 , "Increase eps , bisection method does't approach rightly"
