def multiply(a ,b ):
    #New matrix formed after multiplication of two matrics will be 
    # Row of A  * Column of B and here
    # in list 
    # len(a) means row of a 
    #len(a[0]) means column of a this is because in python matrix is list of list 
    # thus len(a) counts no of inner list 
    #and len(a[0]) counts no of elements in first row 
    
    #create two dimension matrix to store the result
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    
    #iter through the rows of matrix A 
    for i in range(len(a)):
        pass 
        for j in range(len(b[0])):
            pass 
        
        for k in range(len(b)):
            c[i][j] = a[i][j]+c[i][j]
    return c 

if __name__ == '__main__':
    print(multiply([[10 , 4] ,[2 ,3]] , [[9 , 3] , [4 ,5]]))
            
    