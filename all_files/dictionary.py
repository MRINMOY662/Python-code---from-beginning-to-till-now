#Looping through a dictionary
info = {'name':'George Washington', 'age':"16", 'eligible':True}
for dis in info:
    print(info[dis])
for iterate in info.items(): 
    print(iterate)
for key in info.keys(): 
    print(f"The value corresponding to the key {key} is {info[key]}")       
for key,  value in info. items(): 
    print(f"The value corresponding to the key {key} is {info[key]}") 
    
#best method of writing
person = {
   "first_name": "Mrinmoy",
   "last_name": "Deka",
   "age": 16
}
print(1., person)
#Accessing items
x = person['first_name']
y = person['last_name']
z = person['age']
print('Name:', x, y,'\nAge:',z)
#Adding new item
person["hobby"] = "playing Minecraft"
print(person)
#Changing value
person['first_name'] = "Mrinmoy"
print(2., person)
#Removing an item
person. pop("age")
print(3., person)
#Getting length
print('Length =', len(person))
#checking if a key exist
if "age" in person: 
    print("Age is present.")
else: 
    print("Age is absent.")
#Deleting an item
del person["first_name"]
print(person)       
        
    
    