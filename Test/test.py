print("")
print("Welcome to this program \n")
user_input = input("Enter your message: ")
words = user_input.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding == "1") else False
if (coding):
    nwords = []
    if (len(user_input)) >= 3:
        rand1 = "rhj" 
        rand2 = "fvi" 
        st = rand1 + user_input[1:] + user_input[0] + rand2
        nwords.append(st)           
    else:
        print(user_input[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    if len(user_input) >= 3:
        stnew = user_input[3:-3]
        stnew = stnew[-1] + stnew[:-1]
        nwords.append(stnew)
    else:
        nwords.append(user_input[::-1])
    print(" ".join(nwords))
