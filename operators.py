#so lets use logical operators to see different results

whats_temp = int(input("Enter current temperature: "))

if whats_temp <= -20:
    print("It's very cold outside :/")
elif whats_temp <= -10:
    print("Its so cold today ahh :!")
elif whats_temp <= 0:
    print("Its cold outside :/")
elif whats_temp <= 10:
    print("Weather is bit cold today :L")
elif whats_temp <= 20:
    print("Weather looks cool today :D")
elif whats_temp <= 30:
    print("Weather is good today :)")
elif whats_temp <= 40:
    print("Weather looks hot today :l")
elif whats_temp <= 50:
    print("weather looks very hot today :L")
else:
    print("Weather is extremely hot today! :/")


