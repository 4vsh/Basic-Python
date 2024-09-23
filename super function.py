#super function in python Parent class in dogs and cat
class Animal:       #parent class
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some sound"

class Dog(Animal):              #shepard

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        parent_sound = super().sound()
        return f"{parent_sound}, but specifically, I bark."

class Cat(Animal):              #cat
    def sound(self):
        return "I meow."

dog = Dog("Buddy", "CRUXXXXX")
cat = Cat("astroid Destroyer")

print(dog.sound())  # I bark
print(cat.sound())  # I meoww