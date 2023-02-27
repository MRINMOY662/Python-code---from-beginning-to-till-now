#exception handling
try:
    num = int(input(" Enter an interger to get square power => "))
    print( num ** 2)
except ValueError: 
    print(" Number entered is not valid.")
finally:
    print(" I am always get executed.")       