import random
import string

print("This program translates a message into secret Code lang and also you can Decode the code lang.")
print("")
user_input = input("Enter your message: ")
print("")
Coding = int(input("1 for Coding and 0 for Decoding: "))
print("")


#for random module
length = 3
characters = string.ascii_uppercase + string.ascii_lowercase + string.hexdigits
r1 = ''.join(random.choice(characters) for i in range(length))
r2 = ''.join(random.choice(characters) for i in range(length))

words = user_input.split(" ")
if Coding == 1:
    nwords = []
    for word in words:       
        if len(word) >= 3:
            st = r1 + word[1: ] + word[0] + r2           
            nwords.append(st)    
        else:
            nwords.append(r1 + word[: :-1])
    print("Result: "," ".join(nwords).lower())
    print("") 
elif Coding == 0:
    nwords = []
    for word in words: 
        if len(word) >= 9: 
            st =  word[3: -3]
            st = st[-1] + st[ : -1]
            nwords.append(st)
        elif len(word) <= 5: 
            st = word[3:]
            st = st[: : -1]
            nwords. append(st)
    print("Result: " ," ".join(nwords).capitalize())
    print("")   
else: 
    raise ValueError("Not a valid number.")       