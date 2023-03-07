#Python random module
import random
import string

# Define the length of the random string
length = 3

# Define the characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the random string
random_string = ''.join(random.choice(characters) for i in range(length))

print(random_string)

length = 3
characters = string.ascii_uppercase + string.ascii_lowercase + string.hexdigits
r1 = ''.join(random.choice(characters) for i in range(length))
print(r1)
