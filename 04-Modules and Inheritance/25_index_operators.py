#index operators it gives access of an element of the sequence
#[]


name = "aavash Aryal"

if (name[0]).islower():
    name = name.capitalize()

print(name)

first_name = name[0:6]
last_name = name[7:].capitalize()

print(first_name)
print(last_name)
print(name[-1])