# i am doing for linear function , you can customixed this fucntion accordily


def f(x):
    return x 


def trapezoidaIntegration(a , b  , N = 1000 ): 
    #width 
    width  = (b- a ) / N
    sum = 0 # sum of ares of trapezoids  == integral

    #evaluate function at f(a)
    sum += f(a) 

    #considering the internal points between a  and b 
    for i in range(1 , N):
        x = a + i*N
        sum += 2 * f(x) 

    #evaluate the function at f(b)

    sum += f(b)

    return (width * sum )/ 2 




"""
explnation : 
real formula is = h/2  * sumation (f(x) + f(x+1))
so ,  on lenthing this we get  
h/2 * f(x) + 2(fx2) + 2(fx3) .... f(n+1)

so we calucate  , f(x) seperatly and  for 2*.. we loop and again seprelatly sum (f(n+1) that is b )


"""
if __name__ == '__main__':
    print(trapezoidaIntegration(0 , 1 ))
         


