#list-methods

#sort method
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
alp = ["motion", "distance", " displacement", "speed", " velocity", "acceleration"]
num. sort(reverse = True)
alp. sort()
print(num)
print(alp)

#reverse method
num = [8, 8,6,5,7,6,7,77,56788,334,666]
num. reverse()
print(num)

#index method
colors = [" red", "green"," blue","yellow","white"]
print ( colors.index("white"))

#count method
colors = [" red", "green"," blue"," red","white","black"," red"]
print(colors.count(" red")) 

#copying list
lst = [1,  2, 3, 4, 5]
print(lst)
m = lst
m[0] = "Nikita"
print(m)

#count method
fav = ["Kiara Advani", "Danyka Nadeau", " Nikita"]
newest = fav.copy()
newest[1] = "Null"
print(fav)
print(newest)

#append method
colors = [" red", "green"," blue"," red","white","black"," red"]
colors.append("orange")
print(colors)

#insert method
colors = [" red", "green"," blue"," red","white","black"," red"]
colors. insert(2, "nikita")
print(colors)

#extend method
colors = [" red", "green"," blue"," red","white","black"," red"]
fav = ["Kiara Advani", "Danyka Nadeau", " Nikita"]
colors.extend(fav)
print(colors)