#break, continue and pass

while True:
    name = input("Enter your name here: ")

    if name != "":
        break
#using continue
print("\n Now using continue \n")
student_id = "123-456-789"

for i in student_id:
    if i == "-":
        continue

    print(i, end="")


#using pass
print("\n")

name = "Aavash"

for i in name:
    if i == "A":
        pass
    else:
        print(i, end="")


