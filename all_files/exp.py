def exp(x,y):
    '''This program executes exponents using recursion''' 
    if y == 0: 
        return 1
    else: 
        return x*exp(x,y - 1)
print(exp.__doc__)          
var = int(input ('Enter the first number =>'))
vas = int(input ('Enter the first number =>'))
print('Result = ', exp(var, vas))       