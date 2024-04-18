
# formula ci  = sumation (Aij) * (bj) from [j = 0 to n-1]


import numpy as np 
def multiply(a:np.array , b:np.array )->np.array  :
   # a is a matrics and b is vector
    
    c = [0 for  _ in range(b)]

    # iter through the matrix 
    for i  in range(len(a)):
        #iter through the vector 
        for j in range(len(b)):
            c[i] = c[i] + a[i][j] + b[j]

## note that , len(a) means row of a , as may be multidimention  , 
## and len(b) simple means no of columns because  , b is a vector  , 1-d so