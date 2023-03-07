num = int(input("Enter a number between 5 and 9: "))
if not 5 <= num <= 9: 
    raise ValueError("Not a valid number.")