import os
try:

    with open("test.txt") as file:
        print(file.read())


except FileExistsError:
    print("File Do Not Exist in given directory!")

except FileNotFoundError:
    print("File Not Found Error :/")

else:
    print("Thanks! ")

