from  forward_elimination import gaussian_elimination 
import numpy as np 

def back_susbstitution( A ,b ):
    n = len(b)
    A , b  = gaussian_elimination(A , b )

    #now , 
    for k in range(n-1 , -1 , -1): #
        # this will loop from last  to first why ?
         # see  usally after forward elimination matrix will look like this 
        #     1   2  3  | some number 
        #     0   4  5  | some number 
        #     0   0  3   | some number


        # so we have to first find value of z cuz it is east then , 
        # put value of x in 2nd row  , and find value of y 
        # so on put value of z and  x in 1st row and find value of x 
        # this hole process called back-propagration 
    
    
        b[k] = (b[k] - np.dot(A[k, k + 1:n], b[k + 1:n])) / A[k, k]

    print(b)

if __name__ == '__main__':
    print(back_susbstitution(np.array([[1., 1.], [0.035, 0.05]]), np.array([24000., 930.])))



