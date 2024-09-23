#dictonary in python its changable
#they are fast bcz they use hashing method and they are unordered as well as they are the collection of unique keys and stuff like that
places = {'Kathmandu':'New Road', 'Paris':'Spain', 'China':'beijing', 'Nepal':'Kathmandu'}


print(places['Paris'])
print()

#using get method instead of line 6

print(places.get("Hetauda"))
print()
print(places.values())

#using for loops to display all items
print()
for key,value in places.items():
    print(key,value)

#updating the keys and values inside the dictionary

print()
places.update({"Manang":"Mustang"})

for key,value in places.items():
    print(key,value)

#lets remove a key value using .pop

places.pop("Kathmandu")
print(places)

print(places.clear())




