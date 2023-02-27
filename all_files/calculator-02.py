#-----------------input calculator using if-else and function---------

print("Welcome to the ultimate calculator made using python 🖥")
def op (x,y,): #Functions
    sut = x- y
    print("Subtraction: ", sut)
def sub (x,y): 
    subs = x - y
    print("Subtraction:", subs)
def pr (x,y): 
    prts = x * y
    print("Product::", prts)    
def div (x,y): 
    divs = x / y
    print("Division:", divs)


x=int(input(" Enter the first number:"))
y=int(input("Enter the second number:"))
opr=input("Operator:")

if opr=="+": 
        op (7,y) #Calling function
if opr=="-": 
        op (x, y)
if opr=="*": 
        pr (x,y)     
if opr=="/": 
    div (x,y)        
else: 
    "return: 0"  #returns nothing  