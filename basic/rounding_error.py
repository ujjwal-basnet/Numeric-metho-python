num  = 10 
s = 0 

# run loop 100 times
for _ in range(100):
    s = s + 0.1 
    
print('s is ' , s)
print('num is ' , num)
print('both equal  ?  ' , s == 10 )

#outcome is false and this is not good approach 

#this above code shows value of s is 9.9.99999999999998 
# but this should be 10 as 0.1 *100 = 10 



#to clear this type of erros we have rounding errors 

num = 10 
epsilon = 0.0001
if abs(s - num)   < epsilon :
    print("Both numbers are same ")
