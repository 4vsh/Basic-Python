class grandpa:
    name = "Grandpa"
    surname = "Aryal"

    def grand(self):
        print("grandpa here always ready with a story")


class father:
    name = "Father"

    def father(self):
        print("I'm Dad. I have a lot of dad jokes but no one to listen :/")

    def grand(self):
        print("Father here. I inherit some things from Grandpa ans also added my own things.")


class mother:
    name = "Mother"

    def mother(self):
        print("Mom here, doing everything !")

    def grand(self):
        print("Mom here I have  skills and some slipper superpower {iykyk}:XXX :/")


class son(father, mother, grandpa):  # Inherits from father, mother, and grandpa bruh is hybrid of all
    name = "Son"

    def grand(self):
        print("WAZZUP I'm the Son! I have all the cool things from my parents and added my own things!")



myson = son()
Father = father()
Mother = mother()
Grand = grandpa()

Grand.grand()
Father.grand()
Mother.grand()
myson.grand()  # simply bro is hybrid cz u can see bro inherit all his parents and grandpa//////bye/////!!!
