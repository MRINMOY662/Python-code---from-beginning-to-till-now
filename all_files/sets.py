#Sets
#1. union()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Los Angeles", "Madrid"}
cities.update(cities2)
print(cities)

#2. intersection()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

#3. symmetric_difference()
cities = {" Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#4. difference()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities. difference_update(cities2)
print(cities)

#5. isdisjoint()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#6. issuperset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo",  "Madrid"}
print(cities.issuperset(cities2))

#7. issubset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo",  "Madrid"}
print(cities2.issubset(cities))

#8. add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("symbols")
print(cities)

#9. remove()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Madrid")
print(cities)

#pop()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.pop()
print(cities)

#del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
#print(cities) #it'll throw error. 

#clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities. clear()
print(cities)

#checking if item exists
info = {'Carla', 19, False,  5.9}
if "Carla" in info: 
    print('Carla is present.')   
else: 
    print('Carla is absent.')