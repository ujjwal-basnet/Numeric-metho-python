import numpy as np 
def f(x):
    return x*x 





class montecarlo():
    def __init__(self , a , b , N = 100):
        self.a = a 
        self.b = b 
        self.N = N 



    def run(self):
    # count the nuber of generated ponts under f(x)
        counter = 0 

        for _ in range(self.N):
            random_x = self.generate_random()
            random_y = self.generate_random()

            if self.is_below(random_x , random_y):
                counter += 1 
        
        return (self.total_area()* counter) / self.N ## main formula 



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
    algo = montecarlo(a = 1 , b = 2 ,N  =  1000)
    print(algo.run())
    print("You can see it does't work good , because it is in 1-d or lower dimenstion  , simpson algorithm works better  ")

    print("but in higher dimention it works better")