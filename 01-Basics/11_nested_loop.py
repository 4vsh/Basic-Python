#nested loops [simply loops under loop]

print("Printing a symbol using your input! :O")

row = int(input("Enter no of rows: "))
column = int(input("Enter no of columns: "))
symbol = (input("Enter what symbol you want to print: "))


for i in range(row):
    for j in range(column): #always remember first inner loop work /complete its function the  it will go to outer loop
        print(symbol, end="")
    print()

