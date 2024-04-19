
import numpy as np 

def gaussian_elimination(a, b):
    n = len(b)
    # set all the values under the diagonal to be zeros
    # going through all columns , note that range doest include n-1 so it is actullay  , n to n-2
    #
    for k in range(n - 1):
        # we have to set all the values below the pivot row to be zero
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                # this is how we determine the value that will make the actual value 0
                lam = a[i, k] / a[k, k]
                a[i, k:n] = a[i, k:n] - lam * a[k, k:n]
                b[i] = b[i] - lam * b[k]

    return a ,  b 

if __name__ == '__main__' :
    print(gaussian_elimination(np.array(

        [[1.,5.,-2.]  , 
         [2. , 3. , 1. ] ,
        [2. , 4.,-3.]]) ,
        np.array([2.  , 5. , 2.])))

  