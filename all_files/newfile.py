
#-----Begining of python------

print('hello world! I\'m Mrinmoy') #first program of python

name='Juan' '''Changing variable value'''
name='Nord'
print('Hello'+ ' '+name)

#------------------------------------Data-types

a=3 #getting numerical value
b=3.3
d='python'
e=4.21j
print(type(a))
print(type(b))
print(type(d))
print(type(e))
#------------------------------------Taking Round off

pi = 3.1415926535897 # this is the pi number
two_decimals = round(pi, 2)
three_decimals = round(pi, 3)

print(two_decimals)
print(three_decimals)

x = pow(4, 2) # same as 4 * 4
y = pow(4, 3) # same as 4 * 4 * 4

print(x)
print(y)
#------------------------------------

#--------------------

x = 4
x = float(x)

print(x)

#-------------------

x = "4.3"
sum = float(x) + 6.5

print(sum)

#------------------

x=4
sum=float(x)
print(sum)
#---------------------Typecasting to int

y = 5.4
print(int(y))

#----------------Another example of typecasting
string = "24"
x = 5
print(int(24)+5)

#---------------------Strings
name = 'JavaScript'
print(name[0])

#----------------------multi-line strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#-------------replace
str1 = "Silver spoon"
print(str1.replace("Silver", "Gold"))

#-----------split
str2 = " Silver spoon"
print(str2.split(" ")) 

#------------------center
str = " Terminal"
print(str.center(50)) 
print(str.find("T"))

#---------------find
str1 = "mrinmoy-abstract"
print(str1.index("mrinmoy"))

#--------------islower
str1 = "universe"
print(str1.islower())

#for-loop
for i in range(24,70, 8): 
    print(i)
    
name = input('Enter a name:')
for i in range(5,10,2): 
    print(name)
