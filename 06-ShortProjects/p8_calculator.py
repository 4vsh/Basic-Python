import math



print("\t\t Welcome to Simple Mathematical calculator")

print()
f = "y"


def add():

    final = fnum + snum
    print(f"{fnum} + {snum} = {final}")

    pass

def sub():
    final = fnum - snum
    print(f"{fnum} - {snum} = {final}")

    pass
def mup():

    final = fnum * snum
    print(f"{fnum} * {snum} = {final}")
    pass

def div():

    final = fnum / snum
    print(f"{fnum} / {snum} = {final}")
    pass

def rem():
    final = fnum % snum
    print(f"{fnum} % {snum} = {final}")


while f == "y":

    fnum = float(input("Enter first number: "))
    sy = input("Enter symbol betn them (+,-,*,/,%): ")
    snum = float(input("Enter second number: "))


    if sy == "+":
        add()
    elif sy == "-":
        sub()
    elif sy == "*":
        mup()
    elif sy == "/":
        if snum == 0:
            print("Can't Be divide by Zero '0'")
        else:
            div()
    elif sy == "%":
        if snum == 0 or fnum == 0:
            print("Number can't be Zero '0'")
        else:
            rem()
    else:
        print("Value input error :/")

    f = input("Want to use again? (y/n)?:  ").lower()

print("Thanks for using Bye! Made with ❤️ by Aavash. ")
