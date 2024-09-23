# Simple Shopping Cart Program using pYTHON

# Get item details

print("Welcome to the Counter!")
def shopping_cart():
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item}: "))
    quantity = int(input(f"Enter quantity of {item}: "))

    # Calculate total
    total = price * quantity

    # Display summary
    print(f"\nYou have bought {quantity} x {item}(s)")
    print(f"Price per item: ${price:.2f}")
    print(f"Total cost: ${total:.2f}")

    # Ask if user wants to continue
    continue_shopping = input("\nWould you like to add another item? (yes/no): ").strip().lower()

    if continue_shopping == 'yes':
        print("Restarting the shopping process...")
        shopping_cart()
    
    else:
        print("Thank you for your purchase!")

shopping_cart()
