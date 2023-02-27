#Program for printing fabonacii
def fibonacii(n): 
    '''This programs prints fabonacii in a sequence using for loop  '''
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return  fibonacii(n - 1) + fibonacii(n - 2)    
#checking if validate
print(fibonacii.__doc__)
n = int(input('Enter the required fibonacii number =>'))
print('Required Fibonacci sequence:')
while n == 0:
    n = int(input('Enter the required fibonacii number =>')) 
    print('Required Fibonacci sequence:')
    for i in range(n): 
        print(fibonacii(i))
#end of validate        
for i in range(n): 
    print(fibonacii(i))
                            
    