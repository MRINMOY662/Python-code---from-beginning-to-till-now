#List example
lst1 = [1, 2,3,4,5,6,7,8,9]
lst2 = ["Python", "Physics", "Mathematics","No rocket science only pure and applied mathematics.",13578977,797668888," python list", 35789876556777,6665555,656666677,6677,"Sarah","Anastasia"]
print(lst1)
print(lst2)
print(lst2[3])
print(lst2[-1])
if "Python" in lst2:#checking values if exists or not 
    print("I need some space.")
else: 
    print("Rocket science is not available.. ")
print(lst2[1:7:2])#printing alternate values

#generating list using for loop
str = ["Red","Blue","Green","Black","White"]
for string in str: 
    print(string)
    for i in string: 
        print(i)        

#list comprehension
lst = [i for i in range(99)] 
print(lst)
print(["carrot", "elon musk", " mrinmoy"])
#printing leap year using for-loop  
lst3 = [i for i in range(2000,2065) if i%4 == 0]
print(lst3)