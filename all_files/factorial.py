#factorial using recursion
#demo of factorial(3) = 3*2*1
def factorial(n): 
    if n == 0 or n == 1: 
        return 1
    else: 
        return n*factorial(n -1)
#var = 3
print(factorial(n = int(input("Enter required factorial number:"))))

#factorial 4 * factorial(3)
#factorial 3 * factorial(2)
#factorial 2 * factorial(1)
#returns 1