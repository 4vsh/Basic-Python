#it interrupts the flow of program

try:
    first = float(input("Enter first number to divide: "))
    sec = float(input("Enter second number to divide: "))
    x = first/sec

except ZeroDivisionError:
    print(f"{first} can not be divide by 0 :/")


except ValueError:
    print("Enter Numbers not values !")



except Exception:
    print("Something went wrong :(")

else:
    print(x)

finally:
    print("Thanks :) ")