#tupple is similar to list but unchangable

subjects = ("Maths", 1998, 'Boring')

print(subjects.count("Boring")) #counting certain value how many times it appears
print(subjects.index("Boring"))

for i in subjects:
    print(i)


if "Maths" in subjects:
    print("Maths is inside the tuple")
else:
    print("There is no such thing ")

