#else statement with for and while loop
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

num = int(input("Enter an iterable number => "))
while num >= 2:
    print(num) 
    num = num - 1
else: 
    print("Done with the loop.")   
