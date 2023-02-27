#for-loop with else statement
for x in range(9): 
    var = x + 1
    print(f'Iteration no {var} in for loop.')
    if x == 6: 
        break
else:
    print("End with the loop.")    