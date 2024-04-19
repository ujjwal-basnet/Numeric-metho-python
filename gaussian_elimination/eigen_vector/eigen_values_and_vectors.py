
# we will use numpy linearalzebra to caclulate eigen vectors and values as  , doing from strach is complex and takes more time ,
# but i will sure do it when i have free time  , and put  on github 

#simple
from numpy import linalg as la 
import numpy as np 

A = np.array([[2 , 3 ] , [5 ,6 ]])
w , v = la.eig(A)

print("eigen values is "  , w ) 

print("eighen vectors are " , v)