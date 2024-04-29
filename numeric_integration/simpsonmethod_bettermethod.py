
"""
it is beteer than rectangle or trapezodia methods , because it is polinomial 
and  , work by  interpolation 


""" 
def f(x):
     return x*x


def simpson_method(a , b , N = 10000):
    width = (b - a) / N
    sum = 0 
    sum += f(a)

    #evaluate f(x0) and f(xn) i.e f(a) and f(b)
    sum += f(a)  + f(b)


     #consider the internal point with 4 as constant (every second)
    for i in range(1 , N ,2 ):
          x = a + i * width
          sum += 4 * f(x)

    # consider the internal points with 2 as constant (every second point)
    for i in range(2 , N , 2):
         x = a + i * width
         sum += 2 * f(x)

    
    return  (width * sum / 3 ) 


print(simpson_method(0 , 5 ))