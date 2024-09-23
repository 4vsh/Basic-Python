# :=

happy = False

print(happy)

#using walrus operator

print(happpy := False)

print("+---------------------+")

foods = list()

#while True:
#    food = input("Enter food name [type q to quit] :  ")
#    if food == "q":
#        break
#    foods.append(food)
#print()


#doing same using walrus operator :0
                                                           #used second bracket bcz the operator presendence of != which comes first, it gives you true or false by comparing input with q so use small bracket to run the input code first not != q code :)
while (food := input("Enter food name [type q to quit] : ")) != "q":
    foods.append(food)



#just printing
print("Here is your food list :")
for i in foods:

    print(i)

print("Thanks for using this tool")
print("Bye")



