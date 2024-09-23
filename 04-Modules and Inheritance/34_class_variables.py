#nothing much here just simple as variables but inside and outside of the class :) let goo



class monkey:

    eyes = 2

    def __init__(self, nose, ear, head, tail):
        self.nose = nose
        self.ear = ear
        self.head = head
        self.tail = tail


monkey1 = monkey("3M", "4pcs", "1pc", "1pc")
monkey2 = monkey("2M", "1pcs", "1pc", "2pc")


monkey1.eyes = 5 #changing value if eyes of a obkect monkey1



print(monkey1.eyes)
print(monkey2.eyes) #monkey2 will use same default number used in class monkey above

