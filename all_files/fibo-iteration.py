def fibonacci(n):
    '''This is my second iteration of Fibonacci''' 
    if n == 1: 
        return 1
    elif n == 0:
        return 0   
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
print(fibonacci.__doc__)        
n = int(input ("Enter a number =>")) 
for i in range (fibonacci(n)): 
    print("Fibonacci(",i,") = ", fibonacci(i))