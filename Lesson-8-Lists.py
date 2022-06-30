cities = ['New York', 'Moskow', 'Amsterdam', 'Minsk', 'new deli']   #Creat list 'cites'
print(cities)   #Write list 'cites'
print(len(cities)) #Write length list

print(cities[0]) #write
print(cities[-1])
print(cities[4].title())
print(cities[3].upper())
cities[4] = cities[4].title()

cities[1] = 'Warshaw'
print(cities)

cities.append("Riga")
cities.append("Tallin")
print(cities)

#Insert
cities.insert(4, "Berlin")
print(cities)

#Remove nunber
del cities[-3]
print(cities)

#Remove
cities.remove("New York")
print(cities)

#Sort
deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)
print(cities)
cities.sort()
print(cities)
cities.reverse()
print(cities)

