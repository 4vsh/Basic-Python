#not exactly random but it is close to it also called as pseudo random number


import random

r = random.randint(0,6)
print(r)

list = ["Aavash", "Aryal", "Kathmandu", "Nepal"]

f = random.choice(list)

print(f)


#Random cards picker

allcards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "J" ]

random.shuffle(allcards)
print(allcards)
