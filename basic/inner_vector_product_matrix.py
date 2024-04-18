#steps
# say you have two mataric a and b 
# multiply  same index elements of two matrix i.e a[0] * b[0]
#and then sum ,for 3 columns 
# a[0] * b[0] + a[1]*b[1] + a[3]*b[3]

# universal formula sumation (ai*bi) from j = 0 to n-1 


############code
def InnerVector_product(a, b):
    # to store 
    c = 0 
 
    for i in range(len(a)):
        c += a[i] * b[i]
    return c 

print(InnerVector_product([1 ,  2 ] ,[4 , 2 ]))


########################## or #########################
def multiplyInner_Product(a , b ):
    return sum([i*j for (i , j) in zip (a,b)])

print(multiplyInner_Product([1 ,  2 ] ,[4 , 2 ]))

        












