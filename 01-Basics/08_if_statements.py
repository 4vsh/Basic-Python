#if statements in python

name = input("Enter Your Name: ")
age = int(input("Enter your age: "))

if age <= 17 and age >0:
    print(f"You are still teenager {name}")
elif age < 0:
    print(f"You are still inside your mothers stomach eheh!")


else:
    print(f"You are an adult {name}")

