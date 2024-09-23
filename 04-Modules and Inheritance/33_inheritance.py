class animal:
    alive = True
    def eat(self):
        print("Animal is eating!")

    def sleep(self):
        print("Animal is Sleeping")

    def dead(self):
        print("Animal is dead! :/")


class Rabbit(animal):
    alive = False

    def sleep(self):
        print("Animal is not sleeping")

    pass

class Fish(animal):
    def breathe(self):
        print("Fish is breathing :o")
        pass

class pig(animal):
    pass

rab = Rabbit()
fis = Fish()
Pig = pig()

print(animal.alive)
print(rab.alive)
print(fis.alive)
print(Pig.alive)
print()



rab.eat()
fis.sleep()
rab.sleep()
fis.breathe()
#byeee
