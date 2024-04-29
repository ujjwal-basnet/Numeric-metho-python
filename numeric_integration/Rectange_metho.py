

# define the funciton which you want perform integration
# for example here i am going to  for quardatic function 

def f(x):
    return x*x


def rectangle_integral(a, b , N = 1000000000):
    # width of single rectable 
    h = b -a /N
    #sum of the integral (area under the curve of f(X) function )
    sum = 0 

    for i in range(N):
        sum+= h*f(a+ i * h )

    return sum

if __name__ == '__main__':
    print(rectangle_integral(2 ,3 ))