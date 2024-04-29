import numpy as np
import matplotlib.pyplot as plt 



# derivative function 
def f(x , y ):
    return y 



def euler_method(x = 0 , y = 1 , step = 0.1 ):
    x_values = [] 
    y_values = [] 

    while x < 10 :
        x_values.append(x)
        y_values.append(y)
        y = y + step * f(x ,y )
        x = x + step 

    plt.plot(x_values , y_values)
    plt.show()


euler_method()