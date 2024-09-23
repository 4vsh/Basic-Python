item = input("Please enter item name here: ")
cash = float(input(f"Enter price of {item}: "))
quantity = int(input(f"Please enter total quantity of {item} : "))

total_amt = cash*quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is : ${total_amt}")
