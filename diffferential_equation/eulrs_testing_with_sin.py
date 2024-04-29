import numpy as np 
import  matplotlib.pyplot as plt 

def f(x , y ):
    return np.cos(x)

# this is initial condition 
def eulear_method(x = 0 , y = 1 , step = 0.01):
    x_values = []
    y_values = [] 
    while x < 10 :
        x_values.append(x)
        y_values.append(y)
        
        y = y + step * f(x , y )
        x = step + x 

    return x_values  , y_values 


x_values , y_values = eulear_method()
plt.plot(x_values , y_values)
plt.show()