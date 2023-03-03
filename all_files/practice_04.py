# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
print("")
print("Welcome to this program \n")
user_input = input("Enter your text: ")
if len(user_input) >= 3: 
    # user_input.replace[0]
    st = user_input[1:] + user_input[0]
    print(st)
    
else:
    print(user_input[::-1])
    # user_input.r  
