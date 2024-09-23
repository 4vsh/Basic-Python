#args pack all arguments into tuple

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


a = sum(2,5,55,44441)
print(a)