"""

previous multicarlo was not that good because we inititall does;t know , 
bounding box , so what we can do ?
here we caluatate the y(i.e f(x)) for generated random x and put on the our main formula 
and calualte mean ,  
"""

import numpy as np 
def f(x):
    return x*x *x 





class montecarlo():
    def __init__(self , a , b , N = 100):
        self.a = a 
        self.b = b 
        self.N = N 



    def run(self):
    # count the nuber of generated ponts under f(x)
        sum = 0 

        for _ in range(self.N):
            random_x = self.generate_random()
            sum += f(random_x) * (self.b - self.a)  # height * weight = area so summing araa

        return sum / self.N # average 
 
         



    # generate random floating in range [a , b ]
    def generate_random(self):
        #generate random number between  range a and b 
        return self.a + (self.b - self.a) * np.random.uniform()
    """
    np.random.uniform()  -> returns flot values between 0-1 i.e vary close to zero to very close to 1  
    """
    # check if the generated point is below the f(x) function or not 
    @staticmethod
    def is_below(x , y ) :
        if y < f(x):
            return True 
        
        return False 
    
    def total_area(self):
        """
            we are going for square as a boundry box ,
            thus squar  wedith and height is equal 
            weidth can be calucate as b-a 
            thus 
        """
        return (self.b - self.a) * (self.b - self.a )
        

        
if __name__ =='__main__':
    algo = montecarlo(a = 0 , b = 5 ,N  =  100000)
    print(algo.run())
    