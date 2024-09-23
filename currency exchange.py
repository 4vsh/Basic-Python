#making currency exchange using python

#usd to rs


def usdtors():
    ucurr = float(input("Enter Amount in USD: "))

    fcurr = ucurr * 134.25

    print(f"Amount in Rs : {fcurr} Rs.")


def rstousd():
    ncurr = float(input("Enter Amount in Rs.: "))

    fcurr = ncurr / 134.25

    print(f"Amount in Rs : {fcurr} $")

#main code

print("Welcome to money value exchange tool")


while True:
    print("Type usd to change to usd or Type rs to change to rs type q to quit.")
    choose = input("").lower()
    if choose == "usd":
        rstousd()
    elif choose == "rs":
        usdtors()

    elif choose == "q":
        break

    else:
        print("Something went wrong :/ please try again. ")

        break



print("Thanks for using this tool. Made with love by Aavash :)")
