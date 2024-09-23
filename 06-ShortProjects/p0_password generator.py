import random

symbols = list("@#$%^&_*()")

lpc = list("abcdefghijklmnopqrstuvwxyz")

upc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

dig = list("0123456789")

print("\n \t \tWelcome to random password generator!")

while True:
    try:
        num = int(input("\nEnter number of passwords you need: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        total_char = int(input("Enter total number of characters for each password: "))
        if total_char < 8:
            check = input("Password is too short. Do you want to continue? (y/n): ").lower()
            if check == "y":
                break
            elif check == "n":
                continue
            else:
                continue
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

finalpw = symbols + lpc + upc + dig

print("+------------------------------+")
sn = 1
print("Here are your passwords: ")
for i in range(0, num):
    passwords = ''.join(random.choices(finalpw, k=total_char))
    print("+----------------+")
    print(f"{sn}. {passwords}")
    sn += 1

print("+----------------+")
print("\n\t\t Thank you for using this tool made with ❤️ by Aavash!")
